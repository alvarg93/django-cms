from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission

from app.models import Book


class CustomUpdatePermission(BasePermission):
    """
    Permission class to check that a user can update his own resource only
    """

    def has_permission(self, request, view):
        # check that its an update request and user is modifying his resource only
        print (view.action)
        if view.action == 'update' and view.kwargs['id'] != request.user.id:
            return False  # not grant access
        return True  # grant access otherwise


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
        permission_classes = [CustomUpdatePermission]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author', 'year')
        permission_classes = [IsAuthenticatedOrReadOnly]
