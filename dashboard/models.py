from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
#All books added by users stored as unique records
class Book(models.Model):
	#variables for genre choices
	genre_choices = (
		('nonfiction', 'NONFICTION'),
		('fiction', 'FICTION'),
		('narrative', 'NARRATIVE'),
		('science fiction', 'SCIENCE FICTION'),
		('romance', 'ROMANCE'),
		('history', 'HISTORY'),
		('fantasy', 'FANTASY'),
		('educational', 'EDUCATIONAL'),
		('thriller', 'THRILLER'),
		('children', 'CHILDREN'),
	)
	#model fields
	book_id = models.AutoField(primary_key=True)
	title = models.CharField('Book Title', max_length=120)
	author = models.CharField('Book Author', max_length=120)
	genre = models.CharField(max_length=40, choices=genre_choices, default='nonfiction')
	user = models.CharField('user', max_length=120, default='Default')
	created_at = models.DateTimeField(auto_now_add=True)
	rating = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
	review_desc =models.TextField(default='-- no description --')

	def __str__(self):
		return self.title
