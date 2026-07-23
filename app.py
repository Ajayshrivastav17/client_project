from openai import OpenAI
from config import API_KEY

client = OpenAI(api_key=API_KEY)

response = client.responses.create(
    model="gpt-5.5",
    input="Say Hello!"
)

print(response.output_text)
