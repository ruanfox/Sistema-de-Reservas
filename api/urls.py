from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views.users import UserViewSet
from api.views.tables import TableViewSet
from api.views.reservations import ReservationsViewset
router = DefaultRouter()

router.register(r'usuario', UserViewSet)
router.register(r'mesas', TableViewSet)
router.register(r'reservas', ReservationsViewset)

urlpatterns = [
    path('', include(router.urls)),
]
 