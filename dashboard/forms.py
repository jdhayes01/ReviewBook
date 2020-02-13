from django.forms import ModelForm, HiddenInput
from dashboard.models import Book

class BookForm(ModelForm):
	class Meta:
		model = Book
		fields = ['title', 'author', 'genre', 'user']
		widgets = {'user': HiddenInput()}