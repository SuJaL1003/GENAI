import pandas as pd
from google import genai

from dotenv import load_dotenv
import os
load_dotenv()

client = genai.Client(
    api_key=os.getenv("API_KEY")
)

df = pd.read_csv("data/employees.csv")

prompt = f"""
Generate 5 more employee records similar to this:

{df.to_string(index=False)}

Return only CSV format.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)