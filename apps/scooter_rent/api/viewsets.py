from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from apps.scooter_rent.models import Scooter
from apps.scooter_rent.api.serializers import ScooterSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ValidationError

class ScooterViewSet(ModelViewSet):
    """
    """

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Scooter.objects.all()
    serializer_class = ScooterSerializer
    
    

    def create(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user)
        scooter = Scooter()
        scooter.scooter_model = request.data['scooter_model']
        scooter.rent_date = request.data['rent_date']
        scooter.end_rent_date = request.data['end_rent_date']
        scooter.user =  request.data['user']
    
    
        if not user.is_staff:
            Response.status_code = 404
            return Response({'resp': "not success"})
        
        
        scooter.save()

        return Response({'resp': "success"})


    #Ver somente as scooters livres

    #alugar uma scooter

    #liberar uma scooter


class UserViewSet(ModelViewSet):
    """
    """

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        """
        """
        user = User()
        user.username = request.data['username']
        user.set_password(request.data['password'])
        user.save()

        
        return Response({'resp': "success"})
