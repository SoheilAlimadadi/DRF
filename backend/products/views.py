from api.serializers import ProductSerializer
from rest_framework import generics, permissions, authentication
from .models import Product
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .permissions import IsStaffPermissions

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, IsStaffPermissions] 

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, IsStaffPermissions]
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)
        print(serializer.data)

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser, IsStaffPermissions]
    
    def perform_update(self, serializer):
        return super().perform_update(serializer)
    
class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser, IsStaffPermissions]
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    
    

@api_view(['GET' , 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    if request.method == 'GET':
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj).data
            return Response(data)
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)

