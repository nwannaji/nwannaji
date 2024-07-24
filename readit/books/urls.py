from django.urls import path
from . import views
"""
In the below URL decoration, I used both function base and class/function 
decoration to show that one can either choose one  based on preference or use both.
"""

urlpatterns =[
 path('', views.list_books, name='books'),   # Function base url decoration
 path('authors/', views.AuthorList.as_view(), name='authors'),  # Class & Function base url decoration
 path('book/<int:pk>', views.BookDetails.as_view(), name='book'),   # Class & Function base url decoration
 path('author/<int:pk>', views.AuthorDetails.as_view(), name='author'),   # Class & Function base url decoration

]