from django.urls import path
from persons import views

urlpatterns = [
    path('kebaktian',views.kebaktian_list),
    path('kebaktian/<int:pk>/', views.kebaktian_detail),
    path('kelas',views.kelas_list),
    path('kelas/<int:pk>/', views.kelas_detail),
    path('membertypes',views.membertypes_list),
    path('membertype/<int:pk>/', views.membertypes_detail),
    path('members',views.members_list),
    path('member/<int:pk>/', views.members_detail),
    path('userlogin',views.user_login),
    path('userlogout',views.user_logout),
    path('memberlogin',views.member_login),
    #path('memberlogout',views.member_logout),
    #path('user/<int:pk>/', views.users_list_submissions),
]