from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User

def sign_up(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'регистрация успешна, на почту выслано сообщение')
        return redirect('/')
    return render(request, 'AuthApp/register.html', { 'form': form})




class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

