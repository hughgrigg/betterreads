from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    """
    An author of books that exists in the world.
    """
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=127)


class Book(models.Model):
    """
    A book that exists in the world.
    """
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateField(blank=True)
    title = models.CharField(max_length=127)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class UserReadingList(models.Model):
    """
    A user's reading list of books.
    """
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=127)


class UserReadingListItem(models.Model):
    """
    An individual item on a user's reading list.
    """
    created = models.DateTimeField(auto_now_add=True)
    reading_list = models.ForeignKey(UserReadingList, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
