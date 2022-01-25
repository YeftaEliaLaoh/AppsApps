from django.urls import path
from administrasi import views

urlpatterns = [
    path('otp',views.otp_list),
    #path('otp/<int:pk>/', views.otp_detail),
]