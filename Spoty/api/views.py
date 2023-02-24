from django.shortcuts import render
from rest_framework import generics, status
from .serializers import SongSerializer, CreatePlaylistSerializer
from .models import Song, Playlist
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class SongView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class PlaylistView(APIView):
    serializer_class = CreatePlaylistSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(): #not entering here
            song = serializer.data.get('song')
            queryset = Playlist.objects.all()
            queryset = Playlist(song=song)
            queryset.save()
            return Response(SongSerializer(queryset).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)