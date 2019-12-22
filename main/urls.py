"""bookbidding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:section>/<int:index>/', views.site_article, name='site-article'),
    path('events/', views.default_events, name='default-events-list'),
    path('<group_name>/events/', views.events_list, name='events-list'),
    path('<group_name>/info/', views.info, name='info'),
    path('<group_name>/schedule/', views.schedule, name='schedule'),
    path('event/<int:event_id>/', views.event, name='event'),
    #path('addpost/', views.AddPostView.as_view(), name='add-post'),
]
