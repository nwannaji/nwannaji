from django.db.models import Count
from django.shortcuts import render
from django.views import View
from .models import Author, Book

# Create your views here.

def list_books(request):
    """
    List the books that have reviews
    """
    books = Book.objects.exclude(review_date__isnull = True).prefetch_related('author')
    context = {
        'books':books
    }
    return render(request, 'list.html', context)
class AuthorList(View):
    def get(self, request):

        authors = Author.objects.annotate(
            published_books = Count('books')
        ).filter(published_books__gt = 0)

        context = {
            'authors':authors
        }
        return render(request, 'authors.html',context)
    
class BookDetails(View):
    def get(self, request):

        bookdetails = Book.objects.all()
        context = {
            'bookdetails':bookdetails
        }
        return render(request, 'book.html', context)
    
class AuthorDetails(View):
    def get (self, request):

        authordetails = Author.objects.all()
        context = {
            'authordetails': authordetails
        }
        return render(request, 'authors.html', context)
    
