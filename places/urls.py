from django.urls import path
from persons import views

urlpatterns = [
    path('place',views.gereja_list),
    path('place/<int:pk>/', views.gereja_detail),
]