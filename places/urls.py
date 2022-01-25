from django.urls import path
from places import views

urlpatterns = [
    path('locations',views.location_list),
    path('location/<str:pk>/', views.location_detail),
]