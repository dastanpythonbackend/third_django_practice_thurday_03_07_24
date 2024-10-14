from django.urls import path
from .views import home_page, BookListView, add_book, DetailBookView

urlpatterns = [
    path('', home_page, name='home_page'),
    path('list_books/', BookListView.as_view(), name='list_books'),
    path('add_book/', add_book, name='add_book'),
    path('detail_book/<int:pk>/', DetailBookView.as_view(), name='detail_book'),
]
