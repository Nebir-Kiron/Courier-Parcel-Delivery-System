from django.db import models

# Create your models here.

class Marchant(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    email = models.EmailField(max_length=254,null=True)
    create_date = models.DateTimeField( auto_now_add=True,null=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.category
    


class Order(models.Model):
    marchant = models.ForeignKey(Marchant, null=True, on_delete=models.SET_NULL)
    product_category = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL) 
    order_Area = models.CharField(max_length=200, null=True )
    date_created = models.DateTimeField( auto_now_add=True,null=True)
    order_status = models.CharField(max_length=200, null=True )
    order_addres  =  models.CharField(max_length=500, null=True )
    order_quantity = models.FloatField()
    order_price = models.DecimalField(max_digits=10, decimal_places=2)
 