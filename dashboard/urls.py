from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('change_pass/', views.change_pass, name='change_pass'),
    path('add_book/', views.add_book, name='add_book'),
    path('profile/', views.user_profile, name='user_profile')
]