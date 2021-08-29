from django.http import HttpRequest, HttpResponse
from book.models import Book
from django.shortcuts import render


def Mainpage(request: HttpRequest):
    main = Book.objects.all()
    return render(request, "book/mainpage.html", {"books": main,},)