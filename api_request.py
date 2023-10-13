import requests

class APIRequest:
    def __init__(self, url, api_key):
        self.url = url
        self.headers = {
            'Api-Key': api_key  # This is the header key for the API key, as indicated in your Postman collection.
        }

    def get_data(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
