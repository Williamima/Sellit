import uuid
from django.db import models
# Create your models here.


class UserProduct(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    users = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        null=False,
        related_name='users_products'
    )

    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        null=False,
        related_name='users_products'
    )
