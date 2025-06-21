from django.db import models

# Create your models here.
class Snake(models.Model):
    name = models.CharField(max_length = 255)
    price = models.FloatField()
    color = models.CharField(max_length = 10)
    image = models.CharField(max_length = 2083)

class Bin(models.Model):
    name = models.CharField(max_length =255)
    price = models.FloatField()
    shape = models.CharField(max_length = 20)
    image = models.CharField(max_length = 2083)