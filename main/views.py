from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .models import CarInGarage, Promotion, Service, City
from .serializers import CarInGarageSerializer, PromotionSerializer, ServiceSerializer, CitySerializer


class CarInGarageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CarInGarage.objects.all()
    serializer_class = CarInGarageSerializer
    # permission_classes = [IsAuthenticated]


class PromotionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    # permission_classes = [IsAuthenticated]


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    # permission_classes = [IsAuthenticated]


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    # permission_classes = [IsAuthenticated]


def index(request):
    refresh = RefreshToken.for_user(request.user)
    context = {
        "refresh": str(refresh),
        "access": str(refresh.access_token)
               }
    return render(request, 'main/index.html', context)
