import json #used to convert data to json
from django.forms.models import model_to_dict # to convert data to dictionary it give chance to specify the exact field the API to respond

#JsonResponse accept a dictionary while HttpResponse accept string
from django.http import JsonResponse, HttpResponse
from products.models import Product
from products.serializers import ProductSerializer

#rest-api 
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        print(instance)
        return Response(instance)