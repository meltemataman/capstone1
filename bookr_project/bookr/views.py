
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
def welcome(request):
    return HttpResponse("<h1>Welcome to Bookr!</h1>")

# Activity 1.02: Kitap arama ekranı (şimdilik sadece arama yazısını gösteriyor)
def book_search(request):
    query = request.GET.get("query", "")
    return render(request, "bookr/search.html", {"query": query})

# Activity 3.01: Book detay sayfası
def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, "bookr/book_detail.html", {"book": book})