from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BookStoresList(models.Model):
    bookstore_name = models.CharField(max_length=30)
    bookstore_address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.bookstore_name
