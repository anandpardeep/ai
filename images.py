import pdfplumber
import openai
import base64
import io
from PIL import Image
from dotenv import load_dotenv
from openai import OpenAI
import openai
from  extractor import Extractor
from content_elements import *
from extractor import *
from prompt_templates import PromptTemplates

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = openai_api_key
client = OpenAI(api_key=openai_api_key)
def page_to_base64(page):
    """
    Render a pdfplumber page as image and return its base64-encoded PNG.
    """
    img = page.to_image(resolution=300).original.convert("RGB")
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

def ask_gpt4v(image_b64, page_number):
    prompt = PromptTemplates.image_summary_prompt()
    try:
            response = client.responses.create(
                model="gpt-4.1",
                input=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "input_text", "text": f"This is page {page_number} of a PDF. Convert it to structured markdown using tables where appropriate."},
                            {"type": "input_image", "image_url": f"data:image/png;base64,{image_b64}"}
                        ]
                    }
                ]
            )
            return response.output_text.strip()
    except Exception as e:
        print(f"[ImageSummarizer] Error: {e}")
        return "NA"


def extract_pdf_to_markdown(pdf_path, page_numbers=None):
    with pdfplumber.open(pdf_path) as pdf:
        pages = page_numbers or range(len(pdf))

        for i in pages:
            print(f"Processing page {i + 1}...")
            page = pdf.pages[i]
            img_b64 = page_to_base64(page)
            markdown = ask_gpt4v(img_b64, i + 1)

            print(f"\n--- Markdown for Page {i + 1} ---\n")
            print(markdown)
            print("\n" + "="*80 + "\n")

# Example: Extract just page 7 (index 6)
extract_pdf_to_markdown("CrowdStrikeGlobalThreatReport2025.pdf", page_numbers=[27])
