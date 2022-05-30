import json #used to convert data to json
from django.forms.models import model_to_dict # to convert data to dictionary it give chance to specify the exact field the API to respond
#JsonResponse accept a dictionary while HttpResponse accept string
from django.http import JsonResponse, HttpResponse
from products.models import Product
from products.serializers import ProductSerializers

#rest-api 
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data['id'] = instance.id
        # data['title'] = instance.title
        # data['content'] = instance.content
        # data['price'] = instance.price
        # data = model_to_dict(instance, fields=['id', 'price', 'title'])
        data = ProductSerializers(instance).data
    return Response(data)