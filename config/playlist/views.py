from django.shortcuts import render, redirect
from .models import Video
# Create your views here.

def playlist_create (request):
    if request.method == "POST":
        title = request.POST.get("title")
        link = request.POST.get("link")
        Video.objects.create(title = title, embed_code = link)
        return redirect()


    return render (request, "playlist_create.html")


    
def playlist (request):
    videos = Video.objects.all()
    return render (request, "playlist.html", {"videos": videos})

def playlist_like (request):
    if request.method == "POST":
        video_id = request.POST.get("video_id")
        key = f"liked_{video_id}"

        if not request.session.get(key):
            video = Video.objects.get(id = video_id) 
            video.like += 1
            video.save()
            request.session[key] = True
        else:
            video = Video.objects.get(id = video_id) 
            video.like -= 1
            video.save()
            request.session[key] = False


    return redirect("playlist")