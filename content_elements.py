# content_elements.py
import numpy as np
from typing import List
from dataclasses import dataclass,field
import re
import os
from pathlib import Path
import pandas as pd
from abc import ABC, abstractmethod
import base64
from image_summarizer import ImageSummarizer

@dataclass
class ContentElement(ABC):
    """Base class"""
    x0: float
    y0: float
    x1: float
    y1: float
    page_num: int
    element_type: str = field(init=False)
    column: int = field(default=0,init=False)  
    
    @property
    def center_x(self) -> float:
        return (self.x0 + self.x1) / 2    
 
    @abstractmethod
    def to_markdown(self, avg_font_size: float = 12, summarizer: ImageSummarizer=None) -> str:
        pass

@dataclass
class TextElement(ContentElement):
    text: str
    font_size: float
    font_flags: int
    
    def __post_init__(self):
        self.element_type = "text"
        
    def to_markdown(self, avg_font_size: float = 12, summarizer: ImageSummarizer=None) -> str:
        text = self.text.strip()
        if not text:
            return ""
        
        text = re.sub(r'\n+', '\n', text)
        return f"{text}\n\n"        
    
@dataclass
class ImageElement(ContentElement):
    image_data: bytes = None
    image_path: str = ""
    
    def __post_init__(self):
        self.element_type = "image"        
            

    def to_markdown(self, avg_font_size: float = 12, summarizer: ImageSummarizer=None) -> str:
        if not self.image_data:
            return ""

        # Try to summarize image
        base64_str = base64.b64encode(self.image_data).decode("utf-8")
        image_type = "png"  # or infer from path
        rel_path = os.path.relpath(self.image_path)

        if not self.image_data or not summarizer:
            return f"![Image]({rel_path})\n\n"

        description = summarizer.summarize(self.image_data, image_type="png")

        if description == "NA":
            return f"![Image]({rel_path})\n\n"
        else:
            return f"![Image]({rel_path})\n\n**Summary:** {description}\n\n"

@dataclass
class TableElement(ContentElement):
    table_data: List[List[str]]
    
    def __post_init__(self):
        self.element_type = "table"

    def to_markdown(self, avg_font_size: float = 12,summarizer: ImageSummarizer=None) -> str:
        """Convert table element to markdown"""
        if not self.table_data:
            return ""
        
        markdown = "\n"
        df = pd.DataFrame(self.table_data[1:], columns=self.table_data[0])
        return df.to_markdown(index=False) + "\n\n"        