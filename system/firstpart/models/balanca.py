from django.db import  models
from .punonjes import Punonjes
from .lejet import Lejet

class Balanca(models.Model):
    lloji_i_lejes= models.CharField(choices=Lejet.Llojet_e_lejeve, max_length=100)
    nga= models.DateTimeField()
    ne=models.DateTimeField()
    punonjes= models.OneToOneField(Punonjes, on_delete=models.CASCADE)
    totali_i_oreve_te_perdorshme= models.PositiveIntegerField(default=0)
    totali_i_lejeve_te_marra= models.PositiveIntegerField(default=0)