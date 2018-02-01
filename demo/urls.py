from django.conf.urls import url
from demo import views as demoviews

urlpatterns = [
    url(r'^api/musicians/$', demoviews.MusicianListView.as_view()),
    url(r'^api/musicians/(?P<pk>\d+)/$', demoviews.MusicianView.as_view()),
    url(r'^api/albums/$', demoviews.AlbumListView.as_view()),
    url(r'^api/albums/(?P<pk>\d+)/$', demoviews.AlbumView.as_view()),
]
