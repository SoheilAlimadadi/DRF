from rest_framework import serializers
from products.models import Product
from rest_framework.reverse import reverse
from .validators import unique_product_title

class UserOtherProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name =  'product-detail',
        lookup_field = 'pk',
        read_only = True
    )
    title = serializers.CharField(read_only=True)

class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.CharField(read_only=True)
    other_product = serializers.SerializerMethodField(read_only=True)
    
    def get_other_product(self, obj):
        user = obj
        my_product_qs = user.product_set.all()[:5]
        return UserOtherProductInlineSerializer(my_product_qs, context=self.context, many=True).data
    
class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name= "product-detail",
        lookup_field = 'pk'
    )
    delete_url = serializers.HyperlinkedIdentityField(
        view_name= "product-destroy",
        lookup_field = "pk"
    )
    title = serializers.CharField(validators=[unique_product_title])
    class Meta:
        model = Product
        fields = [
            'owner',
            'url',
            'edit_url',
            'delete_url',
            'pk',
            #'user',
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
    
