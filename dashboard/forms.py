from django.forms import ModelForm
from dashboard.models import Book

class BookForm(ModelForm):
	class Meta:
		model = Book
		fields = ['book_id', 'title', 'author', 'genre']