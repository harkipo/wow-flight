from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('view-flight/all/',csrf_exempt(FlightViewSet.as_view({'get': 'list'})) , name='get_all_flight'),
    path('view-flight/<int:pk>/',csrf_exempt(FlightViewSet.as_view({'get': 'retrieve'})) , name='get_flight'),
    path('create-flight/',csrf_exempt(FlightViewSet.as_view({'post': 'create'})) , name='create_flight'),
    path('update-flight/<int:pk>/',csrf_exempt(FlightViewSet.as_view({'put': 'update','patch':'partial_update'})) , name='update_flight'),
    path('delete-flight/<int:pk>/',csrf_exempt(FlightViewSet.as_view({'delete': 'destroy'})) , name='delete_flight'),
    
]
