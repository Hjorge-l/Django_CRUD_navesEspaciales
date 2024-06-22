from django.db import models


# Create your models here.
class naveModel(models.Model):
    id_nave = models.AutoField(primary_key=True)
    nombre_nave = models.CharField(blank=True, max_length=20, default="")
    modelo_nave = models.CharField(blank=True, max_length=20, default="")
    coste_creditos_nave = models.IntegerField(blank=True, default=0)
    num_pasajeros_nave = models.IntegerField(blank=True, default=1)
