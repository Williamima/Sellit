from users.models import User
from users.serializers import UserSerializer
from rest_framework.generics import CreateAPIView
# Create your views here.


class UserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer()
