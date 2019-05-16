from django.db import models
import datetime
from django.contrib.auth.models import User
from django.conf import settings


class Video(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    file_name = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='videos/', null=True, verbose_name="")
    title = models.CharField(max_length=200)
    creation_date = models.DateTimeField(default=datetime.datetime.now())
    modified_date = models.DateTimeField(default=datetime.datetime.now())
