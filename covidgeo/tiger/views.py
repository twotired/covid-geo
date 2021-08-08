from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response

from .models import *
from .serializers import *

FILTERS = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

# Create your views here.
class StateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows states to be viewed or edited.
    """
    queryset = State.objects.all().order_by('name')
    serializer_class = StateSerializer
    filter_backends = FILTERS
    filterset_fields = ['division']
    search_fields = ['name']

    def retrieve(self, request, pk=None):
        queryset = State.objects.all().order_by('name')
        state = get_object_or_404(queryset, pk=pk)
        serializer = StateDetailSerializer(state, context={'request': request})
        return Response(serializer.data)


class CountyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows counties to be viewed or edited.
    """
    queryset = County.objects.all().order_by('name')
    serializer_class = CountySerializer
    filter_backends = FILTERS
    filterset_fields = ['statefp']
    search_fields = ['namelsad']

    def retrieve(self, request, pk=None):
        queryset = County.objects.all().order_by('name')
        county = get_object_or_404(queryset, pk=pk)
        serializer = CountyDetailSerializer(county, context={'request': request})
        return Response(serializer.data)


class UrbanAreaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows urban areas to be viewed or edited.
    """
    queryset = UrbanArea.objects.all().order_by('name10')
    serializer_class = UrbanAreaSerializer
    filter_backends = FILTERS
    filterset_fields = ['funcstat10']
    search_fields = ['name10']

    def retrieve(self, request, pk=None):
        queryset = UrbanArea.objects.all().order_by('name10')
        obj = get_object_or_404(queryset, pk=pk)
        serializer = UrbanAreaDetailSerializer(obj, context={'request': request})
        return Response(serializer.data)

class CongressionalDistrictViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows congressional districts to be viewed or edited.
    """
    queryset = CongressionalDistrict.objects.all().order_by('namelsad')
    serializer_class = CongressionalDistrictSerializer
    filter_backends = FILTERS
    filterset_fields = ['statefp']
    search_fields = ['namelsad']

    def retrieve(self, request, pk=None):
        queryset = CongressionalDistrict.objects.all().order_by('namelsad')
        cd = get_object_or_404(queryset, pk=pk)
        serializer = CongressionalDistrictDetailSerializer(cd, context={'request': request})
        return Response(serializer.data)
