from rest_framework import serializers

from .models import CarInGarage, Promotion, Service, City


class CarInGarageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarInGarage
        fields = ['title', 'vin', 'mileage', 'next_TO_mileage', 'next_TO_date']


class PromotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promotion
        fields = ['title_of_promotion', 'description', 'date_start', 'date_start', 'image', 'city']


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ['title_of_service', 'description', 'list_of_services', 'image', 'city', 'longitube', 'latitube']


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ['name']
