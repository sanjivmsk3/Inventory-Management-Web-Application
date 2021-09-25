from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=200)

    def __str__(self):
        return self.product_name

class Location(models.Model):
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

    def __str__(self):
        return self.city

class ProductMovement(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    from_location = models.ForeignKey(Location, related_name='from_locations', on_delete=models.CASCADE, null=True, blank=True)
    to_location = models.ForeignKey(Location, related_name='to_locations', on_delete=models.CASCADE, null=True, blank=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)

    def __str__(self):
        return self.product_id.product_name