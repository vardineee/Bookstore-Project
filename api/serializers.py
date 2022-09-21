from rest_framework import serializers
from . import models
from django.db.models import Sum


class BookStoresListSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.BookStoresList
        fields = ['bookstore_name', 'bookstore_address', 'phone_number', 'user']


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ['bookstore', 'user','book_title', 'publish_year', 'publisher', 'author', 'language', 'isbn', 'price', 'book_thumbnail', 'pk']


class OwnCartItemSerializers(serializers.ModelSerializer):
    user_book = serializers.SerializerMethodField()
    print (user_book)
    class Meta:
        model = models.CartItem
        fields = ['pk', 'user_book', 'price']

    def get_user_book(self,obj):
        return BookSerializers(obj.user_book).data



class CartSerializers(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    cart_user_books = serializers.SerializerMethodField()
    class Meta:
        model = models.Cart
        fields = ['cart_user_books',  'active', 'total_price']


    def get_total_price(self,obj):
        return models.CartItem.objects.filter(cart=obj).aggregate(Sum('price'))['price__sum']


    def get_cart_user_books(self, obj):
        items = models.CartItem.objects.filter(cart=obj)
        return OwnCartItemSerializers(items, many=True).data
