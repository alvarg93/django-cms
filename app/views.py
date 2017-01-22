from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from serializers import UserSerializer, GroupSerializer, BookSerializer
from .models import Book, Post


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def index(request):
    posts = Post.objects.all().order_by('-created_at')[:5]
    return render(request, 'index.html', {"posts": posts})

def test(request, text):
    return HttpResponse(text)


# def posts(request):
#     posts = Post.objects.all()
#     return render(request, 'index.html', {"posts": posts})

def post(request, post_id):
    posts = Post.objects.all().filter(id=post_id)
    if not posts:
        return index(request)
    return render(request, 'post.html', {"posts": posts})
