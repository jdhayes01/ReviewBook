from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import login as log_in
from django.contrib.auth import authenticate
from django.contrib.auth import logout as log_out
from django.contrib.auth.forms import UserCreationForm
from ReviewBook.forms import SignUpForm

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.user.is_authenticated: #if auth then redirect to dashboard
        return redirect('/dashboard')
    else:
        return redirect('/auth/login') #else send to login page

def signup(request): #signup form request
    if request.method == 'POST': #if form is being submitted
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            log_in(request, user)
            return redirect('/dashboard')
    else: #if not then show form
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def logout(request):
    log_out(request)
    return redirect('/') #return to home page
