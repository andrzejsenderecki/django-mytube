from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^(?P<video_id>\d+)/$', views.video, name='video'),
    url(r'^all_videos/$', views.all_videos, name='all_video'),
    url(r'^all_videos_user/$', views.all_videos_user, name='all_video_user'),
    url(r'^user_video/(?P<video_id>\d+)/$', views.user_video, name='user_video'),
    url(r'^add_video/$', views.add_video, name='add_video'),
    url(r'^edit_video/(?P<video_id>\d+)/$', views.edit_video, name='edit_video'),
    url(r'^delete_video/(?P<video_id>\d+)/$', views.delete_video, name='delete_video'),
    url(r'^comment/(?P<video_id>\d+)/$', views.new_comment, name='new_comment'),

]