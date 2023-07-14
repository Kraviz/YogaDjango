from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Producto(models.Model):
    id = models.BigAutoField (primary_key = True)
    img = models.ImageField(verbose_name="imagen", upload_to="productos", default="", blank=True, null=True)
    titulo = models.CharField(max_length=50, verbose_name='Nombre')
    descripcion = models.CharField(verbose_name='Descripcion', max_length=40, default="")
    stock = models.IntegerField(verbose_name='Stock')
    precio = models.IntegerField(verbose_name='Precio')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creción') 
    updated_at = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de actualización')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['created_at']
    
    def __str__(self):
        return self.titulo
    

class Contacto(models.Model):
    id= models.BigAutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    telefono = models.IntegerField(verbose_name='Telefono')
    correo = models.EmailField(verbose_name='Correo electronico')
    asunto = models.CharField(max_length=50, verbose_name='Asunto')
    comentarios = models.TextField(max_length=300, verbose_name='Comentarios')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creacion')

    def __str__(self):
        return self.asunto + ' - ' + self.user.username
                                   
