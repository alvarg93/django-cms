from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.

def index(request):
    return render (request, 'index.html')

def test(request, text):
    return HttpResponse(text)

def books(request):
    books = Book.objects.all()
    return render (request, 'books.html', {"books": books})