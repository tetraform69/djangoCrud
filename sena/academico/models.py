from django.db import models

vactivo = (
    (1, "Activo"),
    (2, "Inactivo")
)


class COORDINACION(models.Model):
    nom = models.TextField(verbose_name="Nombre de la coordinación")

    def __str__(self) -> str:
        return self.nom


class AREA(models.Model):
    nom = models.CharField(max_length=4, verbose_name="Nombre del area")
    descripcion = models.TextField()
    idcoordina = models.ForeignKey(
        COORDINACION, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nom


class TITULACION(models.Model):
    cod = models.IntegerField(verbose_name="codigo de la titulacion")
    nom = models.TextField()
    idarea = models.ForeignKey(
        AREA, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nom


class FICHA(models.Model):
    nom = models.TextField()
    estado = models.IntegerField(default=1, choices=vactivo)
    idtitulacion = models.ForeignKey(
        TITULACION, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nom


class NCL(models.Model):
    cod = models.TextField()
    nom = models.TextField()
    des = models.TextField()
    idtitulacion = models.ForeignKey(
        TITULACION, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nom


class RAP(models.Model):
    cod = models.TextField()
    nom = models.TextField()
    idncl = models.ForeignKey(
        NCL, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nom


class ACTIVIDAD(models.Model):
    nom = models.TextField()
    estado = models.IntegerField(default=1, choices=vactivo)
    horas = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.nom


class RAP_ACTIVIDAD(models.Model):
    idrap = models.ForeignKey(
        RAP, null=True, blank=True, on_delete=models.CASCADE)
    idactividad = models.ForeignKey(
        ACTIVIDAD, null=True, blank=True, on_delete=models.CASCADE)


class FICHAS_ACTIVIDAD(models.Model):
    idfichas = models.ForeignKey(
        FICHA, null=True, blank=True, on_delete=models.CASCADE)
    idactividad = models.ForeignKey(
        ACTIVIDAD, null=True, blank=True, on_delete=models.CASCADE)
