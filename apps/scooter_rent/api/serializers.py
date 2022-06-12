from rest_framework import serializers
from apps.scooter_rent.models import Scooter
from django.contrib.auth.models import User


class ScooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scooter
        fields = ['id', 'scooter_model', 'rent_date', 'end_rent_date', 'user']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']