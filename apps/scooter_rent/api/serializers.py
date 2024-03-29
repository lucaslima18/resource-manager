from rest_framework import serializers
from apps.scooter_rent.models import Scooter
from django.contrib.auth.models import User


class ScooterSerializer(serializers.ModelSerializer):
    """
        Create a serializer for the Scooter model
    """

    class Meta:
        model = Scooter
        fields = ['id', 'scooter_model', 'license_plate', 'rent_date', 'end_rent_date', 'user']

class UserSerializer(serializers.ModelSerializer):
    """
        Create a serializer for the User model
    """
    
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'is_staff']