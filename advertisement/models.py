from django.db import models

class Anuncio(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='./', null=True, blank=True)
    imagen_url = models.URLField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        if self.imagen:
            self.imagen_url = self.imagen.url
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo
