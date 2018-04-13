from django.contrib.auth.models import User
from rest_framework import serializers
import betterreads.models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = betterreads.models.Author
        fields = ('name',)


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = betterreads.models.Book
        fields = ('published', 'title', 'author')


class UserReadingListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = betterreads.models.UserReadingList
        fields = ('owner', 'name')


class UserReadingListItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = betterreads.models.UserReadingListItem
        fields = ('reading_list', 'book')
