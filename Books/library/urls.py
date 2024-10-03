from django.urls import path
from . import views
from .views import create_new_book,update_existing_book,patch_book,delete_book,author_list,get_authors,create_author

urlpatterns = [
    path('', views.home,name='home'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('create_new_book/', create_new_book, name='create_new_book'),
    path('update_existing_book/<int:pk>/', update_existing_book, name='update_existing_book'),
    path('patch_book/<int:pk>/', patch_book, name='patch_book'),
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),
    path('author_list/', author_list, name='author_list'),
    path('get_authors/<int:id>/',get_authors, name='get_authors'),
    path('create_author/', create_author, name='create_author'),
    
    
   
]
