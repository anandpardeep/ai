from image_summarizer import ImageSummarizer
from dotenv import load_dotenv
from openai import OpenAI
import openai
from  extractor import Extractor
from content_elements import *
from extractor import *

filename = "CrowdStrikeGlobalThreatReport2025.pdf" 
def main():
    load_dotenv()

    openai_api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = openai_api_key
    client = OpenAI(api_key=openai_api_key)
    summarizer = ImageSummarizer(client)
    extractor = PDFExtractor(filename, "spatial_images",summarizer) 
    
    print("Custom extraction.")
    extractor.pages_to_markdown("crowdstrike_spatial.md")
    
    #print("Standard extraction.")
    #extractor.save_markdown("crowdstrike_standard.md", use_spatial=False)
   
    print("Done")
    
if __name__ == "__main__":
    main()   
