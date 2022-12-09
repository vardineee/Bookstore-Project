from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
from . import serializers
from users.models import CustomUser as User
from django.http import Http404
# Create your views here.

class BookStoresListApiView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        bookstores = models.BookStoresList.objects.all()
        serializer = serializers.BookStoresListSerializers(bookstores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self,request):
        serializer = serializers.BookStoresListSerializers(data=request.data)
        if serializer.is_valid():
            obj = User.objects.filter(id=request.user.id)
            obj.update(owner=True)
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self,request,pk):
        bookstore = models.BookStoresList.objects.get(id=pk)
        serializer = serializers.BookStoresListSerializers(bookstore, data =request.data, partial =True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        bookstore = models.BookStoresList.objects.get(id=pk)
        bookstore.delete()
        return Response(status.HTTP_204_NO_CONTENT)

class BookApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        books = models.Book.objects.all()
        serializer =serializers.BookSerializers(books,many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request):
        serializer =serializers.BookSerializers(data=request.data)
        if request.user.owner == True:
            if serializer.is_valid():
                obj = models.BookStoresList.objects.filter(user=request.user)
                serializer.save(user=request.user, bookstore=obj)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        book = models.Book.objects.get(id=pk)
        print(book)
        if request.user == book.user:
            serializer = serializers.BookSerializers(book,data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'invalid token'},status=status.HTTP_401_UNAUTHORIZED)

    def delete(self,request,pk):
        remove_book = models.Book.objects.get(id=pk)
        remove_book.delete()
        return Response(status.HTTP_204_NO_CONTENT)



class UserBookApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        books = models.Book.objects.filter(user=request.user)
        serializer =serializers.BookSerializers(books,many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.BookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartItemView(APIView):
    def get_object(self,pk):
        try:
            return models.CartItem.objects.get(pk=pk)
        except models.CartItem.DoesNotExist:
            raise Http404

    def get(self, request):
        try:
            cart_items = models.Cart.objects.get(user=request.user)
        except:
            cart_items = models.Cart.objects.create(user=request.user)
        serializer = serializers.CartSerializers(cart_items)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def delete(self,request,pk):
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
