from rest_framework import serializers
from rest_framework.reverse import reverse
from api.serializers import UserPublicSerializer
from .validators import validate_title_no_hello, unique_product_title
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    my_user_data = serializers.SerializerMethodField(read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
        )
    title = serializers.CharField(validators=[validate_title_no_hello, 
    unique_product_title])
    # email = serializers.EmailField(write_only=True)
    class Meta:
        model = Product
        fields = [
            'user',
            'url',
            'edit_url',
            'pk',
            'title', 
            'content', 
            'price', 
            'sales_price', 
            'my_discount',
            'get_my_user_data'
        ]

    ''' 
        create a custom validation method to validate an object field e.g. 'title'.
        this can be here or in a custom validation.py file.
    '''
    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__exact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name.
    #         ")
    #     return value

    def get_my_user_data(self, obj):
        return {
            "username": obj.user.username
        }

    def create(self, validated_data):
        # return Product.objects.create(**validated_data)
        # email = validated_data.pop('email')
        obj = super().create(validated_data)
        return obj

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title')
    #     return instance

    def get_edit_url(self, obj):
        request = self.context.get('request')

        if request is None:
            return None        
        return reverse("product-edit", kwargs={"pk": obj.pk},
        request=request)
        
        # return f"/api/products/{obj.pk}/"
    def get_my_discount(self, obj):
        return obj.get_discount()