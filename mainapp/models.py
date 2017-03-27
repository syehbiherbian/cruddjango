from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)
    firstname = models.CharField(max_length=35)
    lastname = models.CharField(max_length=45)
    def __unicode__(self):
        return self.firstname

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender =models.CharField(max_length=20)
    address = models.TextField()
    phone = models.CharField(max_length=15)

class Book(models.Model):
    name = models.CharField(max_length=50)
    cover = models.ImageField()
    created_date = models.DateField(default=datetime.datetime.now())
    retail_price = models.IntegerField()
    rent_price = models.IntegerField()
    def __unicode__(self):
        return self.name

class Rental(models.Model):
    STATUS_CHOICES = (
    ('rented', 'Rented'),
    ('completed', 'Completed')
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        blank=True
    )
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="rented")
    total_days = models.IntegerField(null=True, blank=True)
    debited_funds = models.IntegerField(null=True, blank=True)

    @property
    def different_days(self):
        diff_days = (timezone.now() - self.start_date).days
        if diff_days > 5 :
            if self.status == 'rented' :
                self.status = 'completed'

        self.total_days = diff_days
        self.save()
        return diff_days

    @property
    def debited(self):
        debited = self.book.rent_price * self.total_days
        self.debited_funds = debited
        self.save()
        return debited
