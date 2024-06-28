# main.py

from api_client import APIClient

def main():
    # Create an instance of the APIClient class
    api_client = APIClient()

    # Call the make_request method with the desired parameters
    response = api_client.make_request(method='GET')

    # Handle the response
    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    main()
