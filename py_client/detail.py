# API = Application Programming Interface
import requests

# endpoint = "https://httpbin.org/"
endpoint = "http://127.0.0.1:8000/api/products/10/" #'localhost:8000/api/'

get_response =  requests.get(endpoint)
print(get_response.json())
print(get_response.status_code)