from .models import Flight
from rest_framework import serializers


class FlightSerializer(serializers.ModelSerializer):
    """
    Serializer class for Flights Model
    """
    class Meta:
        model = Flight
        fields = '__all__'
