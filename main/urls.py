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
    path('profile/', views.profile, name='profile'),
    # articles
    path('blog/', views.articles_list, name='blog'),
    path('artcle/blog/<int:article_id>/', views.blog_article, name='blog-article'),
    path('article/<int:section>/<int:index>/', views.site_article, name='site-article'),
    path('addarticle/', views.AddArticleView.as_view(), name='add-article'),
    # invents
    path('events/', views.default_events, name='default-events'),
    path('events/<group_name>/', views.group_events, name='group-events'),
    path('event/<int:event_id>/', views.event, name='event'),
    # class page
    path('<class_id>/info/', views.info, name='info'),
    path('<class-id>/schedule/', views.schedule, name='schedule'),
    
    #path('addpost/', views.AddPostView.as_view(), name='add-post'),

    # privacy policy
    path('privacypolicy/', views.privacypolicy, name='privacy-policy'),
]
