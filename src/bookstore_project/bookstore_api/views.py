# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from . import serializers
from . import models
from . import permissions

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, updating and deleting profiles."""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token."""
    serializer_class = AuthTokenSerializer
    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token."""
        return ObtainAuthToken().post(request)

class BooksViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items."""
    authentication_classes= (TokenAuthentication,)
    serializer_class =  serializers.UpdateBooksSerializer
    queryset = models.Books.objects.all()
    #permission_classes = (permissions.PostOwnStatus, IsAuthenticatedOrReadOnly)
    permission_classes = (permissions.UpdateBooks, IsAuthenticated)
    #permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('author_name', 'genre_name',)
    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""
        serializer.save(user_profile=self.request.user)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)
