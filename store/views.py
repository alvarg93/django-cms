from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from serializers import UserSerializer, GroupSerializer, BookSerializer
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
    return render (request, 'index.html')

def test(request, text):
    return HttpResponse(text)

def books(request):
    books = Book.objects.all()
    return render (request, 'books.html', {"books": books})