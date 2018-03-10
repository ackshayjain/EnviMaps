from django.conf.urls import include, url
from . import views



urlpatterns = [
    
    url(r'^$',views.index,name='index'),
    url(r'^thanks/$',views.thanks,name='thanks'),
    # url(r'^movies/(?i)(?P<movie_id>[0-9]+)/$', views.get_movie, name = 'get_movie'),
    # url(r'^movies/(?i)(?P<movie_id>[0-9]+)/rate/$', views.get_rating, name = 'get_rating'),
]
