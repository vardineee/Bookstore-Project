from django.db import models
from users.models import CustomUser as User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class BookStoresList(models.Model):
    bookstore_name = models.CharField(max_length=30)
    bookstore_address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.bookstore_name

class Book(models.Model):
    bookstore = models.ForeignKey(BookStoresList, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=30)
    publish_year = models.DateField()
    publisher = models.CharField(max_length=50)
    author = models.CharField(max_length=250)
    language = models.CharField(max_length=30)
    isbn = models.IntegerField()
    price = models.FloatField()
    book_thumbnail = models.ImageField(upload_to=None, blank=True, null=True)

    def __str__(self):
        return self.book_title

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.email


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True)
    user_book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.user_book.book_title
