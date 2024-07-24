from django.contrib import admin

from vedios.models  import Video
class Videoadmin(admin.ModelAdmin):
    list_display=('title','video_file','uploaded_at')
    
admin.site.register(Video,Videoadmin)
# Register your models here.

# Register your models here.
