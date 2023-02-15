from django.urls import path
from .views import SongView, PlaylistView

urlpatterns = [
    path('song', SongView.as_view()),
    path('playlist', PlaylistView.as_view())
]