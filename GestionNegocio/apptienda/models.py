from django.db import models


# Create your models here.
class Categoria(models.Model):
    nombreCat = models.CharField(max_length=50, unique=True)
    
    def __str__(self) -> str:
        return self.nombreCat


class Producto(models.Model):
    codigoPro = models.IntegerField(unique=True)
    nombrePro = models.CharField(max_length=50)
    precioPro = models.IntegerField()
    categoriaPro = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    fotoPro = models.FileField(upload_to="fotos/", null=True, blank=True)

    def __str__(self) -> str:
        return self.nombrePro