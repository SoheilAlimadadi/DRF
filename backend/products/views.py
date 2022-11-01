from api.serializers import ProductSerializer
from rest_framework import generics
from .models import Product

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
