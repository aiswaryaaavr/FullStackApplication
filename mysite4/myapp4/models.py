from django.db import models

# Create your models here.to create variables 
from django.db import models 
# why twice,wht parameter?

class Register(models.Model): 

    Fname = models.CharField(max_length=100)
    Lname = models.CharField(max_length=100)
    Phone = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
