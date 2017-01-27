from django.conf.urls import url
from . import views
#from django.contrib import admin

urlpatterns = [
    url(r'^$', views.login_page, name ='login_page'),
    url(r'^register/$', views.register, name ='register'),
    url(r'^login/$', views.login, name ='login'),
]
