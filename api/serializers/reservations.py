from rest_framework import serializers
from api.models.reservations import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

    def create(self, validated_data):
        reservation = Reservation(**validated_data)
        reservation.save()
        return reservation