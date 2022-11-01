from pyexpat import model
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by('?').first()
    if model_data:
        data = ProductSerializer(model_data).data
    return Response(data)
