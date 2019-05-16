from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createRecording', views.createRecording, name='createRecording'),
    path('uploadVideo', views.uploadVideo, name='uploadVideo'),
    path('updateVideo/<pk>/', views.updateVideo, name='updateVideo'),
    path('deleteVideo/<pk>/', views.deleteVideo, name='deleteVideo'),
]