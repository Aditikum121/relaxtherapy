from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import VideoUploadForm
from .forms import Video



def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.uploaded_by = request.user
            video.save()
            return redirect('video_list')  # Redirect to a view that lists all videos
    else:
        form = VideoUploadForm()
    return render(request, 'tempelates/upload_vedio.html', {'form': form})

# Create your views here.
def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})
