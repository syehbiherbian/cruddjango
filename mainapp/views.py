from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from mainapp.models import Book, User, Profile, Rental
from mainapp.forms import BookForm, RegisterForm, RentForm
from django import forms
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'home.html')

#Book
def listbook(request):
    book = Book.objects.all()
    return render(request, 'listbook.html', {'book': book})
def addbook(request):
    if request.method == 'POST':
        bookform = BookForm(request.POST)
        if bookform.is_valid():
            book, status = Book.objects.get_or_create(name=bookform.cleaned_data['name'], retail_price=bookform.cleaned_data['retail_price'], rent_price=bookform.cleaned_data['rent_price'])
            return HttpResponseRedirect('/listbook')
    else:
        bookform = BookForm()
    return render(request, 'addbook.html', {'bookform' : bookform})
def editbook(request, id):
    editbook = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            editbook.name = form.cleaned_data['name']
            editbook.retail_price = form.cleaned_data['retail_price']
            editbook.rent_price = form.cleaned_data['retail_price']
            editbook.save()
            return HttpResponseRedirect('/listbook')
    else:
        form = BookForm(initial = {'name' : editbook.name, 'retail_price' : editbook.retail_price, 'rent_price' : editbook.rent_price })
    return render(request, 'editbook.html', {'form' : form})
def detailbook(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'detailbook.html', {
        'name': book.name,
        'cover': book.cover,
        'retail_price' : book.retail_price,
        'rebt_price' : book.rent_price
    })
def deletebook(request, id):
    hapusrental = Rental.objects.filter(book__id=id)
    hapusrental.delete()
    hapusbuku = Book.objects.get(id=id)
    hapusbuku.delete()
    return HttpResponseRedirect('/listbook')

#User
def listuser(request):
    user = User.objects.all()
    return render(request, 'listuser.html', {'user': user})
def edituser(request, id):
    edituser= User.objects.get(id=id)
    editprofile= Profile.objects.get(user=edituser)
    if request.method == 'POST':
        editform = RegisterForm(request.POST)
        if editform.is_valid():
            edituser.email = editform.cleaned_data['email']
            edituser.password = editform.cleaned_data['password']
            edituser.firstname = editform.cleaned_data['firstname']
            edituser.lastname = editform.cleaned_data['lastname']
            edituser.save()

            editprofile.gender = editform.cleaned_data['gender']
            editprofile.address = editform.cleaned_data['address']
            editprofile.phone = editform.cleaned_data['phone']
            editprofile.save()
            return HttpResponseRedirect('/listuser')
    else:
        editform = RegisterForm(initial = {'email' : edituser.email, 'password' : edituser.password, 'firstname' : edituser.firstname, 'lastname' : edituser.lastname, 'gender' : editprofile.gender, 'address' : editprofile.address, 'phone' : editprofile.phone})
    return render(request, 'edituser.html', {'editform' : editform})
def detailuser(request, id):
    user = User.objects.get(id=id)
    detail = Profile.objects.get(user=user)
    return render(request, 'detailuser.html', {'email': user.email, 'password': user.password, 'firstname' : user.firstname, 'lastname': user.lastname, 'gender': detail.gender, 'address' : detail.address, 'phone' : detail.phone})

def deleteuser(request, id):
    hapusrental = Rental.objects.filter(user__id=id)
    hapusrental.delete()
    hapususer = User.objects.get(id=id)
    hapusprofile = Profile.objects.get(user=hapususer)
    hapususer.delete()
    hapusprofile.delete()
    return HttpResponseRedirect('/listuser')

#tambah user
def adduser(request):
    if request.method == 'POST':
        regisform = RegisterForm(request.POST)
        if regisform.is_valid():
            user, status = User.objects.get_or_create(email=regisform.cleaned_data['email'], password=regisform.cleaned_data['password'], firstname=regisform.cleaned_data['firstname'], lastname=regisform.cleaned_data['lastname'],)
            profile, status = Profile.objects.get_or_create(user=user, gender=regisform.cleaned_data['gender'], address=regisform.cleaned_data['address'], phone=regisform.cleaned_data['phone'])
            return HttpResponseRedirect('/listuser')
    else:
        regisform = RegisterForm()
    return render(request, 'register.html', {'regisform' : regisform})

#Rental
def listrental(request):
    rental = Rental.objects.all()
    # return HttpResponse(rental.total_days)
    return render(request, 'listrental.html', {'rental' : rental})

def addrental(request):
    if request.method == 'POST':
        rentform = RentForm(request.POST)
        if rentform.is_valid():
            rental, status = Rental.objects.get_or_create(user=rentform.cleaned_data['user'], book=rentform.cleaned_data['book'])
            # user, status = User.objects.get_or_create(email=regisform.cleaned_data['email'], password=regisform.cleaned_data['password'], firstname=regisform.cleaned_data['firstname'], lastname=regisform.cleaned_data['lastname'],)
            # profile, status = Profile.objects.get_or_create(user=user, gender=regisform.cleaned_data['gender'], address=regisform.cleaned_data['address'], phone=regisform.cleaned_data['phone'])
            return HttpResponseRedirect('/listrental')
    else:
        rentform = RentForm()
    return render(request, 'addrental.html', {'rentform' : rentform})


def completedrental(request, id):
    rental = Rental.objects.get(id=id)
    rental.status = 'completed'
    rental.end_date = timezone.now()
    rental.save()
    return HttpResponseRedirect('/listrental/')
