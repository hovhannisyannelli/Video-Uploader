from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url('/signup', views.SignUp.as_view(), name='signup'),
]