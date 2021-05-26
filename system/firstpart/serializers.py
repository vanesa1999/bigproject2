from rest_framework import  serializers
from django.contrib.auth.models import User
from .models import Punonjes,Departament, Departament_per_punonjes,DitePushimi ,Balanca, Lejet
from rest_framework.response import Response
from django.contrib.auth.models import Group

class PunonjesSerializer(serializers.ModelSerializer):
    #username1= serializers.SerializerMethodField('get_username_from_user')
    class Meta:
        model= Punonjes
        fields = "__all__"
    #def get_username_from_user(self, punonjes):
        #username1= punonjes.username.username
        #return username1

class DepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Departament
        fields= '__all__'


class Departament_per_punonjesSerializer(serializers.ModelSerializer):
    titulli= serializers.SerializerMethodField('get_titulli_from_departament')
    pergjegjesi= serializers.SerializerMethodField('get_pergjegjesi_from_departament')
    class Meta:
        model= Departament_per_punonjes
        fields= ['punonjes', 'info', 'titulli', 'pergjegjesi']
    def get_titulli_from_departament(self, departament_per_punonjes):
        titulli= departament_per_punonjes.info.titulli
        return titulli
    def get_pergjegjesi_from_departament(self, departament_per_punonjes):
        pergjegjesi= departament_per_punonjes.info.pergjegjesi.__str__()
        return pergjegjesi

class LejetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Lejet
        fields= ['data_e_kerkeses', 'lloji_i_lejes', 'fillimi', 'mbarimi', 'arsyetimi']

class LejetViewSerializer(serializers.ModelSerializer):
    class Meta:
        model= Lejet
        fields= '__all__'


class LejetViewHrSerializer(serializers.ModelSerializer):
    class Meta:
        model= Lejet
        fields= '__all__'
        extra_kwargs = {'data_e_kerkeses': {'read_only': True},
                        'lloji_i_lejes': {'read_only': True},
                        'fillimi': {'read_only': True},
                        'mbarimi': {'read_only': True},
                        'punonjes': {'read_only': True},
                        'id': {'read_only': True},}


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ['username', 'email', 'password', 'id']

class DitePushimiSerializer(serializers.ModelSerializer):
    class Meta:
        model= DitePushimi
        fields= '__all__'
