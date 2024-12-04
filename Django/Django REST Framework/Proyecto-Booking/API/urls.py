from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, ResourceViewSet, BookingViewSet
from django.contrib.auth.models import User

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'resources', ResourceViewSet)
router.register(r'booking', BookingViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls))
]