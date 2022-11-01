from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    #model_data = Product.objects.all().order_by('?').first()
    serializer = ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(request.data)
