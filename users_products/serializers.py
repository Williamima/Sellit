from rest_framework import serializers
from users_products.models import UserProduct


class UserProductSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source='user.id', read_only=True)
    user_username = serializers.CharField(
        read_only=True,
        source='user.username'
    )
    user_email = serializers.CharField(
        source='user.email'
    )

    class Meta:
        model: UserProduct
        fields = [
            'id',
            'user_id',
            'user_username',
            'user_email'
        ]
        read_only_fields = [
            'id',
            'status'
        ]
