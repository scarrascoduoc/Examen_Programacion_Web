from django.db import models

# Create your models here.
class Formulario(models.Model):
    Rut = models.IntegerField(primary_key=True, verbose_name='Rut')
    Nombre = models.CharField(max_length=100, verbose_name='Nombre')
    Correo = models.CharField(max_length=100, verbose_name='Correo')
    Telefono = models.IntegerField(verbose_name='Telefono')
    Region = models.CharField(max_length=100, verbose_name='Region')
    Comuna = models.CharField(max_length=100, verbose_name='Comuna')
    
    def __str__(self):
        return self.Rut
class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='id Producto')
    NombreProducto = models.CharField(max_length=100, verbose_name='Nombre Producto')
    ValorProducto = models.IntegerField(verbose_name='Valor Producto')
    CategoriaProducto = models.IntegerField(verbose_name='Categoria Producto')
    StockProducto = models.IntegerField(verbose_name='Stock Producto')
    
    def __str__(self):
        return self.NombreProducto

class Login(models.Model):
    usuario = models.CharField(primary_key=True,max_length=100, verbose_name='Usuario')
    password = models.CharField(max_length=100, verbose_name='Password')

    def __str__(self):
        return self.usuario

class Donaciones(models.Model):
    nombre = models.CharField(max_length=20)
    apellido_pat = models.CharField(max_length=50)
    apellido_mat = models.CharField(max_length=50)
    montos = models.IntegerField(choices=[(1000,'1000'),
         (5000,'5000'),
         (10000,'10000'),
         (20000,'20000')],null=True)
    monto = models.CharField(max_length=10, blank=True)
    
    def __str__(self):
        return self.nombre

class Cuenta(models.Model):
    usuario = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    contrasena = models.CharField(max_length=20)
    
    def __str__(self):
        return self.usuario