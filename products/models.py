import uuid
from django.db import models

# Create your models here.


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    video_url = models.TextField(null=True)

    owner = models.ManyToManyField(
        'users.User',
        through='users_products.UserProduct',
        related_name='my_products'
    )
