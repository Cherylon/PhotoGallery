from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import timezone

class News(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(blank=True, null=True)
<<<<<<< HEAD
    date = models.DateField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='news/thumbnail' ,blank=True, null=True)
=======
    date = models.DateField(auto_now=True)
    thumbnail = models.ImageField(blank=True, null=True)
>>>>>>> 52b8b7717a60d386ba9d447c27c0917cd501814a
    class Meta:
        ordering = ['date']

        def __unicode__(self):
            return  super.title

<<<<<<< HEAD
        def __str__(self):
            return super.title

class Photo(models.Model):
    img = models.ImageField(upload_to='gallery/photos', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='gallery/thumbnail', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    news_id = models.ForeignKey(News, on_delete=models.CASCADE, blank=True, null=True,)
=======
class Photos(models.Model):
    img = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)
>>>>>>> 52b8b7717a60d386ba9d447c27c0917cd501814a
    class Meta:
        ordering = ['date']





<<<<<<< HEAD

=======
>>>>>>> 52b8b7717a60d386ba9d447c27c0917cd501814a
