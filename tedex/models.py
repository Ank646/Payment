from django.db import models

# Create your models here.
class ticket(models.Model):
    nme=models.CharField(max_length=25)
    phone=models.CharField(max_length=10)
    college=models.CharField(max_length=250)
    email=models.CharField(max_length=30)
    no=models.CharField(max_length=10)
    oid=models.CharField(max_length=100)
    dt=models.DateTimeField(auto_now_add=True)
   
   