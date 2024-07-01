from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    correo = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    usuario = models.CharField(max_length=14, blank=True, null=True)
    contraseña = models.CharField(max_length=16, blank=True, null=True)

    def __str__(self):
        return str(self.usuario)
    
class Comentar(models.Model):
    comentario = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.comentario)[:50]  # Muestra los primeros 50 caracteres del comentario
