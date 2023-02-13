from django.urls import path
from .views import SongView

urlpatterns = [
    path('song', SongView.as_view())
]