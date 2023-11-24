from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('register/', views.sign_up, name='register'),
    path('user/create', views.UserCreate.as_view()),
]
