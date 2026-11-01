from django.urls import path 
from .views import playlist, playlist_create ,playlist_like


urlpatterns = [
    path("", playlist, name="playlist"),
    path("create/", playlist_create, name= "playlist_create"),
    path("like/", playlist_like, name= "playlist_like"),
]
