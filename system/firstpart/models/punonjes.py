from django.db import models
from django.contrib.auth.models import User
class Punonjes (models.Model):
    Pozicionet= (
        ('HR' , 'HR'),
        ('Pergjegjes Departamenti', 'Pergjegjes Departamenti'),
        ('Punonjes Departamenti', 'Punonjes Departamenti'),
    )
    Gjinia= (
        ('Femer', 'Femer'),
        ('Mashkull', 'Mashkull'),
    )
    Statusi= (
        ('Aktiv', 'Aktiv'),
        ('Joaktiv', 'Joaktiv'),
    )
    username= models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    emer= models.CharField(max_length=100)
    mbiemer= models.CharField(max_length=100)
    data_e_fillimit= models.DateField()
    data_e_mbarimit= models.DateField(blank=True, default='')
    pozicioni= models.CharField(choices=Pozicionet, max_length=100)
    gjinia= models.CharField(choices=Gjinia, max_length=100)
    numri_i_telefonit= models.CharField(null=True, max_length=10)
    statusi= models.CharField(choices=Statusi, max_length=100)
    def __str__(self):
        return f'{self.emer} {self.mbiemer}'
