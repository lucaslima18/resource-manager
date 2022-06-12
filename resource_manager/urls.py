from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from apps.scooter_rent.api.viewsets import ScooterViewSet, UserViewSet


router = routers.DefaultRouter()
router.register(r'scooters', ScooterViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
