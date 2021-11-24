from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

# Create your models here.


class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    age = models.IntegerField()
    
    def __str__(self):
        return "{}".format(self.user)


STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Gerais'),
    ('RJ', 'Rio de Janerio')
)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100) 
    zip_code = models.CharField(max_length=20)
    state = models.CharField(max_length=100, choices=STATES)
    
    def __str__(self):
        return self.first_name