from django.shortcuts import render
from  .models import Post 
def blog(request):
    posts = Post.objects.all()
    return render(request, "post_list.html", {"posts": posts})
