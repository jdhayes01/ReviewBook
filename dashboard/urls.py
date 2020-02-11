from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('change_pass/', views.change_pass, name='change_pass')
]