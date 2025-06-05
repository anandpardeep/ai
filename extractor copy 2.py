# extractor.py
from abc import ABC, abstractmethod
import fitz
import pymupdf4llm
import numpy as np
from typing import List, Dict, Tuple, Union
from dataclasses import dataclass,field
import os
from pathlib import Path
import pandas as pd
from abc import ABC, abstractmethod
from image_summarizer import ImageSummarizer
from dotenv import load_dotenv
from content_elements import *
from pymupdf4llm.helpers.multi_column import column_boxes

class Extractor(ABC):
    @abstractmethod
    def save_markdown(self) -> str:
        """Extract the full document content in a normalized format (e.g., Markdown or plain text)."""
        pass    

class PDFExtractor(Extractor):   
    def __init__(self, pdf_path: str, image_output_dir: str = "extracted_images",image_summarizer: ImageSummarizer=None):
        self.pdf_path = pdf_path
        self.doc = fitz.open(pdf_path)
        self.image_output_dir = Path(image_output_dir)
        self.image_output_dir.mkdir(exist_ok=True)
        self.image_counter = 0
        self.image_summarizer=image_summarizer
        
    def extract_text_elements(self, page: fitz.Page, page_num: int) -> List[TextElement]:
        
        """Extract text elements with their spatial positions"""
        text_dict = page.get_text("dict")
        elements = []
        
        for block in text_dict["blocks"]:
            if "lines" in block:  # Text block
                block_text = ""
                font_sizes = []
                font_flags = []
                
                for line in block["lines"]:
                    line_text = ""
                    for span in line["spans"]:
                        line_text += span["text"]
                        font_sizes.append(span["size"])
                        font_flags.append(span["flags"])
                    if line_text.strip():
                        block_text += line_text + "\n"
                
                if block_text.strip():
                    avg_font_size = np.mean(font_sizes) if font_sizes else 12
                    avg_font_flags = int(np.mean(font_flags)) if font_flags else 0
                    
                    elements.append(TextElement(
                        x0=block["bbox"][0],
                        y0=block["bbox"][1],
                        x1=block["bbox"][2],
                        y1=block["bbox"][3],
                        page_num=page_num,
                        text=block_text.strip(),
                        font_size=avg_font_size,
                        font_flags=avg_font_flags
                    ))
        
        return elements
    
    def extract_image_elements(self, page: fitz.Page, page_num: int) -> List[ImageElement]:
        elements = []
        image_list = page.get_images(full=True)
        
        for img_index, img in enumerate(image_list):
            xref = img[0]
            
            img_rects = page.get_image_rects(xref)
            
            for rect in img_rects:

                try:
                    pix = fitz.Pixmap(self.doc, xref)                    
                    self.image_counter += 1
                    image_filename = f"page_{page_num+1}_img_{self.image_counter}.png"
                    image_path = self.image_output_dir / image_filename
                    
                    img_data = pix.tobytes("png")
                    with open(image_path, "wb") as f:
                        f.write(img_data)
                    
                    elements.append(ImageElement(
                        x0=rect.x0,
                        y0=rect.y0,
                        x1=rect.x1,
                        y1=rect.y1,
                        page_num=page_num,
                        image_data=img_data,
                        image_path=str(image_path)
                    ))                    
                    pix = None
                    
                except Exception as e:
                    print(f"Error extracting image: {e}")
                    continue
        
        return elements
    
    def extract_table_elements(self, page: fitz.Page, page_num: int) -> List[TableElement]:
        elements = []
        
        try:
            tables = page.find_tables()
            for table in tables:
                table_data = table.extract()
                if table_data:
                    try:                        
                        elements.append(TableElement(
                        x0=table.bbox[0],
                        y0=table.bbox[1],
                        x1=table.bbox[2],
                        y1=table.bbox[3],
                        page_num=page_num,
                        table_data=table_data
                    ))
                    except Exception as e:
                        print(f"Failed to convert table to markdown: {e}")
                        return ""
                    
        except Exception as e:
            print(f"Error extracting tables: {e}")
        
        return elements
    
    def detect_columns(self, elements: List[ContentElement], page: fitz.Page) -> List[ContentElement]:
        try:
            col_bboxes = column_boxes(page, footer_margin=50, no_image_text=True)
            if not col_bboxes:
                for elem in elements:
                    elem.column = 0
                return elements

            for elem in elements:
                elem_rect = fitz.Rect(elem.x0, elem.y0, elem.x1, elem.y1)
                for idx, col_bbox in enumerate(col_bboxes):
                    if col_bbox.intersects(elem_rect):
                        elem.column = idx
                        break
                else:
                    elem.column = 0  # default if no match
            return elements

        except Exception as e:
            print(f"[detect_columns] Error using column_boxes: {e}")
            for elem in elements:
                elem.column = 0
            return elements
   
    def sort_elements(self, elements: List[ContentElement]) -> List[ContentElement]:
        if not elements:
            return elements
        
        # Group by column
        from collections import defaultdict
        columns = defaultdict(list)
        
        for elem in elements:
            col = getattr(elem, 'column', 0)
            columns[col].append(elem)
        
        # Sort within each column by y-coordinate (top to bottom)
        sorted_elements = []
        for col_num in sorted(columns.keys()):
            col_elements = sorted(columns[col_num], key=lambda x: x.y0)
            sorted_elements.extend(col_elements)
        
        return sorted_elements
    
    def extract_page_with_order(self, page_num: int) -> str:
        page = self.doc[page_num]
        
        text_elements = self.extract_text_elements(page, page_num)
        image_elements = self.extract_image_elements(page, page_num)
        table_elements = self.extract_table_elements(page, page_num)
        
        all_elements = text_elements + image_elements + table_elements
        
        if not all_elements:
            return f"# Page {page_num + 1}\n\n*No content found*\n\n"
        
        all_elements = self.detect_columns(all_elements, page)
        
        sorted_elements = self.sort_elements(all_elements)
        
        font_sizes = [elem.font_size for elem in text_elements if elem.font_size > 0]
        avg_font_size = np.mean(font_sizes) if font_sizes else 12
        
        markdown = f"# Page {page_num + 1}\n\n"
        
        for element in sorted_elements:
            markdown += element.to_markdown(avg_font_size,self.image_summarizer)
        
        return markdown
    
    def extract_full_document(self) -> str:
        full_markdown = ""
        
        for page_num in range(len(self.doc)):
            page_markdown = self.extract_page_with_order(7)
            full_markdown += page_markdown
            
            if page_num < len(self.doc) - 1:
                full_markdown += "\n---\n\n"
        
        return full_markdown    

    def save_markdown(self, output_path: str, use_spatial: bool = True):
        if use_spatial:
            content = self.extract_full_document()
        else:
            content = pymupdf4llm.to_markdown(
                self.pdf_path,
                write_images=True,
                image_path=str(self.image_output_dir)
            )
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Markdown saved to: {output_path}")
    
    def __del__(self):
        if hasattr(self, 'doc') and self.doc:
            self.doc.close()
