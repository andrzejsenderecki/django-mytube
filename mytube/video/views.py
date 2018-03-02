from django.shortcuts import render
from .models import Video

def video(request, video_id):
    return render(request, 'video/video.html', {'video': Video.objects.get(id=video_id),})
