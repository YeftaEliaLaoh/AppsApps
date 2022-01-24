from django.urls import path
from places import views

urlpatterns = [
    path('location',views.location_list),
    path('location/<int:pk>/', views.location_detail),
]