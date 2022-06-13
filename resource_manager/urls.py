from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from apps.scooter_rent.api.viewsets import ScooterViewSet, UserViewSet
from rest_framework.authtoken import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Scooter Rent",
      default_version='v1',
      description="This application is responsible for scooters rent",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="lucas.ala1999@gmail.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register(r'scooters', ScooterViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]

urlpatterns += [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

