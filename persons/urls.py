from django.urls import path
from persons import views

urlpatterns = [
    path('kebaktian',views.kebaktian_list),
    path('kebaktian/<int:pk>/', views.kebaktian_detail),
    path('kelas',views.kelas_list),
    path('kelas/<int:pk>/', views.kelas_detail),
    path('roles',views.roles_list),
    path('roles/<int:pk>/', views.roles_detail),
    path('users',views.users_list),
    path('users/<int:pk>/', views.users_detail),
    path('login',views.user_login),
    path('logout',views.user_logout),
    #path('user/<int:pk>/', views.users_list_submissions),
]