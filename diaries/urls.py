import imp
from nturl2path import url2pathname
from urllib.parse import urlparse
from django.urls import URLPattern, path
from .import views

app_name = 'diaries'

urlpatterns = [
    path('', views.top, name = 'top')
]