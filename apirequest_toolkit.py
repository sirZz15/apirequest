from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from apirequest_tool import APIRequestTool

class APIRequestToolkit(BaseToolkit):
    name: str = "API Request Toolkit"
    description: str = "Toolkit for processing data, including API requests"

    def get_tools(self) -> List[BaseTool]:
        return [APIRequestTool()]

    def get_env_keys(self) -> List[str]:
        return ["API_KEY"]  # If you have any environment-specific keys, list them here
