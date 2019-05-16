from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.forms.models import model_to_dict
from django import forms
from .models import Video
from .forms import VideoForm
import json


def index(request):
    video_list = Video.objects.filter(user=request.user).order_by("-creation_date").values('pk', 'title')
    context = {
        'video_list': video_list
    }
    return render(request, 'home.html', context)
def createRecording(request):
    return redirect('uploadVideo')
def updateVideo(request, pk):
    video = Video.objects.get(pk=pk)
    form = VideoForm(request.POST or None, request.FILES or None, instance=video)
    context = {
        'form': form,
        'video_file': video.video_file
    }
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect("/recordings/")
    return render(request, 'updateRecording.html', context)

def uploadVideo(request):
    form = VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        saved_form = form.save(commit=False)
        saved_form.user = request.user
        saved_form.save()
        return HttpResponseRedirect("/recordings/")

    context = {
               'form': form
               }
    return render(request, 'createRecording.html', context)

def deleteVideo(request, pk):
    Video.objects.filter(pk=pk).delete()
    return HttpResponseRedirect("/recordings/")



