from rest_framework import serializers

from .models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('date', 'time_start', 'time_end', 'phone_number', 'email', 'name', 'count_people', 'comment')
