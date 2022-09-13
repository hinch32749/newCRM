from django.contrib.auth.models import AbstractUser
from django.db import models


class AdvUser(AbstractUser):
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')


class CarInGarage(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название авто')
    vin = models.CharField(max_length=50, verbose_name='VIN')
    mileage = models.IntegerField(verbose_name='Пробег')
    next_TO_mileage = models.IntegerField(verbose_name='Следующее ТО по милям')
    next_TO_date = models.DateField(verbose_name='Следующее ТО дате')

    class Meta:
        verbose_name_plural = 'Машины'
        verbose_name = 'Машина'

    def __str__(self):
        return f'{self.title}'


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Город')

    class Meta:
        verbose_name_plural = 'Города'
        verbose_name = 'Город'

    def __str__(self):
        return f'{self.name}'


class Promotion(models.Model):
    title_of_promotion = models.CharField(max_length=100, verbose_name='Название Акции')
    description = models.TextField(verbose_name='Описание Акции')
    date_start = models.DateField(verbose_name='Начало Акции')
    date_end = models.DateField(verbose_name='Конец Акции')
    image = models.ImageField(verbose_name='Картинка Акции', upload_to='promo/')
    city = models.ForeignKey('City', verbose_name='Город', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Акции'
        verbose_name = 'Акция'

    def __str__(self):
        return f'{self.title_of_promotion}'


class Service(models.Model):
    title_of_service = models.CharField(max_length=100, verbose_name='Сервисе')
    description = models.TextField(verbose_name='Описание Услуги')
    list_of_services = models.TextField(verbose_name='Список работ с вашим автомобилем')
    image = models.ImageField(verbose_name='Картинка Услуги', upload_to='service/')
    city = models.ForeignKey('City', verbose_name='Город', on_delete=models.CASCADE)
    longitude = models.CharField(max_length=50, verbose_name='Долгота')
    latitude = models.CharField(max_length=50, verbose_name='Широта')

    class Meta:
        verbose_name_plural = 'Сервисы'
        verbose_name = 'Сервис'

    def __str__(self):
        return f'{self.title_of_service}'


class Car(models.Model):
    pass

