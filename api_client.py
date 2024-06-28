# api_client.py

import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv()
import requests
from auth import get_access_token

class APIClient:
    def __init__(self):
        self.base_url = os.environ.get('BASE_URL')
        self.access_token = get_access_token()

    def get_headers(self):
        headers = {
            'accept': 'application/json, text/plain, */*',
            'Authorization': f'Bearer {self.access_token}'
        }
        return headers

    def make_request(self, method='GET', **kwargs):
        url = f'{self.base_url}'
        headers = self.get_headers()
        response = requests.request(method, url, headers=headers, **kwargs)
        if response.status_code == 200:
            print(response.text)
        else:
            print(f"Error: {response.status_code} - {response.text}")
        return response
