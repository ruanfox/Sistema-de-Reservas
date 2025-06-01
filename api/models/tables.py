from django.db import models

class Table(models.Model):
    STATUS_CHOICHES = [
        ("DISPONIVEL", "disponivel"),
        ("RESERVADA", "reservada"),
        ("INATIVA", "inativa"),
    ]

    nome = models.CharField(max_length=255)
    capacidade = models.IntegerField()
    status = models.CharField(max_length=25, choices=STATUS_CHOICHES)

    def __str__(self):
        return f"Mesa {self.nome}"