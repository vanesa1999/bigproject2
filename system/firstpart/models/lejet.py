from django.db import models
from .punonjes import Punonjes
import uuid
class Lejet (models.Model):
    Llojet_e_lejeve = (
        ('Leje e paguar','Leje e paguar'),
        ('Leje e papaguar', 'Leje e papaguar'),
    )
    Statusi_i_lejes = (
        ('Ne pritje', 'Ne pritje'),
        ('Pranuar', 'Pranuar'),
        ('Anulluar', 'Anulluar'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data_e_kerkeses= models.DateTimeField(auto_now_add=True)
    lloji_i_lejes= models.CharField(choices= Llojet_e_lejeve, max_length=100)
    fillimi= models.DateTimeField()
    mbarimi= models.DateTimeField()
    statusi= models.CharField(choices=Statusi_i_lejes, max_length=100)
    arsyetimi= models.TextField()
    punonjes= models.ForeignKey(Punonjes, on_delete=models.CASCADE)

    class Meta:
        ordering = ['data_e_kerkeses']

    def __str__(self):
        return f' {self.punonjes} kerkesa e dates {self.data_e_kerkeses} : {self.statusi}'