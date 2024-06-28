from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.generics import CreateAPIView
# Create your views here.


class UserView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer()
