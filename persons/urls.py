from django.urls import path
from persons import views

urlpatterns = [
    path('users',views.users_list),
    #path('user/<int:pk>/', views.users_list_submissions),
]