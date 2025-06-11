import requests
from bs4 import BeautifulSoup
import os
import dotenv
import google.generativeai as genai
import json

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
    if user_input.lower() in {"exit", "quit"}:
        print("Goodbye!!!")
        break
    response = chat.send_message(user_input)
    #print("Gemini:", response.text)

    response = chat.send_message("Return this request ONLY in JSON format with fields for 'keywords', 'search_terms', and 'websites' only.") #Findings are put into JSON format so that it can be parsed into variables that can be easily re-used in my code
    '''
    ``` in my JSON outputted text is blocking my json.loads() function so... We find all text before and after the {}
    '''
    gemini_response = response.text
    start = gemini_response.find('{')
    end = gemini_response.rfind('}') + 1
    clean_json = gemini_response[start:end]
    Scraper_data = json.loads(clean_json)
    print("Here's what I found!!!\n", Scraper_data)
    
    #for key in Scraper_data: #enter json into my pythopn dictionary...

    '''
    What i need to do is now, Look for a way to parse this through and rather than printing a bunch of information to the user. I wan the AI to create keywords, and store these + websites into a list/dict.
    '''
    

