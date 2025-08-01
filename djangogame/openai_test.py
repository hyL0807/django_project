from openai import OpenAI
from djangogame import config
client = OpenAI(
    api_key=config.OPENAI_API_KEY
)

response = client.responses.create(
    model="gpt-3.5-turbo",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)