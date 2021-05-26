from django.db import models
from .punonjes import Punonjes


class Departament(models.Model):
    Departamentet = (
        ('Financa', 'Financa'),
        ('Sekretaria','Sekretaria'),
        ('Administrata', 'Administrata'),
        ('IT', 'IT'),
        ('HR', "HR"),
    )
    pergjegjesi = models.OneToOneField(Punonjes, on_delete=models.CASCADE)
    titulli= models.CharField(choices= Departamentet, max_length=100)
    parent_departament= models.ForeignKey('Departament', null= True,on_delete=models.CASCADE)
    def __str__(self):
        return self.titulli

class Departament_per_punonjes(models.Model):
    punonjes= models.OneToOneField(Punonjes, on_delete=models.CASCADE)
    info= models.OneToOneField( Departament, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.punonjes} ne departamentin {self.info}'