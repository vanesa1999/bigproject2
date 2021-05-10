from django.db import models

class Dite_pushimi(models.Model):
    Pushimetzyrtare = (
        ('25.12.2021', '25.12.2021'),
        ('31.12.2021', '31.12.2021'),
        ('01.06.2021', '01.06.2021'),
    )
    pushimet_zyrtare= models.CharField(choices= Pushimetzyrtare, max_length=100)
    aprovuar= models.BooleanField(default=False)
    def __str__(self):
        return f'{self.pushimet_zyrtare} : {self.aprovuar}'