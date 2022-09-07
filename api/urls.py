from django.urls import path, include
from .views import (BookStoresListApiView,)

urlpatterns = [
    path('allbooks', BookStoresListApiView.as_view()),
    # path('allbooks/<int:pk>/', BookStoresListApiView.as_view()),
]
