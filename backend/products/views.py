from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

# post methode
class ProductCreateAPIView(generics.CreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    def perform_create(self,serializer):
        # here we change data and save it in database
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content=title
            serializer.save(content=content)


Product_create_view=ProductCreateAPIView.as_view()


# get methode
class ProductDetailsAPIView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # lookup_field ='pk


Product_detail_view=ProductDetailsAPIView.as_view()

# list api gives all user data but there is another methode we can use that because it has slight change in create API
class ProductListAPIView(generics.ListAPIView):
    '''

    '''
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # lookup_field ='pk


Product_list_view=ProductListAPIView.as_view()


# list all data in create api function 
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    def perform_create(self,serializer):
        # here we change data and save it in database
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content=title
            serializer.save(content=content)


Product_listcreate_view=ProductListCreateAPIView.as_view()



class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field ='pk'

    def perform_update(obj,serializer):
        instance=serializer.save()
        if not instance.content:
            instance.content=instance.title
            # 
Product_update_view=ProductUpdateAPIView.as_view()

class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field ='pk'

    def perform_destroy(obj,instance):
        super().perform_destroy(instance)
Product_destroy_view=ProductDestroyAPIView.as_view()
