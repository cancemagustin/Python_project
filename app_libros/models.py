from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, choices=[('borrador', 'Borrador'), ('publicado', 'Publicado')], default='borrador')

    def __str__(self):
        return self.titulo