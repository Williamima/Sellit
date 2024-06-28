from users.models import User
from users.serializers import UserSerializer, CustomJWTSerializer
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.


class UserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer()


class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer
