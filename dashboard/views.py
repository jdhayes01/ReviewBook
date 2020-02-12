from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dashboard.models import Book
from dashboard.forms import BookForm

@login_required
def dashboard(request):
    user = request.user
    return render(request, 'dashboard.html', {
        'name':user
        })

def change_pass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })

def add_book(request):
	form = BookForm()
	return render(request, 'add_book.html', {
        'form': form
    })

def user_profile(request):
    user = request.user
    return render(request, 'user_profile.html', {
        'name':user
        })
