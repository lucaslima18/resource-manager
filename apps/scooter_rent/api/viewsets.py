from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from apps.scooter_rent.models import Scooter
from apps.scooter_rent.api.serializers import ScooterSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class ScooterViewSet(ModelViewSet):
    """
    """

    queryset = Scooter.objects.all()
    serializer_class = ScooterSerializer

    #Ver somente as scooters livres

    #alugar uma scooter

    #liberar uma scooter

    


class UserViewSet(ModelViewSet):
    """
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    #pesquisar por nome de usuário 
