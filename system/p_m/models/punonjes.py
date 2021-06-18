from django.db import models
from django.contrib.auth.models import User

class Pozicionet (models.Model):
    id= models.IntegerField(primary_key=True, editable=False)
    Pozicionet= (
        ('HR' , 'HR'),
        ('Pergjegjes Departamenti', 'Pergjegjes Departamenti'),
        ('Punonjes Departamenti', 'Punonjes Departamenti'),
    )
    pozicioni = models.CharField(choices=Pozicionet, max_length=100)


class Punonjes (models.Model):
    Gjinia= (
        ('Femer', 'Femer'),
        ('Mashkull', 'Mashkull'),
    )
    Statusi= (
        ('Aktiv', 'Aktiv'),
        ('Joaktiv', 'Joaktiv'),
    )

    username= models.OneToOneField(User,null=True, on_delete=models.SET_NULL)
    emer= models.CharField(max_length=100)
    mbiemer= models.CharField(max_length=100)
    pozicioni= models.ManyToManyField(Pozicionet)
    data_e_fillimit= models.DateField(null= True)
    data_e_mbarimit= models.DateField(null=True)
    gjinia= models.CharField(choices=Gjinia, max_length=100)
    numri_i_telefonit= models.CharField(null=True, max_length=10)
    statusi= models.CharField(choices=Statusi, max_length=100)
    departamenti = models.ForeignKey('Departament', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.emer} {self.mbiemer}'
