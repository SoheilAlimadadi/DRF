from rest_framework import serializers
from products.models import Product
from rest_framework.reverse import reverse
from .validators import validate_title

class ProductSerializer(serializers.ModelSerializer):
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name= "product-detail",
        lookup_field = 'pk'
    )
    delete_url = serializers.HyperlinkedIdentityField(
        view_name= "product-destroy",
        lookup_field = "pk"
    )
    title = serializers.CharField(validators=[validate_title])
    class Meta:
        model = Product
        fields = [
            'url',
            'edit_url',
            'delete_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
        ]
        
    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)
    
