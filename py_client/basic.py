# API = Application Programming Interface
import requests

# endpoint = "https://httpbin.org/"
endpoint = "http://127.0.0.1:8000/api/" #'localhost:8000/api/'

get_response =  requests.post(endpoint, json={"product_id": 123})  # HttpRequest

# print(get_response.text)
# print(get_response.headers)
print(get_response.json()) #to print out the source code as in webscrapping 
# print(get_response.status_code)