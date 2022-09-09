from django.urls import path, include
from .views import (CustomUserApiView)

urlpatterns = [
    path('users', CustomUserApiView.as_view()),
    path('user/<int:pk>', CustomUserApiView.as_view())

]
