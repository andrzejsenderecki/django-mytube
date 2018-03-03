from django.db import models
from django.utils import timezone
from django.conf import settings

class Video(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    publish = models.DateTimeField(default=timezone.now)
    video = models.FileField(upload_to='static/')

    def __str__(self):
        return self.name

class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name