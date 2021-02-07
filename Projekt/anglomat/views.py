from django.contrib.auth.models import User
import django_filters
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Klient, Auto, Naprawa
from .serializers import *


class KlientList(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    search_fields = ['Imie', 'Nazwisko']
    filterset_fields = ['Imie', 'Nazwisko']
    ordering_fields = ['Imie', 'Nazwisko']
    name = 'klient-list'


class KlientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = KlientSerializer
    name = 'klient-detail'


class NaprawaFilter(django_filters.FilterSet):
    from_DataZlecenia = django_filters.DateFilter(field_name='DataZlecenia', lookup_expr='gte')
    to_DataZlecenia = django_filters.DateFilter(field_name='DataZlecenia', lookup_expr='lte')

    class Meta:
        model = Naprawa
        fields = ['from_DataZlecenia', 'to_DataZlecenia']


class AutoList(generics.ListCreateAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    search_fields = ['NrRejestracyjny']
    filterset_fields = ['NrRejestracyjny']
    ordering_fields = ['NrRejestracyjny']
    name = 'auto-list'


class AutoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    name = 'auto-detail'
    filter_fields = ['NrRejestracyjny']
    search_fields = ['NrRejestracyjny']
    ordering_fields = ['NrRejestracyjny']


class NaprawaList(generics.ListCreateAPIView):
    queryset = Naprawa.objects.all()
    serializer_class = NaprawaSerializer
    name = 'naprawa-list'
    filter_fields = ['DataZlecenia']
    search_fields = ['DataZlecenia']
    ordering_fields = ['DataZlecenia']


# def perform_create(self, serializer):
# serializer.save(owner=self.request.user)

class NaprawaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Naprawa.objects.all()
    serializer_class = NaprawaSerializer
    name = 'naprawa-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'klienci': reverse(KlientList.name, request=request),
                         'auta': reverse(AutoList.name, request=request),
                         'naprawy': reverse(NaprawaList.name, request=request)
                         })
