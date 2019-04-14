from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import NewsSerializer, PhotoSerializer
from .models import News, Photo


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-date')
    serializer_class = NewsSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all().order_by('-date')
    serializer_class = PhotoSerializer