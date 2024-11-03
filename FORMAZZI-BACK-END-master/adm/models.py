
from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Administrador(models.Model):
    id = models.CharField(max_length=255, primary_key=True)  
    nome = models.CharField(max_length=255)
    empresa_pertencente = models.CharField(max_length=255)
    id_empresa_pertencente = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Hash a senha antes de salvar
        if self.password:
            self.password = make_password(self.password)
        super(Administrador, self).save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']  # Ordem padrão por username