from django.urls import path 
from .views import magic_number

urlpatterns = [
    path("", magic_number)
    
]
