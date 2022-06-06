import requests

endpoint = "http://127.0.0.1:8000/api/products/update/"

data = {
    'title' : 'Hello World again',
    'price' : 129.89
}

get_response =  requests.put(endpoint, json=data)
print(get_response.json())