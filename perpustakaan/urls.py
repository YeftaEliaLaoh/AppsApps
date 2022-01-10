from django.urls import path
from .views import BooksCreateApi,BooksApi,BooksUpdateApi,BooksDeleteApi
from perpustakaan import views

urlpatterns = [
    path('bookcategories/', views.bookCategory_list),
    path('bookcategory/<int:pk>/', views.bookCategory_detail),
    path('languages/', views.language_list),
    path('language/<int:pk>/', views.language_detail),
    path('publishers/', views.publisher_list),
    path('publisher/<int:pk>/', views.publisher_detail),
    path('books',BooksApi.as_view()),
    path('book/create',BooksCreateApi.as_view()),
    path('book/<int:pk>',BooksUpdateApi.as_view()),
    path('book/delete/<int:pk>',BooksDeleteApi.as_view()),
    path('retrieveall/', views.books_retrieveall),
    path('listsubmissions/<int:pk>/', views.book_listsubmissions),
]