from django.db.models import Count
from django.shortcuts import render
from django.views.generic import View, DetailView
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
    
class BookDetails(DetailView):
    model = Book
    pk_url_kwarg = 'pk'
    template_name = 'book.html'
    
    
class AuthorDetails(DetailView):
    model = Author
    pk_url_kwarg = 'pk'
    template_name = "authors.html"
