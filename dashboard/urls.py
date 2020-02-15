from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'), #user dashboard
    path('change_pass/', views.change_pass, name='change_pass'), #change password
    path('add_book/', views.add_book, name='add_book'),#add book
    path('profile/', views.user_profile, name='user_profile'), #user profile
    path('book_profile/<book_title>', views.book_profile, name='book_profile'), #book profile (edit book)
    path('delete_book/<book_title>', views.delete_book, name='delete_book'), #delete book (within book profile)
    path('dwnld_csv', views.dwnld_csv, name='dwnld_csv') #download csv
]