from django.db import models

class Service(models.Model):
    Service_icon=models.CharField(max_length=50)
    Service_tittle=models.CharField(max_length=50)
    Service_des= models.TextField()

# Create your models here.
