from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('search/', views.book_search, name='book_search'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
]