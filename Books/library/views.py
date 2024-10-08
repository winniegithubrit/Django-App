from django.shortcuts import render, get_object_or_404,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Book,Author
from django.http import JsonResponse
from .forms import BookForm,AuthorForm
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



def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  

    return render(request, 'delete_book.html', {'book': book})

# VIEWS FOR AUTHORS

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})


def get_authors(request, id):
    author = get_object_or_404(Author, id=id)
    return render(request, 'get_authors.html', {'author': author})


def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('author_list')  
    else:
        form = AuthorForm()

    return render(request, 'create_author.html', {'form': form})

def delete_author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
    return render(request,'delete_author.html', {'author': author})