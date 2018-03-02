from django.db import models

class Video(models.Model):
    name = models.CharField(max_length=150)
    video = models.FileField(upload_to='static/')

    def __str__(self):
        return self.name