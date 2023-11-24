from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('books/', views.BooksList.as_view()),
    path('books/<int:pk>/', views.BooksDetail.as_view()),
    path('books/create', views.BooksCreate.as_view()),
    path('books/update/<int:pk>/', views.BooksUpdate.as_view()),
    path('books/delete/<int:pk>/', views.BooksDelete.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)