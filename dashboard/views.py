from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dashboard.models import Book
from dashboard.forms import BookForm, EditBookForm
import csv
from django.http import HttpResponse

@login_required
def dashboard(request):
    username = request.user
    try:
        books = Book.objects.all().filter(user=username)
    except:
        books = None
    return render(request, 'dashboard.html', {
        'name':username,
        'books':books
        })
@login_required
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
@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {
        'form': form,
        'user':request.user
    })
@login_required
def user_profile(request):
    user = request.user
    return render(request, 'user_profile.html', {
        'user':user
        })
@login_required
def book_profile(request, *args, **kwargs):
    bookTitle = kwargs['book_title']
    book = Book.objects.get(title=bookTitle, user=request.user)
    if request.method == 'POST':
        form = EditBookForm(request.POST)
        if form.is_valid():
            book.title = request.POST.get("title", "")
            book.author = request.POST.get("author", "")
            book.genre = request.POST.get("genre", "")
            book.rating = request.POST.get("rating", "")
            book.review_desc = request.POST.get("review_desc", "")
            book.save()
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = EditBookForm(instance=book)
    return render(request, 'book_profile.html', {
        'form': form,
        'book_title':book.title
    })
@login_required
def delete_book(request, *args, **kwargs):
    bookTitle = kwargs['book_title']
    book = Book.objects.get(title=bookTitle, user=request.user)
    book.delete()
    return redirect('dashboard')

@login_required
def dwnld_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ReviewBook.csv"'
    userbooks = Book.objects.all().filter(user=request.user)
    writer = csv.writer(response)
    writer.writerow(['Book ID', 'Title', 'Author', 'Genre', 'Timestamp', 'Rating', 'Review/Description'])
    for book in userbooks:
         writer.writerow([book.book_id, book.title, book.author, book.genre, book.created_at, book.rating, book.review_desc])
    return response