from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import timezone

class News(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='news/thumbnail' ,blank=True, null=True)
    class Meta:
        ordering = ['date']

        def __unicode__(self):
            return  super.title

class Photo(models.Model):
    img = models.ImageField(upload_to='gallery/photos', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='gallery/thumbnail', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['date']





