
from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
     #so when someone requests a page with a /blog/ in the url, the request is fwded to blog/urls.py
]
