from django.contrib import admin
from service.models  import Service
class Serviceadmin(admin.ModelAdmin):
    list_display=('Service_icon','Service_tittle','Service_des')
    
admin.site.register(Service,Serviceadmin)
# Register your models here.
