from django.http import JsonResponse,HttpResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request,*args,**kwargs):
    
    '''
    DRF API view 
    '''
    # if request.method!="POST":
    #     return Response({"msg":"get is not allowd"},status=405)
    # instance = Product.objects.all().order_by('?').first()
    # data = request.data
    # if instance:
    #     # data = model_to_dict(model_data, fields=['id', 'title','price','sale_price'])
    #     data=ProductSerializer(instance).data
    seri= ProductSerializer(data=request.data)
    if seri.is_valid(raise_exception=True):
        # instance=seri.save()
        # print(instance)
        data=seri.data
        print(data)
        return Response(seri.data)
    return Response({"msg":"not good data"})
  