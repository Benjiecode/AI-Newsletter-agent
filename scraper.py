import requests
from bs4 import BeautifulSoup
import os
import dotenv
import google.generativeai as genai

#get environment variables from .env file
dotenv.load_dotenv()
api_key = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

#load in the location we're sendiong the email from:
email_user = os.getenv("EMAIL_ADDRESS")
email_pass = os.getenv("EMAIL_PASSWORD")

#making api calls:
model = genai.GenerativeModel("gemini-1.5-flash") #uses Generativemodel class from the genai module to make calls to a specific model
chat = model.start_chat()

# Loop for feeding info to AI
while True:
    user_input = input("You: ")
    response = chat.send_message(user_input)
    print("Gemini:", response.text)

    response = chat.send_message("Turn this request into a list of 5 keywords that would help me find news articles online.")
    print("Keywords:", response.text)

    #Get AI to summarise what it just found into some keywords, and find sources like websites etc...
    
    #response.text
    '''
    What i need to do is now, Look for a way to parse this through and rather than printing a bunch of information to the user. I wan the AI to create keywords, and store these + websites into a list/dict.
    '''
    if user_input.lower() in {"exit", "quit"}:
        break
