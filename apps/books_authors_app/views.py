from django.shortcuts import render, redirect 
from .models import * 
 
 
 
# Create your views here. 
def index(request): 
    all_books = Books.objects.all()
    context = {
        "all_books":all_books
    }
    return render(request, 'books_authors_app/index.html', context) 


def createBook(request):
    Books.objects.create(title=request.POST['title'], desc=request.POST['desc'])
    return redirect('/')

def bookPage(request, id):
    book = Books.objects.get(id=id)
    context = {
        "book":book,
        "all_authors":Authors.objects.all()
    }

    return render(request, 'books_authors_app/book_page.html', context)

def addAuthor(request):
    author_to_add = Authors.objects.get(id=request.POST['author'])
    book = Books.objects.get(id=request.POST['book'])
    book.authors.add(author_to_add)
    book.save()
    return redirect("/books/" + str(book.id))

def authors(request):
    all_authors = Authors.objects.all()
    context = {
        "all_authors":all_authors
    }

    return render(request, 'books_authors_app/authors.html', context)

def newAuthor(request):
    
    Authors.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], notes = request.POST['notes'])

    return redirect("/authors/")

def authorPage(request, id):
    author = Authors.objects.get(id=id)
    all_books = Books.objects.all()
    context = {
        "author":author,
        "all_books":all_books
    }

    return render(request, 'books_authors_app/author_page.html', context)

def addBook(request):
    author = Authors.objects.get(id=request.POST['author'])
    book = Books.objects.get(id=request.POST['book'])

    author.books.add(book)
    author.save()
    return redirect("/authorPage/" + str(author.id))
