from django.db import models

VERSION = (
    ('3', '3'),
    ('2', '2'),
    ('1', '1')
)

class Products(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(blank=True)
    description = models.TextField(blank=True)
    ami = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    version = models.CharField(choices=VERSION, max_length=20, default='1')