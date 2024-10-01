from django.urls import path
from . import views
from .views import create_new_book,update_existing_book

urlpatterns = [
    path('', views.home,name='home'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('create_new_book/', create_new_book, name='create_new_book'),
    path('update_existing_book/<int:pk>/', update_existing_book, name='update_existing_book')
]
