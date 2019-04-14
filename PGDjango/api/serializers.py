from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import News, Photo


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'date', 'thumbnail')


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'img', 'thumbnail', 'date')
