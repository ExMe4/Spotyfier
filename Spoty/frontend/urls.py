from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('selectsongs', index),
    path('playlistcreated', index)
]
