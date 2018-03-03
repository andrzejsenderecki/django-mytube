from django.shortcuts import render
from .models import Video, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.utils import timezone
from .forms import VideoForm, CommentForm

def video(request, video_id):
    return render(request, 'video/video.html', {'video': Video.objects.get(id=video_id),})

def all_videos(request):
    all_video = Video.objects.all()
    return render(request, 'video/all_video.html', {'all_video': all_video},)

@login_required
def all_videos_user(request):
    user_name = User.objects.get(username=request.user)
    all_video_user = Video.objects.filter(author__username=user_name)
    return render(request, 'video/all_video_user.html', {'all_video_user': all_video_user,
                                                         'user_name': user_name},)

@login_required
def user_video(request, video_id):
    user_name = User.objects.get(username=request.user)
    return render(request, 'video/user_video.html', {'user_video': Video.objects.get(id=video_id),
                                                     'user_name': user_name})

@login_required
def add_video(request):
    user_name = User.objects.get(username=request.user)
    if request.method == 'POST':
        video_form = VideoForm(request.POST, request.FILES)
        if video_form.is_valid():
            new_video = video_form.save(commit=False)
            new_video.author = request.user
            new_video.publish = timezone.now()
            new_video.save()
            return HttpResponseRedirect('/dashboard')
    else:
        video_form = VideoForm()
    return render(request, 'video/new_video.html', {'video_form': video_form, 'user_name': user_name})

@login_required
def edit_video(request, video_id):
    user_name = User.objects.get(username=request.user)
    edit_video = Video.objects.get(id=video_id)
    edit_video_form = VideoForm(initial={'name': edit_video.name,
                                         'description': edit_video.description,
                                         'video': edit_video.video,})

    if request.method == 'POST':
        edit_video = Video.objects.get(id=video_id)
        edit_video_form = VideoForm(instance=edit_video, data=request.POST,
                                    files = request.FILES,
                                    initial={'name': edit_video.name,
                                             'description': edit_video.description,
                                             'video': edit_video.video,})
        if edit_video_form.is_valid():
            new_video = edit_video_form.save(commit=False)
            new_video.author = request.user
            new_video.save()
            return HttpResponseRedirect('/dashboard')
        else:
            edit_video_form = VideoForm()

    return render(request, 'video/edit_video.html', {'edit_video_form': edit_video_form,
                                                          'user_name': user_name, 'edit_video': edit_video})

@login_required
def delete_video(request, video_id):
    user_name = User.objects.get(username=request.user)
    delete_video = Video.objects.get(id=video_id).delete()
    return HttpResponseRedirect('/dashboard')

def new_comment(request, video_id):
    video = Video.objects.get(id=video_id)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.published = timezone.now()
            comment.video = video
            comment.save()
            return HttpResponseRedirect('/%s' % video_id)
    else:
        comment_form = CommentForm()
    return render(request, 'video/comment.html', {'comment_form': comment_form})