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
