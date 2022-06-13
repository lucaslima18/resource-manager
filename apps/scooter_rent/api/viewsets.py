from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from apps.scooter_rent.models import Scooter
from apps.scooter_rent.api.serializers import ScooterSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ValidationError
from datetime import datetime

class ScooterViewSet(ModelViewSet):
    """

    """

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Scooter.objects.all()
    serializer_class = ScooterSerializer
    
    

    def create(self, request, *args, **kwargs):
        """
        """
        
        user = User.objects.get(username=request.user)
        scooter = Scooter()
        scooter.scooter_model = request.data['scooter_model']
        scooter.license_plate = request.data['license_plate']

        try:
            scooter.rent_date = request.data['rent_date']
            scooter.end_rent_date = request.data['end_rent_date']
            scooter.user =  request.data['user']
        
        except:
            pass
    
        if not user.is_staff:
            Response.status_code = 404
            return Response({'message': "you dont have authrization to create scooters!"})
        
        if Scooter.objects.filter(license_plate=scooter.license_plate):
            Response.status_code = 404
            return Response({'message': f"{request.data['license_plate']} license plate already exists!"})  
        
        
        scooter.save()

        return Response({'message': "scooter success added!"})
    
    
    def update(self, request, *args, **kwargs):
        """

        """
        user = User.objects.get(username=request.user)
        scooter = Scooter.objects.get(id=self.get_object().id)
        blank_scooter_model_or_plate = False

        try:
            scooter.scooter_model = request.data['scooter_model']
            scooter.license_plate = request.data['license_plate']
            if Scooter.objects.filter(license_plate=scooter.license_plate):
                Response.status_code = 404
                return Response({'message': f"{request.data['license_plate']} license plate already exists!"}) 
        
        except:
            blank_scooter_model_or_plate = True

        scooter.rent_date = request.data['rent_date']
        scooter.end_rent_date = request.data['end_rent_date']
        scooter.user = User.objects.only('id').get(id=request.data['user'])

        if not user.is_staff:
            data_list = {
                "rent_date": scooter.rent_date,
                "end_rent_date": scooter.end_rent_date,
                "user":  scooter.user
            }

            for data in data_list:
                if not data_list[data]:
                    Response.status_code = 404
                    return Response({'message': f"{data} can not be empty!"}) 

            if not blank_scooter_model_or_plate:
               Response.status_code = 404
               return Response({'message': "you can't change the model name or license plate of the scooter!"})
            
            if request.user.id is not request.data['user']:
                return Response({'message': "você não pode atribuir esta scooter a outro usuário!"})


        scooter.save()

        return Response({'message': f"scooter {scooter.scooter_model} success updated!"})
    

    def partial_update(self, request, *args, **kwargs):
        """

        """
        user = User.objects.get(username=request.user)
        scooter = Scooter.objects.get(id=self.get_object().id)
        blank_scooter_model_or_plate = False

        try:
            scooter.scooter_model = request.data['scooter_model']
            scooter.license_plate = request.data['license_plate']
            if Scooter.objects.filter(license_plate=scooter.license_plate):
                Response.status_code = 404
                return Response({'message': f"{request.data['license_plate']} license plate already exists!"}) 
        
        except:
            blank_scooter_model_or_plate = True

        scooter.rent_date = request.data['rent_date']
        scooter.end_rent_date = request.data['end_rent_date']
        scooter.user = User.objects.only('id').get(id=request.data['user'])

        if not user.is_staff:
            data_list = {
                "rent_date": scooter.rent_date,
                "end_rent_date": scooter.end_rent_date,
                "user":  scooter.user
            }

            for data in data_list:
                if not data_list[data]:
                    Response.status_code = 404
                    return Response({'message': f"{data} can not be empty!"}) 

            if not blank_scooter_model_or_plate:
               Response.status_code = 404
               return Response({'message': "you can't change the model name or license plate of the scooter!"})
            
            if request.user.id is not request.data['user']:
                return Response({'message': "você não pode atribuir esta scooter a outro usuário!"})


        scooter.save()

        return Response({'message': f"scooter {scooter.scooter_model} success updated!"})


    def destroy(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user)
        scooter = Scooter.objects.filter(id=self.get_object().id)

        if not user.is_staff:
            Response.status_code = 404
            return Response({'message': "you dont have authrization to create scooters!"})
        
        scooter.delete()

        return Response({'message': "scooter successfully deleted!"})

class UserViewSet(ModelViewSet):
    """
    """

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        """
        """
        
        user = User()
        user.username = request.data['username']
        user.set_password(request.data['password'])
        user.is_staff = request.data['is_staff']
        user.save()

        
        return Response({'message': "success"})
