from django.db import models      

from .models import UploadImage 
from django import forms  
  
  
class ImageForm(forms.ModelForm):  
    class meta:  
        # To specify the model to be used to create form  
        model=UploadImage 
        # It includes all the fields of model  
        fields = ('caption', 'image')   
    