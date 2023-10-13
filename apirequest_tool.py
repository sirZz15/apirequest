from pydantic import BaseModel, Field

class APIRequestInput(BaseModel):
    url: str = Field(..., description="The URL to send the request to")
    api_key: str = Field(..., description="The API key for the request")

from superagi.tools.base_tool import BaseTool
from typing import Type, Any
from api_request import APIRequest
from json_parser import JSONParser
from error_handler import ErrorHandler

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
