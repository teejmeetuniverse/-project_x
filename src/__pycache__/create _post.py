# 2/2/2024


# tjmeetuniverse

# importing my libraries

import requests
from login import authenticate_with_twitter

# bearer_token = "MY_BEARER _TOKEN"

def authenticate_with_twitter(bearer_token):
   
   url = https://api.twitter.com/2/tweets

   data = {'text': "MY FIRST POST TO TWITTER :)"}

   headers = {      
      'Authorization': 'bearer' + bearer_token
   }
   response = requests.post(
      url,
      data=data,
      headers=headers,
   )
   
   if response.status_code == 200:
      print(response.status_code)

   elif response.status_code == 400:
      print(response.status_code)

      response_data = response.json()
      print(response_data)
   






