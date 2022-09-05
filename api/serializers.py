from rest_framework import serializers
from . import models

class BookStoresListSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.BookStoresList
        fields = ['bookstore_name', 'bookstore_address', 'phone_number', 'user']
