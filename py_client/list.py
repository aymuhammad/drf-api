# API = Application Programming Interface
from lib2to3.pgen2 import token
from wsgiref import headers
import requests
from getpass import getpass

# endpoint = "https://httpbin.org/"
auth_endpoint = "http://127.0.0.1:8000/api/auth/" #'localhost:8000/api/'
username = input("What is your Username?\n")
password= getpass("What is your password?\n")
   
auth_response =  requests.post(auth_endpoint, json={'username': username, 'password': password})
print(auth_response.json())

if auth_response.status_code == 200:
    #token generation
    token = auth_response.json()['token']
    headers ={
        "authorization" : f"Bearer {token}"
    }
    endpoint = 'http://localhost:8000/api/products/'

    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())