from google import genai
from google.genai import types
import test_config

GEMINI_API_KEY = test_config.GOOGLE_API_KEY
client = genai.Client(
    api_key = GEMINI_API_KEY
)
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="오늘 날씨가 어때?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
    ),
)

print(response.text)