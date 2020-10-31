from django.shortcuts import render, HttpResponse, redirect
from .models import Post

# Create your views here.


def home(request):
    name = "Mahabir Pun"
    return render(request, "home.html", {"name": name})


def about(request):
    return render(request, "about.html")


def contact(request):
    address = "Kathmandu"

    return render(request, "contact.html", {"address": address})


def contactme(request, name):
    address = "Kathmandu"

    return render(request, "contactme.html", {"name": name, "address": address})


def index(request):
    posts = Post.objects.all()  # ORM
    return render(request, "index.html", {"posts": posts})


def createPost(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        newpost = Post.objects.create(title=title, desctiption=description)
        newpost.save()
        return redirect("dashboard")

    return render(request, "create_post.html")


def deletePost(request, post_id):
    Post.objects.get(id=post_id).delete()
    return redirect("dashboard")


def editPost(request, post_id):
    post = Post.objects.get(id=post_id)
    # print(post)
    if(request.method == "POST"):
        post.title = request.POST["title"]
        post.desctiption = request.POST["description"]
        post.save()
        return redirect("dashboard")

    return render(request, "edit_post.html", {"post": post})
