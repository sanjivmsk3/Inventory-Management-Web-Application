from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=400)

    def __str__(self):
        return self.product_name

class WLocat(models.Model):
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.city

class ProductMovement(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    from_location = models.ForeignKey(WLocat, related_name='from_locations', null=True, blank=True, on_delete=models.CASCADE)
    to_location = models.ForeignKey(WLocat, related_name='to_locations', null=True, blank=True, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)

    def __str__(self):
        return self.product_id.product_name