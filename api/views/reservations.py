from rest_framework import viewsets
from api.models.reservations import Reservation
from api.serializers.reservations import ReservationSerializer

class ReservationsViewset(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer