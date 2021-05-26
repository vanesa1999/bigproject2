from django.db import models

class DitePushimi(models.Model):
    Statusi = (
        ('Aktive', 'Aktive'),
        ('Joaktive', 'Joaktive'),
    )
    data = models.DateField()
    emri_i_festes = models.CharField(max_length=200)
    statusi = models.CharField(choices=Statusi, max_length=200)

    def __str__(self):
        return f'{self.emri_i_festes} : {self.data} {self.satusi}'
