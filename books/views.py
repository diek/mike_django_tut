# from django.shortcuts import render
from django.http import HttpResponse
from books.models import Books
from django.template import Context, loader


def index(request):
    book_list = Books.objects.all()
    book_load = loader.get_template('books/index.html')
    book_context = Context({'book_list': book_list})
    return HttpResponse(book_load.render(book_context))
