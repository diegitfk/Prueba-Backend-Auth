from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# En vista del contexto un producto de una veterinaria no puede ser medicamente y accesorio a la vez
# o alimento y accesorio, por ende un producto puede estar asociado a una categoria, y una categoria, puede
# estas asociada a muchos productos por ende hay una relacion de uno a mucho de Categoria a Producto
# Categoria --- 1 : N --> Producto
# ------------------------------------------------------------------
class Categoria(models.Model):
    id = models.BigAutoField(primary_key=True , null=False)
    nombre = models.CharField(max_length=30 , null=False)
    descripcion = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.nombre

class Producto(models.Model):
    id = models.BigAutoField(primary_key=True , null=False)
    nombre = models.CharField(max_length=40 , null=False)
    descripcion = models.CharField(max_length=150 , null=True)
    precio = models.FloatField(null=False)
    categoria = models.ForeignKey(Categoria , on_delete=models.CASCADE , related_name="productos") # Id de la categoria a la que pertenece el producto
    creado_por = models.ForeignKey(User , on_delete=models.CASCADE , related_name="productos_creados") #Id del usuario que creo el producto
