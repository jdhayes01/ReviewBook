from django.forms import ModelForm, HiddenInput
from dashboard.models import Book

# Form for adding book based off Book model
class BookForm(ModelForm):
	class Meta:
		model = Book
		fields = ['title', 'author', 'genre', 'user']
		widgets = {'user': HiddenInput()}

# Form to edit book details based off book model
class EditBookForm(ModelForm):
	class Meta:
		model = Book
		fields = ['title', 'author', 'genre', 'rating', 'review_desc']