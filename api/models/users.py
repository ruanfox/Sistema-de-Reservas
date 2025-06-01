from django.db import models

class User(models.Model):
    TIPO_CHOICES = [
        ("CLIENTE", "cliente"),
        ("ADMINISTRADOR", "administrador"),
    ]
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null= False)
    senha = models.CharField(max_length=128)
    role = models.CharField(max_length=50, choices=TIPO_CHOICES)

    def __str__(self):
        return f"Usuario {self.nome}"
    