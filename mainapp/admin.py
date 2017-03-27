from django.contrib import admin
from mainapp.models import User, Book, Profile, Rental

# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Profile)
admin.site.register(Rental)
