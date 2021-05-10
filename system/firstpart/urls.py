from django.db import models
from django.contrib.auth.models import User
Pozicionet= ['HR', 'Pergjegjes Departamenti', 'Punonjes Departamenti']
Gjinia= ['Femer', 'MAshkull']
Status= ['Aktiv', 'Joaktiv']

class Punonjes(models.Model):
    username= models.OneToOneField(User, null= True, on_delete=models.SET_NULL )
    emer= models.CharField(max_length=100)
    mbiemer= models.CharField(max_length=100)
    data_e_fillimit= models.DateField()
    data_e_mbarimit= models.DateField( blank=True)
    pozicioni= models.CharField(choices=Pozicionet, max_length=100)
    gjinia= models.CharField(choices=Gjinia, max_length=100)
    numri_i_telefonit= models.CharField(blank=True, default='', max_length=10)
    statusi= models.CharField(choices=Status, max_length=100)

