from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key= True)
    profile_pic = models.ImageField(upload_to='customer_pics')
    address = models.CharField(max_length=150)
    contact_no = models.CharField(max_length=15)
    def __str__(self):
        return f'{self.user.first_name}'
    
    def get_absolute_url(self):
        return reverse('homepage')
    

class PgOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key= True)
    PgOwner_pic = models.ImageField(upload_to='PgOwner_pics')
    NID_pic = models.ImageField(upload_to='PgOwner_NID_pics')
    location = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=15)
    def __str__(self):
        return f'{self.user.first_name}'
    
    def get_absolute_url(self):
        return reverse('homepage')
