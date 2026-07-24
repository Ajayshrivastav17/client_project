from dotenv import load_dotenv
# dotenv is the python package and load_dotenv is the function of loading env file
# without load_dotenv can't read the env file contents.


import os
# os is the module that interact with operating system.



load_dotenv()
# reads entire content in the env file as environmental variables.

API_KEY = os.getenv("OPENAI_API_KEY")
#os.getenv means get the environments variables.
#os.getenv is exactly keep the secreat imformation from the source code.

print(API_KEY)
#It will print the values stored in the variables.




