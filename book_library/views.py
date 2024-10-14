from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .forms import BookForm
from django.contrib import messages

from .models import Book


# Create your views here.

def home_page(request):
    return render(request, 'home_page.html')

class BookListView(ListView):
    model = Book
    template_name = 'list_books.html'
    context_object_name = 'list_books'

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Книга успешно добавлена.')
            return redirect('add_book')
    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})

class DetailBookView(DetailView):
    model = Book
    template_name = 'detail_book.html'
    context_object_name = 'detail_book'
