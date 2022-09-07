from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
from . import serializers
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
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk):
    #     bookstore = self.get_object(pk)
    #     bookstore.delete()
    #     return Response(status.HTTP_204_NO_CONTENT)
