# image_summarizer.py

from base64 import b64encode
from prompt_templates import PromptTemplates

class ImageSummarizer:
    def __init__(self, client,model: str ="gpt-4.1"):
        self.client = client
        self.prompt = PromptTemplates.image_summary_prompt()

    def summarize(self, image_data: bytes, image_type: str = "png") -> str:
        base64_str = b64encode(image_data).decode("utf-8")
        try:
            response = self.client.responses.create(
                model="gpt-4.1",
                input=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "input_text", "text": self.prompt},
                            {"type": "input_image", "image_url": f"data:image/{image_type};base64,{base64_str}"}
                        ]
                    }
                ]
            )
            return response.output_text.strip()
        except Exception as e:
            print(f"[ImageSummarizer] Error: {e}")
            return "NA"

    def base64ToMarkdown(self,image_b64, page_number):
        prompt = PromptTemplates.image_summary_prompt()
        try:
                response = self.client.responses.create(
                    model="gpt-4.1",
                    input=[
                        {
                            "role": "user",
                            "content": [
                                {"type": "input_text", "text": (
                                        f"This is page {page_number} of a PDF. Convert it to clean, structured markdown. "
                                        "Use tables when needed. Do not include explanations, comments, or statements "
                                        "about the absence of tables. Just return the markdown content.")},
                                {"type": "input_image", "image_url": f"data:image/png;base64,{image_b64}"}
                            ]
                        }
                    ]
                )
                return response.output_text.strip()
        except Exception as e:
            print(f"[ImageSummarizer] Error: {e}")
            return "NA"