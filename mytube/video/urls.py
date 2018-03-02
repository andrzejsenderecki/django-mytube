from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^(?P<video_id>\d+)/$', views.video, name='video'),
]