from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'video_url'
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'video_url': {'allow_null': True}
        }
