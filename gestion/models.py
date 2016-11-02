from django.db import models

class Plantas(models.Model):
	nombre= models.CharField(max_length=100)
	cantidad_silos=models.IntegerField()
	descripcion= models.TextField()
	null = models.BooleanField(default=False)


class Silos(models.Model):
	plantas= models.ForeignKey(Plantas)
	nombre= models.CharField(max_length=100)
	capacidad = models.FloatField()
	descripcion= models.TextField()
	null = models.BooleanField(default=False)
	
