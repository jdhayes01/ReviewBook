from django.test import TestCase
from dashboard.models import Book
from django.urls import reverse
from dashboard.forms import BookForm, EditBookForm

class BookTestCase(TestCase):
    def setUp(self):
        Book.objects.create(title='Green Eggs and Ham', author='Dr. Seuss', genre='children')

    def test_book_values(self):
        test_book = Book.objects.get(title='Green Eggs and Ham')
        self.assertTrue(isinstance(test_book, Book))
        self.assertEqual(test_book.title, 'Green Eggs and Ham')
        self.assertEqual(test_book.author, 'Dr. Seuss')
        self.assertEqual(test_book.genre, 'children')
        self.assertEqual(test_book.__str__(), test_book.title)

    def test_edit_book_values(self):
        test_book = Book.objects.get(title='Green Eggs and Ham')
        test_book.rating = 5
        test_book.review_desc = "Green Eggs and Ham is a children's book by Dr. Seuss"
        test_book.save()
        self.assertEqual(test_book.rating, 5)
        self.assertEqual(test_book.review_desc, "Green Eggs and Ham is a children's book by Dr. Seuss")

class DashboardTestCase(TestCase):

    def test_dashboard_view(self):
        url = reverse('dashboard')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)

    def test_changepass_view(self):
        url = reverse('change_pass')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)

    def test_addbook_view(self):
        url = reverse('add_book')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)

    def test_userprofile_view(self):
        url = reverse('user_profile')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)

    def test_bookprofile_view(self):
        url = reverse('book_profile', args=['Green Eggs and Ham'])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)

    def test_deletebook_view(self):
        url = reverse('delete_book', args=['Green Eggs and Ham'])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)

    def test_dwnldcsv_view(self):
        url = reverse('dwnld_csv')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)

class BookFormsTestCase(TestCase):  

    def setUp(self):
        Book.objects.create(title='Green Eggs and Ham', author='Dr. Seuss', genre='children', rating=5, review_desc='A classic by Dr. Seuss')

    def test_addbook_form(self):
        test_book = Book.objects.get(title='Green Eggs and Ham')
        data = {
          'title': test_book.title, 
          'author': test_book.author,
          'genre': test_book.genre,
          'user': 'user',
          }
        form = BookForm(data=data)
        self.assertTrue(form.is_valid()) 

    def test_editbook_form(self):
        test_book = Book.objects.get(title='Green Eggs and Ham')
        data = {
          'title': test_book.title, 
          'author': test_book.author,
          'genre': test_book.genre,
          'rating': test_book.rating,
          'review_desc': test_book.review_desc,
          }
        form = EditBookForm(data=data)
        self.assertTrue(form.is_valid()) 

