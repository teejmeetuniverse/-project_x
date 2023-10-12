# 8/29/2023

# teejmeetuniverse

#get authentication credentials

import requests
"""
"api_key": "MY API KEY"
"api_secret_key": "MY API SECRET KEY"
"return_var": "MY BEARER TOKEN"
"""
# log into twitter
def authenticate_with_twitter(username, password):

    return_var = False
    session = requests.Session()
    session.auth = (username, password)
    session.verify = False
    # example request URL
    auth_url = "https://api.twitter.com/oauth2/token?grant_type=client_credentials"

    # send post to twitter to get bearer token    
    response = session.post(auth_url)
    # checking the response "(debug)"
    ## print(response)
    if response.ok is True:
        response_json = response.json()
        return_var = response_json['access_token']

    return return_var