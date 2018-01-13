"""courseproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from cinemadatabase import views
from cinemadatabase import views as core_views


urlpatterns = [
    # url(r'^my-view/$', views.my_view),
    # url(r'^second-view/$', views.MyView.as_view()),
    #
    url(r'^login', 
        views.login_view, 
        name="login"),
    
    url(r'^logout/$', 
        views.logout_view, 
        name="logout"),
    
    url(r'^$', 
        views.FilmListView.as_view(),
        name='film_list'),
        
    url(r'^film/(?P<pk>[0-9]+)/$', 
        views.FilmDetailView.as_view(),
        name='film_detail'),
        
    url(r'^actor/(?P<pk>[0-9]+)/$', 
        views.ActorDetailView.as_view(),
        name='actor_detail'),
        
    url(r'^discussion/(?P<pk>[0-9]+)/$', 
        views.DiscussionDetailView.as_view(),
        name='discussion_detail'),
        
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^category/$', views.category),
    url(r'^search/$', views.search),
    url(r'^user/(?P<pk>[0-9]+)/$', 
        views.UserDetailView.as_view(),
        name='user')
]
