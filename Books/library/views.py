from django.shortcuts import render, get_object_or_404,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Book
from django.http import JsonResponse
from .forms import BookForm
import json


def home(request):
    return render(request,'home.html',{})

# display all the books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books':books})

# get book by id
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book':book})

# creating a new book
def create_new_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list') 
    else:
        form = BookForm() 

   
    return render(request, 'create_new_book.html', {'form': form})

# Update an existing book
def update_existing_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list') 
    else:  
        form = BookForm(instance=book)  

    return render(request, 'update_existing_book.html', {'form': form})

@csrf_exempt  
def patch_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'PATCH':
        try:
            data = json.loads(request.body)  
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        form = BookForm(data, instance=book)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

from django.shortcuts import get_object_or_404, redirect, render
from .models import Book  # Make sure to import your Book model

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  

    return render(request, 'delete_book.html', {'book': book})
