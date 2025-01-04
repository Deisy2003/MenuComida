from django.db import models
from django.utils import timezone

# Create your models here.

class Platillo (models.Model):

    TIPOS_PLATILLOS = [
        ('Sopa', 'Sopa'),
        ('Segundo', 'Segundo'),
        ('Bebida', 'Bebida'),
        ('Postre', 'Postre'),
        ('Otro', 'Otro'),
    ]

    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPOS_PLATILLOS, default='otro')
    is_hidden = models.BooleanField(default=False)


    precio = models.DecimalField(max_digits=6, decimal_places=2)
    
    informacion_nutricional = models.TextField()
    fecha_disponible = models.DateField()
    foto_platillo=models.ImageField( upload_to='fotos_platillo/', null=True, blank=True) 


    def __str__(self):
        return self.nombre



class Calificacion(models.Model):
    platillo = models.ForeignKey(Platillo, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=100)
    calificacion = models.IntegerField(choices=[(1, '1 estrella'), (2, '2 estrellas'), (3, '3 estrellas'), (4, '4 estrellas'), (5, '5 estrellas')])
    comentario = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Calificación de {self.usuario} para {self.platillo.nombre}"