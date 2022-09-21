from django.urls import path, include
from . import views

urlpatterns = [
    path('bookstores', views.BookStoresListApiView.as_view()),
    path('bookstore/<int:pk>', views.BookStoresListApiView.as_view()),
    path('newbookstore', views.BookStoresListApiView.as_view()),
    path('allbooks', views.BookApiView.as_view()),
    path('newbook', views.BookApiView.as_view()),
    path('book/<int:pk>', views.BookApiView.as_view()),
    path('mybooks', views.UserBookApiView.as_view()),
    path('addtocart', views.CartItemView.as_view()),
    path('addtocart/<int:pk>', views.CartItemView.as_view())
]
