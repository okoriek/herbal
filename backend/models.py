from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    product_image = models.FileField(upload_to='product/')
    price = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Product Name: {self.name} ------------- Product Price: {self.price}"