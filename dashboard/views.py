from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dashboard.models import Book
from dashboard.forms import BookForm, EditBookForm
import csv
from django.http import HttpResponse

#User dashboard
@login_required
def dashboard(request):
    username = request.user
    try: #get users books
        books = Book.objects.all().filter(user=username)[:5]
    except:
        books = None

    try: #get top rated books
        ratedbooks = Book.objects.all().filter(user=username).order_by('-rating')[:5]
    except:
        ratedbooks = None

    return render(request, 'dashboard.html', { #render user dashboard with data
        'name':username,
        'books':books,
        'ratedbooks':ratedbooks
        })
#change password
@login_required
def change_pass(request):
    if request.method == 'POST': #if form is being submitted
        form = PasswordChangeForm(request.user, request.POST) 
        if form.is_valid():#validate form
            user = form.save()
            update_session_auth_hash(request, user) #updates the session hash to prevent a password change from logging out the user 
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else: #else load form for user
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })
#Add Book
@login_required
def add_book(request):
    if request.method == 'POST': #if form is being submitted
        form = BookForm(request.POST)
        if form.is_valid(): #validate form
            form.save()
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else: #else load empty book
        form = BookForm()
    return render(request, 'add_book.html', {
        'form': form,
        'user':request.user
    })
#Render User Profile
@login_required
def user_profile(request):
    user = request.user
    return render(request, 'user_profile.html', {
        'user':user
        })
#Render Book Profile (to edit/delete)
@login_required
def book_profile(request, *args, **kwargs): #book to edit passed in kwargs
    bookTitle = kwargs['book_title'] #get clicked book title
    book = Book.objects.get(title=bookTitle, user=request.user) #get appropriate book
    if request.method == 'POST': #if edit book form is being submitted
        form = EditBookForm(request.POST)
        if form.is_valid(): #validate form
            #set all appropriate values
            book.title = request.POST.get("title", "")
            book.author = request.POST.get("author", "")
            book.genre = request.POST.get("genre", "")
            book.rating = request.POST.get("rating", "")
            book.review_desc = request.POST.get("review_desc", "")
            book.save() #save new values
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = EditBookForm(instance=book)
    return render(request, 'book_profile.html', {
        'form': form,
        'book_title':book.title
    })
#Delete Book within Book Profile
@login_required
def delete_book(request, *args, **kwargs): #book to delete passed in kwargs
    bookTitle = kwargs['book_title'] 
    book = Book.objects.get(title=bookTitle, user=request.user) #get appropriate book
    book.delete() #delete and redirect to user dashboard
    return redirect('dashboard')
#Download CSV file of books
@login_required
def dwnld_csv(request):
    # Create the HttpResponse object with the appropriate CSV header and details.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ReviewBook.csv"' 
    userbooks = Book.objects.all().filter(user=request.user) #get user's books
    writer = csv.writer(response) 
    writer.writerow(['Book ID', 'Title', 'Author', 'Genre', 'Timestamp', 'Rating', 'Review/Description']) #write first row
    for book in userbooks: #loop through user's books writing a new row for each record
         writer.writerow([book.book_id, book.title, book.author, book.genre, book.created_at, book.rating, book.review_desc])
    return response