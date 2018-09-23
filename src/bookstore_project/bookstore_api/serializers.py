from rest_framework import serializers

from . import models

class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user."""
        user = models.UserProfile(
            email = validated_data['email'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

class UpdateBooksSerializer(serializers.ModelSerializer):
    """A serializer for profile feed items."""
    class Meta:
        model = models.Books
        fields = ('id', 'user_profile','book_name','author_name', 'genre_name', 'publication_house_name','added_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
