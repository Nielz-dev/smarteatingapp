from django.db import models
from usuarios.models import UserAccount
import random
from django.utils import timezone
from django.db import models

def generate_random_foto_perfil():
    opciones = [
        'https://cdn.pixabay.com/photo/2017/03/23/19/57/asparagus-2169305_1280.jpg',
        'https://images.pexels.com/photos/9295693/pexels-photo-9295693.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
        'https://img.freepik.com/foto-gratis/mano-cultivo-cortando-carne-ahumada-cerca-variedad-alimentos_23-2147930226.jpg?w=826&t=st=1685472208~exp=1685472808~hmac=60cd6297b2d1e5fe8012eb1343f36013606aa39a9f43f77369e57116db734796',
        'https://img.freepik.com/foto-gratis/penne-pasta-salsa-tomate-pollo-tomates-mesa-madera_2829-19739.jpg?w=1380&t=st=1685472240~exp=1685472840~hmac=c993dd25db6b3459a8de2f166fcd83faee6b95e5f6aa9e67c5e8c97814d363f4'
        
    ]
    return random.choice(opciones)

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.CharField(max_length=50)
    tipo_peso = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    

class Plato(models.Model):
    usuario = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    foto_perfil = models.URLField(default=generate_random_foto_perfil,max_length=350)
    ingredientes = models.ManyToManyField(Ingrediente, blank=True)

    def __str__(self):
        return self.nombre

  