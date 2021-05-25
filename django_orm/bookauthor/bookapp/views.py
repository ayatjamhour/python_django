from django.shortcuts import render, HttpResponse,redirect
from .models import *

# INDEX - SHOW BOOKS

def index(request):
    context = { 
    "books" : book.objects.all(),
    "authors" : author.objects.all(),
    }
    return render(request,'index.html',context)

# CREATE A NEW BOOK


def add_book(request):
    b_title = request.POST['book_title']
    b_desc = request.POST['book_desc']
    book.objects.create(title=b_title,desc=b_desc)
    return redirect('/')


# INFO PAGE - BOOK

def show_book(request,id):
    book_to_Show = book.objects.get(id=id)
    book_authors=book_to_Show.authors.all()
    authors_to_show = author.objects.all()
    context = { 
        "book_to_get_title" : book_to_Show.title,
        "book_to_get_id" : book_to_Show.id,
        "book_to_get_desc" : book_to_Show.desc,
        "book_to_get_authors" : book_authors,
        "drop_down_authors" :authors_to_show,
        
    }
    
    return render(request,'bookinfo.html',context)


# ADD AUTHOR TO A BOOK

def add_book_to_author(request):
    b_id=request.POST['book_id']
    a_id = request.POST['all_authors_menu']
    this_book=book.objects.get(id=b_id)
    this_author=author.objects.get(id=a_id)
    this_book.authors.add(this_author)
    return redirect('/books/' + b_id)

def add_author_to_book(request):
    
    a_id=request.POST['author_id']
    b_id = request.POST['all_books_menu']
    this_author=author.objects.get(id=a_id)
    this_book=book.objects.get(id=b_id)
    this_author.books.add(this_book)
    return redirect('/authors/' + a_id)


# SHOW ALL AUTHORS

def show_authors(request):

    author_list = author.objects.all()

    context = {
        "author_list_html": author_list
    }

    return render(request, "addauthor.html", context)


# SHOW AUTHOR
def add_author(request):
    a_first_name = request.POST['f_name']
    a_last_name = request.POST['l_name']
    Notes = request.POST['notes_box']
    author.objects.create(first_name=a_first_name,last_name=a_last_name,notes=Notes)
    return redirect('/authors')


# display auathor
def display_author(request):
    context = {
        "all_authors" : author.objects.all()
    }
    return render(request,'authorinfo.html',context)

# ###################
# # ADD A BOOK TO AN AUTHOR
# ####################


# def add_book(request, number):

#     author_id = int(number)
#     add_book_id = int(request.POST["book"])

#     c = author.objects.get(id=author_id)
#     d = book.objects.get(id=add_book_id)
#     c.books.add(d)

#     messages.add_message(request, messages.INFO, "Book added!")

#     return redirect(f"/authors/{number}")
