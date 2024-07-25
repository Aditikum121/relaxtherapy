from django.db import models


class UploadImage(models.Model):
    caption = models.CharField(max_length=200)  
    image = models.FileField(upload_to='images') 
    def __str__(self):  
        return self.caption
# Create your models here.
