import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

LLMWHISPERER_API_KEY = os.getenv('LLMWHISPERER_API_KEY')

def extract_text_from_pdf(pdf_path):
    url = "https://llmwhisperer-api.unstract.com/v1/whisper"
    headers = {
        'unstract-key': LLMWHISPERER_API_KEY,
        'Content-Type': 'application/octet-stream'
    }
    params = {
        'force_text_processing': 'true',
        'processing_mode': 'ocr',
        'output_mode': 'line-printer',
        'pages_to_extract': 'all'  # Process all pages
    }

    with open(pdf_path, 'rb') as pdf_file:
        response = requests.post(url, headers=headers, params=params, data=pdf_file)

    if response.status_code == 200:
        return response.text
    else:
        print(f"Error: {response.status_code}")
        print(response.json())
        print(response.text)

if __name__ == "__main__":
    pdf_path = "/Users/davidhorvath/Desktop/unstract_env/Opposition to Renewable Energy Facilities in the United States_ M.pdf"
    result = extract_text_from_pdf(pdf_path)
    if result:
        print(result)
