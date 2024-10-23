from django.shortcuts import render, redirect
from django.db.models import Max, Min
from books.models import Book

def index_view(request):
    return redirect('all_books')
def all_books_view(request):
    template = 'books/books_list.html'
    data = {'books': Book.objects.all().values(), 'full_list': True}
    return render(request, template, context=data)
def books_view(request, date=''):
    template = 'books/books_list.html'
    if not date:
        queryset = Book.objects.all()
    else:
        queryset = Book.objects.filter(pub_date=date)
    prev_date = Book.objects.filter(pub_date__lt=date).aggregate(Max('pub_date'))['pub_date__max']
    next_date = Book.objects.filter(pub_date__gt=date).aggregate(Min('pub_date'))['pub_date__min']
    data = {'books': queryset.values(), 'full_list': False, 'prev_date': prev_date, 'next_date': next_date}
    return render(request, template, context=data)
