from django.db import models

# Create your models here.
class RestaurantModel(models.Model):
    name=models.CharField(max_length=50)
    valuation=models.CharField(max_length=30)
    address=models.TextField()
    def __str__(self):
        return self.name