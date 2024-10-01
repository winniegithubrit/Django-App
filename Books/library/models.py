from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    
    def __str__(self):
        return self.name
    
class Genre(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    published_date = models.DateField()
    isbn = models.CharField(max_length=255)
    summary = models.TextField()
    cover_image = models.ImageField(upload_to='images/', null=True, blank=True)
    genres = models.ManyToManyField(Genre)
    
    def __str__(self):
        return self.name
    
    
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name='reviews')
    reviewer_name = models.CharField(max_length=255)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Review of {self.book.title} by {self.reviewer_name}'