from google import genai
from dotenv import load_dotenv
import os
load_dotenv()

client = genai.Client(
    api_key=os.getenv("API_KEY")
)

prompt = """
User activity:
- User A logged in and purchased a laptop worth $1200
- User B logged in but did not make any purchase
- User C purchased a phone worth $800

Return output in JSON format:
{
 "summary":"",
 "total_users":0,
 "purchasing_users":0,
 "total_revenue":0,
 "insights":[]
}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)