from django.db import models
from django.core.urlresolvers import reverse

class Plantas(models.Model):
	nombre= models.CharField(max_length=100, unique=True)
	cantidad_silos=models.IntegerField()
	descripcion= models.TextField()
	null = models.BooleanField(default=False)

	def __unicode__(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse('plantas.views.Edit_Plantas', args=[str(self.id)])

class Silos(models.Model):
	plantas= models.ForeignKey(Plantas)
	nombre= models.CharField(max_length=100)
	capacidad = models.FloatField()
	en_inventario= models.FloatField(default=0)
	resto= models.FloatField(default=0)
	descripcion= models.TextField()
	null = models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.nombre
	def get_absolute_url(self):
		return reverse('plantas.views.Edit_Silos', args=[str(self.plantas.id),str(self.id)])
