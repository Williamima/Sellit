from django.urls import path
from users_products.views import UserProductView

urlpatterns = [
    path('products/<str:product_id>/users/', UserProductView.as_view()),
]
