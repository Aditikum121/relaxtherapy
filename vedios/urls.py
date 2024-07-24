# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     # Your URL patterns
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from .views1 import upload_video
from .views1 import video_list

urlpatterns = [
    path('upload/', upload_video, name='upload_video'),
    # Add other URLs such as the video list view
    path('list/', video_list, name='video_list'),
]