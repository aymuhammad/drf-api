# API = Application Programming Interface
import requests

# endpoint = "https://httpbin.org/"
endpoint = "http://127.0.0.1:8000/api/products/" #'localhost:8000/api/'

data = {
     'content' : 'Auwal Yahya', 'title':'Create a new API'
}
   
get_response =  requests.post(endpoint, json=data)
print(get_response.json())
print(get_response.status_code)