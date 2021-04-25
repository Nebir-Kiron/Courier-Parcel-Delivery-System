from django.db import models

# Create your models here.

class Marchant(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    email = models.EmailField(max_length=254,null=True)
    create_date = models.DateTimeField( auto_now_add=False,null=True)


