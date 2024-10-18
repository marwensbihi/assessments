
from django.contrib.auth import authenticate

from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    
    username = serializers.CharField(
        min_length=1,
        required=True,
        error_messages={
            'required': 'Username is required.',
            'min_length': 'Username must be at least 1 character long.'
        }
    )
    password = serializers.CharField(
        min_length=1,
        required=True,
        write_only=True,  # Do not return the password in responses
        error_messages={
            'required': 'Password is required.',
            'min_length': 'Password must be at least 1 character long.'
        }
    )

    def validate(self, attrs):
        """Custom validation to check if the username and password are correct."""
        username = attrs.get('username')
        password = attrs.get('password')

        # Authenticate the user
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError('Invalid credentials. Please try again.')
        
        attrs['user'] = user  # Store the user object in the attributes
        return attrs
