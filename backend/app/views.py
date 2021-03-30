from rest_framework import status, mixins
from rest_framework.response import Response
from .serializer import FlightSerializer
from .models import *
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView

class FlightViewSet(ModelViewSet):
    """
    API view to create new flights
    Method Allowed - POST 
    """
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer



