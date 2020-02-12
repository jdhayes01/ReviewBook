from django.db import models

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

	def __str__(self):
		return self.name


#Books added by users with their corresponding book_id and user_id
class BookAdded(models.Model):
	id = models.AutoField(primary_key=True)
	book_title = models.CharField('Book Title', max_length=120, default='Default') 
	user = models.CharField('user', max_length=120, default='Default') 

#Review added by users with their correspond user_id
class Reviews(models.Model):
	#model fields
	review_id = models.AutoField(primary_key=True)
	book_id = models.IntegerField()
	user_id = models.IntegerField()
	rating = models.IntegerField()
	review_desc =models.TextField()