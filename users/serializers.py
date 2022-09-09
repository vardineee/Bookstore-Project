from rest_framework import serializers
from . import models


class CustomUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ['email', 'gender', 'id', 'username']
