from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission


class Company(models.Model):
    
    id = models.AutoField(primary_key=True) 
    
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100) 
    logo = models.ImageField(upload_to='companies/', null=True, blank=True)
    
    public_code = models.CharField(max_length=6)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    status = models.BooleanField(default=True) 
    
    def __str__(self):
        return self.name

class Service(models.Model) :
    
    id = models.AutoField(primary_key=True) 
    
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
        
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name + " " + self.company.name
    

class Job(models.Model):
    
    id = models.AutoField(primary_key=True) 
    
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name + " " + self.company.name


class User(models.Model):
    
    id = models.AutoField(primary_key=True) 
    
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    
    picture = models.ImageField(upload_to='users/', null=True, blank=True)
        
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    connected_at = models.DateTimeField(auto_now=True)
    
    admin = models.BooleanField(default=False)    
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name + " " + self.first_name + " : " + self.service.company.name
    