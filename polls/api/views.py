from django.shortcuts import get_list_or_404 , render  , get_object_or_404
from django.http import Http404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from vote.models import (
                         County,
                         Country ,
                         Constituency ,
                         Ward ,
                         President ,
                         Governor,
                         Senator ,
                         Womensrep ,
                         Memberofparliament ,
                         MemberofCountyAssembly,
                         RallyDate,
                         Party,
                         )
from api.serializers import (
                             CountySerializer,
                             CountrySerializer,
                             ConstituencySerializer,
                             WardSerializer,
                             PresidentSerializer,
                             GovernorSerializer,
                             SenatorSerializer,
                             WomensrepSerializer,
                             MemberofparliamentSerializer,
                             MemberofCountyAssemblySerializer,
                             RallyDateSerializer,
                             PartySerializer,
                            )

class PartyList(generics.ListAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer

class RallyDateList(generics.ListAPIView):
    queryset = RallyDate.objects.all()
    serializer_class = RallyDateSerializer

class PresidentList(generics.ListAPIView):
    queryset = President.objects.all()
    serializer_class = PresidentSerializer


class PresidentDetail(generics.ListAPIView):
    serializer_class = PresidentSerializer

    def get_queryset(self): #override the get queryset method.and return the queryset you want
        country = self.kwargs['country'] #filtering agianst the url kwargs
        return President.objects.filter(Country__Name__contains = country)


class GovernorList(generics.ListAPIView):
    serializer_class = GovernorSerializer
    queryset = Governor.objects.all()

class GovernorDetail(generics.ListAPIView):
    serializer_class = GovernorSerializer

    def get_queryset(self):
        county = self.kwargs['county']
        return Governor.objects.filter(County__Name__contains = county)

class SenatorList(generics.ListAPIView):
    serializer_class = SenatorSerializer
    queryset = Senator.objects.all()

class SenatorDetail(generics.ListAPIView):
    serializer_class = SenatorSerializer

    def get_queryset(self):
        county = self.kwargs['county']
        return Senator.objects.filter(County__Name__contains = county)

class WomenrepsList(generics.ListAPIView):
    serializer_class = WomensrepSerializer
    queryset = Womensrep.objects.all()

class WomenrepsDetail(generics.ListAPIView):
    serializer_class = WomensrepSerializer

    def get_queryset(self):
        county = self.kwargs['county']
        return Womensrep.objects.filter(County__Name__contains = county)

class ConstituencyList(generics.ListAPIView):
    serializer_class = ConstituencySerializer

    def get_queryset(self):
        county = self.kwargs['county']
        return Constituency.objects.filter(County__Name__contains = county)
