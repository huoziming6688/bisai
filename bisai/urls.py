"""bisai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
import xadmin
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.views.generic import TemplateView
from users.views import RegisterView, ActiveUserView, LoginView, LogoutView, Show
from subdistricts.views import xiaoquview
from django.views.static import serve
from bisai.settings import MEDIA_ROOT
from operations.views import *
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    re_path('^$', TemplateView.as_view(template_name='index.html'), name='index'),
    re_path('^register/$', RegisterView.as_view(), name='register'),
    re_path('^login/$', LoginView.as_view(), name='login'),
    re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(), name="user_active"),
    re_path('^map/$', TemplateView.as_view(template_name='home-map.html'), name='map'),
    re_path('^rent/$',showrent, name='rent'),
    re_path('^renthandle/$',getinfo,name='renthandle'),
    re_path('^agency-list.html/$', xiaoquview.as_view(), name='xiaoqu'),
    re_path('^infor/$', TemplateView.as_view(template_name='user-profile.html'), name='infor'),
    re_path('^shoucang/$', TemplateView.as_view(template_name='favourite-properties.html'), name='shoucang'),
    re_path('^help/$', TemplateView.as_view(template_name='page-contact.html'), name='help'),
    re_path('logout/$', LogoutView.as_view(), name='logout'),
    re_path('edit/$', Show.as_view(), name='edit'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    # re_path(r'^image/upload/$', UploadImageView.as_view(), name="image_upload"),
    # re_path('upload/$', UserImageView.as_view(), name='upload'),
]
