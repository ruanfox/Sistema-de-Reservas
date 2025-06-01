from django.db import models
from .tables import Table
from .users import User

class Reservation(models.Model):
    STATUS_CHOICHES = [
        ("ATIVO", "ativo"),
        ("CANCELADO", "cancelado")
    ]
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    mesa_id = models.ForeignKey(Table, on_delete=models.CASCADE)
    data_reserva = models.DateTimeField(null=False, blank=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICHES)

    def __str__(self):
        return f"Reserva {self.data_reserva}"