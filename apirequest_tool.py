from pydantic import BaseModel, Field
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
class JSONParser:
    def __init__(self, data):
        self.data = data

    def extract_info(self):
        # No need to parse 'self.data' as it's already a dictionary.
        return self.data  # or process 'self.data' as needed
        
class APIRequestInput(BaseModel):
    url: str = Field(..., description="The URL to send the request to")
    api_key: str = Field(..., description="The API key for the request")

from superagi.tools.base_tool import BaseTool
from typing import Type, Any

class ErrorHandler:
    def __init__(self):
        pass

    def handle_error(self, error):
        print(f"An error occurred: {error}")

class APIRequestTool(BaseTool):
    """
    API Request Tool
    """
    name: str = "API Request Tool"
    args_schema: Type[BaseModel] = APIRequestInput
    description: str = "Sends an API request and returns the response"

    def _execute(self, args: Any) -> Any:
        api_request = APIRequest(args.url, args.api_key)
        json_parser = JSONParser(api_request.get_data())
        error_handler = ErrorHandler()

        try:
            data = json_parser.extract_info()
            return data
        except Exception as e:
            error_handler.handle_error(e)
            return None  # Or you might want to return some error indication here
