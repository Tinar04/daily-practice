from django.shortcuts import render
from django.http import HttpResponse
from .mock_data import BOOKS

# Create your views here.
for i in range(len(BOOKS)):
    print(BOOKS[i].get('genre','not found'))

# search function 
def func(query,BOOKS):
    if query:
            list_of_books = [book for book in BOOKS if query.lower() in book['name'].lower() or query.lower() in book['genre'].lower()]
    else:
        list_of_books = BOOKS
    return list_of_books



def book_view(request):
    query = request.GET.get("search",'')

    book_list = func(query,BOOKS)
    
    context = {
        'books':book_list
    }
    return render(request,'display_books.html',context)

def book_detail_view(request,book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            b = book
            break

    else:
        b = None
            
    context = {
        'book':b
    }
    return render(request,'book_detail.html',context)

def historical_fiction_view(request):
    query = request.GET.get("search",'')
    list = [book for book in BOOKS if book['genre'].lower()=='historical fiction']

    book_list = func(query,list)    

    context = {
        'books':book_list
    }
    return render(request,'display_books.html',context)


def fantasy_view(request):
    query = request.GET.get("search",'')
    list = [book for book in BOOKS if book['genre'].lower()=='fantasy']

    book_list = func(query,list)
    context = {
        'books':book_list

    }
    return render(request,'display_books.html',context)

def mystery_view(request):
    query = request.GET.get("search",'')
    list = [book for book in BOOKS if book['genre'].lower()=='mystery']
    
    book_list = func(query,list)
    context = {
        'books':book_list
    
        }
    return render(request,'display_books.html',context)

def romance_view(request):
    query = request.GET.get("search",'')
    list = [book for book in BOOKS if book['genre'].lower()=='romance']
    
    book_list = func(query,list)
    context = {
        'books':book_list
    
        }
    return render(request,'display_books.html',context)

def science_fiction_view(request):
    query = request.GET.get("search",'')
    list = [book for book in BOOKS if book['genre'].lower()=='science fiction']
    
    book_list = func(query,list)
    context = {
        'books':book_list
    
        }
    return render(request,'display_books.html',context)
