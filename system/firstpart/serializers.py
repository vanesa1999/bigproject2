from rest_framework import  serializers
from django.contrib.auth.models import User
from .models import Punonjes,Departament, Departament_per_punonjes,Dite_pushimi,Balanca, Lejet


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


class LejetViewSerializerA(serializers.ModelSerializer):
    class Meta:
        model= Lejet
        fields= '__all__'
        extra_kwargs = {'data_e_kerkeses': {'read_only': True},
                        'lloji_i_lejes': {'read_only': True},
                        'fillimi': {'read_only': True},
                        'mbarimi': {'read_only': True},
                        'arsyetimi': {'read_only': True},
                        'punonjes': {'read_only': True},
                        'id': {'read_only': True},}

class UserSerializer(serializers.ModelSerializer):
    punonjes= PunonjesSerializer(many= True)
    password2 = serializers.CharField(style= {'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'punonjes']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def save(self):
        user = User(
            email= self.validated_data['email'],
            username= self.validated_data['username'],

        )
        password= self.validated_data['password']
        password2= self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        user.set_password(password)
        user.save()

        return user
    def create (self):
        punonjes_data = self.validated_data.pop('punonjes')
        validated_data= self.validated_data
        user= User.objects.create(**validated_data)
        Punonjes.objects.create(username=user, **punonjes_data)
        return user




