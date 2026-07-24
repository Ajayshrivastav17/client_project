from dotenv import load_dotenv
# dotenv is the python package and load_dotenv is the function of loading env file
# without load_dotenv can't read the env file contents.


import os
# os is the module that interact with operating system.


load_dotenv()
# reads entire content in the env file as environmental variables.


print(os.getcwd())
#getcwd stands for Get Current Working Directory.

print(os.path.exists(".env"))
#This checks whether a file named .env exists in the current directory.

print(os.getenv("OPENAI_API_KEY"))
# It looks for a variable named "OPENAI_API_KEY".
