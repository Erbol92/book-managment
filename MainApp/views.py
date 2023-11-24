from django.shortcuts import render
from rest_framework import generics
from . import serializers
from .models import Books
# Create your views here.

class BooksList(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = serializers.BooksSerializer


class BooksDetail(generics.RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = serializers.BooksSerializer

class BooksCreate(generics.CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = serializers.BooksSerializer

class BooksUpdate(generics.UpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = serializers.BooksSerializer

class BooksDelete(generics.DestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = serializers.BooksSerializer