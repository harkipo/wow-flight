from rest_framework import status, mixins
from rest_framework.response import Response
from .serializer import FlightSerializer
from .models import *
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView


def dictfetchall(cursor):  # Returns list of key value pairs from db
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def datetime_to_epoch(value):
    """
    Converts python datatime into epoch(unix) time
    """
    import time
    return int(time.mktime(value.timetuple())*1000)


def epoch_to_datetime(value):
    """
    Converts epoch(unix) time into python datatime
    """
    import datetime
    # return datetime.datetime.fromtimestamp(value)
    return datetime.datetime.fromtimestamp(value).strftime('%c')


class FlightViewSet(ModelViewSet):
    """
    API view to create , update and delete flights
    Method Allowed - POST , GET , PUT , PATCH , DELETE
    """
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class FlightSearchView(APIView):
    """
    API view for searching flights between 2 places
    Methods - POST
    """

    def post(self, request, format=None):
        try:
            import datetime
            data = request.data
            departure_city = data.get("departure_city")
            arrival_city = data.get("arrival_city")
            departure_time = data.get("departure_time")
            departure_time = datetime.datetime.strptime(
                departure_time, "%Y-%m-%dT%H:%M")
            departure_time_epoch = datetime_to_epoch(departure_time)

            """
            Fetch Direct flight plans
            """
            flight_plan_direct = Flight.objects.filter(
                departure_city__iexact=departure_city, arrival_city__iexact=arrival_city, departure_time__gte=departure_time_epoch)
            # print("direct >>",flight_plan_direct)
            flight_direct_serializer = FlightSerializer(
                flight_plan_direct, context={'request': request}, many=True)

            """
            Fetch connecting flight plans
            """
            from django.db import connection
            cursor = connection.cursor()
            query = f""" SELECT f1.number AS first_number , f1.departure_city AS first_departure_city ,f1.departure_time as first_departure_time ,f1.arrival_city AS first_arrival_city,f1.arrival_time as first_arrival_time ,f2.number AS second_number , f2.departure_city AS second_departure_city ,f2.departure_time as second_departure_time ,f2.arrival_city AS second_arrival_city,f2.arrival_time as second_arrival_time FROM `flight`f1 INNER JOIN flight f2 ON f1.arrival_city = f2.departure_city WHERE f1.arrival_time < f2.departure_time AND (f1.departure_city LIKE '{departure_city}' AND f2.arrival_city LIKE '{arrival_city}')  """
            cursor.execute(query)
            connecting_plans = dictfetchall(cursor)
            cursor.close()
            # print("connecting >>",connecting_plans)

            return Response({"direct_flight_plans": flight_direct_serializer.data, "connecting_flight_plans": connecting_plans})
        except Exception as e:
            print("exception >>",e)
            return Response({"direct_flight_plans": [], "connecting_flight_plans": []})

