from ast import keyword
from rest_framework.authentication import TokenAuthentication as BaseTokenAuth
from rest_framework.authtoken.model import Token

class TokenAuthentication(BaseTokenAuth):
    keyword = "Bearer"