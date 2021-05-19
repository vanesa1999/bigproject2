from rest_framework import  serializers
from django.contrib.auth.models import User
from .models import Punonjes,Departament, Departament_per_punonjes,Dite_pushimi,Balanca

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class PunonjesSerializer(serializers.ModelSerializer):
    User = serializers.PrimaryKeyRelatedField()
    class Meta:
        model= Punonjes
        fields= ['emer', 'mbiemer', 'data_e_fillimit', 'data_e_mbarimit','pozicioni', 'gjinia', 'numri_i_telefonit', 'statusi', 'username']
        depth=   1


class DepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Departament
        fields= ['titulli', 'Nendepartamenti', 'Mbidepartamenti', 'pergjegjesi']
        depth= 2


