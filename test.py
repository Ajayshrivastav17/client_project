from dotenv import load_dotenv
import os

load_dotenv()

print(os.getcwd())
print(os.path.exists(".env"))
print(os.getenv("OPENAI_API_KEY"))