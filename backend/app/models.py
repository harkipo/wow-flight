from django.db import models


class Flight(models.Model):
    number = models.CharField(max_length=255, blank=True, null=True)
    departure_city = models.CharField(max_length=255, blank=True, null=True)
    departure_time = models.CharField(max_length=15, blank=True, null=True)
    arrival_city = models.CharField(max_length=255, blank=True, null=True)
    arrival_time = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.number

    class Meta:
        db_table = 'flight'
