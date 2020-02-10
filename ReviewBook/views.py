from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm

def login(request):
    user = request.user
    if user.is_authenticated: #if auth then redirect to dashboard
        return redirect('/dashboard')
    else:
        return redirect('/login') #else send to login page

def signup(request): #signup form request
    if request.method == 'POST': #if form is being submitted
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(user)
            return redirect('/login')
    else: #if not then show form
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logout(request):
    logout(request)
    return redirect('/login')
