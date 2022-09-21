from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
from . import serializers

# Create your views here.

class CustomUserApiView(APIView):
    def get(self,request):
        users = models.CustomUser.objects.all()
        serializer = serializers.CustomUserSerializers(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self,request):
        serializer = serializers.CustomUserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk):
        user = models.CustomUser.objects.get(id=pk)
        serializer = serializers.CustomUserSerializers(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
