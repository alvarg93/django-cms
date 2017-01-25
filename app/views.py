from django.contrib.auth.models import User, Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from serializers import UserSerializer, GroupSerializer, PostSerializer
from .models import Post, Author


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer


def getAuthors(post):
    return post.author

def index(request):
    posts = Post.objects.all().filter(is_published=True).order_by('-created_at')[:5]
    authors = Author.objects.all().order_by('-created_at')[:4]
    return render(request, 'index.html', {"posts": posts, "authors": authors})


def test(request, text):
    return HttpResponse(text)


def posts(request):
    posts = Post.objects.all().filter(is_published=True).order_by('-created_at')
    paginator = Paginator(posts, 10)  # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    return render(request, 'posts.html', {"posts": posts})


def post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        return render(request, 'post.html', {"post": post})
    except Post.DoesNotExist:
        return index(request)
