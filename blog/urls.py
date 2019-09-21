
from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'), #so when someone requests a page with a /blog/ in the url, the request is fwded to blog/urls.py
    path('<int:blog_id>/', views.detail, name='detail'), #anytime a user requests some blog/(with an integer here), django will save the int as 'blog_id' and will check the views.detail function for what to do
]
