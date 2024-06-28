# my_api_package/auth.py

import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv()
import requests

def get_access_token():
    """
    Retrieves an access token from the API's authentication endpoint.
    """
    print(f"AUTH_ENDPOINT: {os.environ.get('AUTH_ENDPOINT')}")
    print(f"CLIENT_ID: {os.environ.get('CLIENT_ID')}")
    print(f"CLIENT_SECRET: {os.environ.get('CLIENT_SECRET')}")

    auth_endpoint = os.environ.get('AUTH_ENDPOINT')
    client_id = os.environ.get('CLIENT_ID')
    client_secret = os.environ.get('CLIENT_SECRET')

    auth_data = {
        'grant_type': 'client_credentials',
        'scope': 'api'
    }

    response = requests.post(auth_endpoint, data=auth_data, auth=(client_id, client_secret))
    if response.status_code == 200:
        access_token = response.json().get('access_token')
        #print(f'Access Token: {access_token}')
        return access_token
    else:
        #print(f'Error: {response.status_code} - {response.text}')
        return access_token

if __name__ == "__main__":
    access_token = get_access_token()
    print(f"Access Token: {access_token}")