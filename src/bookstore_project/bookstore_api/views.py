# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import viewsets

from . import serializers
from . import models

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, updating and deleting profiles."""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
