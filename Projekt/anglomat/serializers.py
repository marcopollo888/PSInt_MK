from rest_framework import serializers
from .views import *
from .models import *


class KlientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Klient
        fields = ['PESEL', 'Imie', 'Nazwisko', 'Telefon']


class AutoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Auto
        fields = ['NrRejestracyjny', 'Marka', 'Model', 'VIN', 'DataPierwszejRejestracji']


class NaprawaSerializer(serializers.HyperlinkedModelSerializer):
    IdKlienta = serializers.SlugRelatedField(queryset=Klient.objects.all(), slug_field='PESEL')
    IdAuta = serializers.SlugRelatedField(queryset=Auto.objects.all(), slug_field='NrRejestracyjny')

    class Meta:
        model = Naprawa
        fields = ['IdKlienta', 'IdAuta', 'Cena', 'DataZlecenia']
