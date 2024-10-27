from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..models import Airline
from ..serializers import AirlineSerializer


#AİRLİNES Concrete View Classes
class AirlineListCreateView(generics.ListCreateAPIView):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer
    permission_classes = (IsAuthenticated,)


class AirlineListView(generics.ListAPIView):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer
    permission_classes = (IsAuthenticated,)


class AirlineRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer
    permission_classes = (IsAuthenticated,)
