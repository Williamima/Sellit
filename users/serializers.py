from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message='A user with that username already exists.'
            )
        ],
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message='A account with that email is already existent'
            )
        ]
    )

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data: dict) -> User:
        superuser = validated_data.get('is_superuser')
        if superuser:
            return User.objects.create_superuser(**validated_data)
        else:
            return User.objects.create_user(**validated_data)


class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['is_superuser'] = user.is_superuser

        return token
