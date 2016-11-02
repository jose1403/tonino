from django.db import models
from PIL import Image
# Create your models here.
class DATOS_DE_LA_EMPRESA(models.Model):
	NOMBRE = models.CharField(max_length=100)
	NOMBRE_DEL_ENCARGADO= models.CharField(max_length=100)
	RIF= models.CharField(max_length=30)

	DIRECCION= models.TextField()
	TELEFONO= models.CharField(max_length=30)
	CELULAR= models.CharField(max_length=30)
	CODIGO_POSTAL=models.CharField(max_length=10)
	FAX= models.CharField(max_length=30, blank=True)
	LOGO= models.ImageField(upload_to='imagenes/empresa',default='/imagenes/empresa/logo.jpg')
															

	def __unicode__(self):
		return self.NOMBRE

"""a= DATOS_DE_LA_EMPRESA.objects.create(NOMBRE='Moliven', NOMBRE_DEL_ENCARGADO='Antonio',RIF='j38293',DIRECCION='av',TELEFONO='0304949',CELULAR='9877887',CODIGO_POSTAL='3303',FAX='233123')"""