from pypdf import PdfReader
from google import genai

from dotenv import load_dotenv
import os
load_dotenv()

client = genai.Client(
    api_key=os.getenv("API_KEY")
)


reader = PdfReader("data/sample.pdf")

text = ""

for page in reader.pages:
    text += page.extract_text()

prompt = f"""
PDF Content:
{text}

Question:
Summarize this PDF.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)