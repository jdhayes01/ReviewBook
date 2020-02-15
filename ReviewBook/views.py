from django.shortcuts import render, redirect
from django.contrib.auth import login as log_in
from django.contrib.auth import authenticate
from django.contrib.auth import logout as log_out
from django.contrib.auth.forms import UserCreationForm
from ReviewBook.forms import SignUpForm
from dashboard.models import Book
from django.db.models import Count

#homepage (called Dashboard in project specs)
def index(request):
    try: #get most read books by ranking how many times it has been added to the DB
        books = Book.objects.values('title', 'author').annotate(title_count=Count('*')).order_by('-title_count')[:5]       
    except:
        books = None
        
    try: #get highest rated books in order of descending rating
        ratedBooks = Book.objects.values('title', 'author', 'rating').annotate(title_count=Count('*')).order_by('-rating')[:5]
    except:
        ratedBooks = None

    try: #get most recently added books in order of creation timestamps
        recentBooks =  Book.objects.all().annotate(title_count=Count('*')).order_by('-created_at')[:5]
    except:
        recentBooks = None
        
    auth = request.user.is_authenticated #store user is_auth
    return render(request, 'index.html',{ #render index template with books and auth
        'books':books, 
        'ratedBooks':ratedBooks,
        'recentBooks':recentBooks,
        'auth':auth
        })

#login portal
def login(request):
    if request.user.is_authenticated: #if auth then redirect to dashboard
        return redirect('/dashboard')
    else:
        return redirect('/auth/login') #else send to login page

#sign up form
def signup(request): 
    if request.method == 'POST': #if form is being submitted
        form = SignUpForm(request.POST) 
        if form.is_valid(): #validate form and save
            form.save()
            #get user and pass then login and redirect to user dashboard
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            log_in(request, user)
            return redirect('/dashboard')
    else: #else then render empty form
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

#simple logout
def logout(request):
    log_out(request)
    return redirect('/') #return to home page
