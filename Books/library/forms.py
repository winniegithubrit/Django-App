from django import forms
from .models import Book,Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','publisher','published_date','isbn','summary','cover_image']
        
        
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio','profile_picture']