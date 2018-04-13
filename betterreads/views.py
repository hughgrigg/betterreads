from django.contrib.auth.models import User
from rest_framework import viewsets
from betterreads.models import Author, Book, UserReadingList,\
    UserReadingListItem
from betterreads.serializers import UserSerializer, AuthorSerializer, \
    BookSerializer, UserReadingListSerializer, UserReadingListItemSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer


class UserReadingListViewSet(viewsets.ModelViewSet):
    queryset = UserReadingList.objects.all()
    serializer_class = UserReadingListSerializer


class UserReadingListItemViewSet(viewsets.ModelViewSet):
    queryset = UserReadingListItem.objects.all()
    serializer_class = UserReadingListItemSerializer
