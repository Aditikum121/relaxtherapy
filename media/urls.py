from django.urls import path  
from studybud1.views import image_request  
  
app_name = 'sampleapp'  
urlpatterns = [  
    path(' ', image_request, name = "image-request"), 
]