from .models import Flight
from rest_framework import serializers

# class UnixEpochDateField(serializers.DateTimeField):
#     def to_representation(self, value):
#         """ Return epoch time for a datetime object or ``None``"""
#         import time
#         try:
#             return int(time.mktime(value.timetuple()))
#         except (AttributeError, TypeError):
#             return None

#     def to_internal_value(self, value):
#         import datetime
#         return datetime.datetime.fromtimestamp(int(value))


class FlightSerializer(serializers.ModelSerializer):
    """
    Serializer class for Ingredients Model
    """
    class Meta:
        model = Flight
        # departure_time  = UnixEpochDateField(source='departure_time')
        # arrival_time  = UnixEpochDateField(source='arrival_time')
        fields = '__all__'


# def datetime_to_epoch(value):
#     import time
#     return int(time.mktime(value.timetuple())*1000)

# def epoch_to_datetime(value):
#     import datetime
#     return datetime.datetime.fromtimestamp(value)
#     return datetime.datetime.fromtimestamp(value).strftime('%c')

