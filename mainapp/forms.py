from django import forms
from mainapp.models import Book, User

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=25)
    password = forms.CharField(label="Password")

class RegisterForm(forms.Form):
    CHOICES = (('pria', 'Pria'),('wanita', 'Wanita'),)
    email = forms.EmailField(label="Email", max_length=50 )
    password = forms.CharField(widget=forms.PasswordInput, label="Password", max_length=25)
    firstname = forms.CharField(label="First Name", max_length=50)
    lastname = forms.CharField(label="Last Name", max_length=50)
    gender = forms.ChoiceField(label="Gender", choices=CHOICES)
    address = forms.CharField(label="Address", max_length=50)
    phone = forms.CharField(label="Phone Number", max_length=50)

class BookForm(forms.Form):
    name = forms.CharField(label="Name Book", max_length=50)
    retail_price = forms.IntegerField(label="Retail Price")
    rent_price = forms.IntegerField(label="Rental Price")

class RentForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    book = forms.ModelChoiceField(queryset=Book.objects.all())
    end_date = forms.DateTimeField(widget=forms.widgets.DateTimeInput, label="Tanggal Kembali")
