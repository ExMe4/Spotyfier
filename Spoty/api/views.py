from django.shortcuts import render
from rest_framework import generics
from .serializers import SongSerializer
from .models import Song

# Create your views here.

class SongView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer