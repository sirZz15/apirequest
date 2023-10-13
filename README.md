The main classes, functions, and methods used in this task are:

Classes:
1. `APIRequest`: This class is responsible for making the API request and getting the JSON data.
2. `JSONParser`: This class is responsible for parsing the JSON data and extracting the required information.
3. `ErrorHandler`: This class is responsible for handling any errors or exceptions that may occur during the API request or JSON parsing.

Functions:
1. `main`: This function is the entry point of the program. It creates instances of the `APIRequest`, `JSONParser`, and `ErrorHandler` classes, and coordinates their interactions.

Methods:
1. `APIRequest.__init__(self, url)`: This method initializes the API endpoint URL.
2. `APIRequest.get_data(self)`: This method makes the API request and returns the JSON data.
3. `JSONParser.__init__(self, data)`: This method initializes the JSON data.
4. `JSONParser.extract_info(self)`: This method parses the JSON data and extracts the required information.
5. `ErrorHandler.__init__(self)`: This method initializes the ErrorHandler class.
6. `ErrorHandler.handle_error(self, error)`: This method handles any given error or exception.

Now, let's write the Python code for these classes and functions.

requirements.txt
