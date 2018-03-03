from django import forms
from .models import Video, Comment

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('name', 'description', 'video')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'content')
