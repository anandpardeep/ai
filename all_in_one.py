import fitz  
import base64
from typing import List
import os
from dotenv import load_dotenv
from openai import OpenAI
import openai
import pymupdf4llm

filename="/Users/anandpardeep/AI/CrowdStrikeGlobalThreatReport2025.pdf"


all_pages_pdf = pymupdf4llm.to_markdown(filename, write_images=True,image_path="/Users/anandpardeep/AI/images",extract_words=False,show_progress=True,force_text=False,page_chunks=True)

import pathlib
#pathlib.Path("output.md").write_bytes(all_pages_pdf.encode())

for page in all_pages_pdf:
    page_number = page['metadata']['page']    
    print(page_number)
    print(page)