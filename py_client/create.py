# API = Application Programming Interface
from email import header
from wsgiref import headers
import requests

# endpoint = "https://httpbin.org/"

headers={'Authorization': 'Bearer1476d992007f17d7b18bd34573f96d098cdc65a5'}
endpoint = "http://127.0.0.1:8000/api/products/" #'localhost:8000/api/'

data = {
     'content' : 'this is a new content', 'title':'Create a new API', 'price':78.99,
}
   
get_response =  requests.post(endpoint, json=data, headers=headers)
print(get_response.json())
print(get_response.status_code)