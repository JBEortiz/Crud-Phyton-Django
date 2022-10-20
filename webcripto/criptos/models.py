from django.db import models

# Create your models here.
class Cripto(models.Model):
    id= models.AutoField(primary_key=True)
    icon = models.ImageField(max_length=100,verbose_name='icono')
    image= models.ImageField(upload_to='image/',verbose_name='imagen',null=True)
    name = models.CharField(max_length=100,verbose_name='nombre')
    sigle = models.CharField(max_length=100,verbose_name='siglas')
    unids = models.CharField(max_length=100,verbose_name='unidades',null=True)
    preci = models.CharField(max_length=100,verbose_name='precio')
    description = models.CharField(max_length=300,null=True,verbose_name='descripcion')
    codeFont = models.CharField(max_length=100,verbose_name='codigoFuente')
    web = models.CharField(max_length=100)
    
    
    def __str__(self):
        item = "Titulo :" +self.name
        return item