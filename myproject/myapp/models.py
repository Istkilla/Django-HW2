from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    adress = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f'name: {self.name}, email: {self.email}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.DecimalField(max_digits=30, decimal_places=3)
    date = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f'name: {self.name}, price: {self.price}, description: {self.description}'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    sum = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f'customer: {self.customer}, product: {self.products}, price: {self.all_price}'
# Create your models here.
