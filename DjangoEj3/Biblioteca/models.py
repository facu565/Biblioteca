from django.db import models

# Create your models here.

ESTADO_LIBRO= [
        ('DP', 'Disponible'),
        ('PS', 'Prestado'),
        ('RE', 'Reservado'),
        ('ND', 'No Disponible'),
    ]

class Persona(models.Model):
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    correo = models.CharField(max_length = 50)
    telefono = models.CharField(max_length = 50)
    numLibros = models.IntegerField()
    adeudo = models.FloatField()
    def __str__(self):
        return "{} {}".format(self.nombre,self.apellido)

class Alumno(Persona):
    matricula = models.IntegerField()

class Profesor(Persona):
    numEmpleado = models.IntegerField()

class Material(models.Model):
    codigo = models.CharField(max_length = 50)
    autor = models.CharField(max_length = 50)
    titulo = models.CharField(max_length = 50)
    year = models.IntegerField()
    status = models.CharField(max_length=2, choices=ESTADO_LIBRO, )
    def __str__(self):
        return self.titulo

class Libro(Material):
    nombre = models.CharField(max_length = 50)
    def __str__(self):
        return self.nombre

class Revista(Material):
    pass

class Prestamo(models.Model):
    codigo = models.CharField(max_length = 50)
    fechaSalida = models.DateField(auto_now=False)
    fechaRegreso = models.DateField(auto_now=False)
    persona = models.ForeignKey('Persona',on_delete=models.CASCADE,null=False)
    material = models.ForeignKey('Material',on_delete=models.CASCADE,null=False)
    def __str__(self):
        return self.codigo
