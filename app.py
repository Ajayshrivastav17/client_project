from openai import OpenAI
#Imports the OpenAI class from the openai Python SDK.
# This class is used to communicate with the OpenAI API.

from config import API_KEY
# Imports the API_KEY variable from your config.py file.
# config.py reads the API key from the .env file.

client = OpenAI(api_key=API_KEY)
# Creates an OpenAI client.
# The client manages authentication and sends requests to the API.



response = client.responses.create(
    model="gpt-oss-20b",
    input="Say Hello!"
 )
# responses is the API resource for generating model outputs.
# create() sends a new request to the model.

print(response.output_text)
# The API returns a response object containing lots of information.
