from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.permissions import IsAuthenticated

from .models import  Punonjes, Departament, Departament_per_punonjes, Lejet
from .serializers import  PunonjesSerializer, DepartamentSerializer, UserSerializer, \
    Departament_per_punonjesSerializer, LejetCreateSerializer, LejetViewSerializer, LejetViewSerializerA
from .permissions import IsOwner, IsHR, IsHRORIsOwner, IsOwnerLeje

from rest_framework.generics import CreateAPIView, RetrieveDestroyAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView, DestroyAPIView

class PunonjesViewSet(ModelViewSet):
    serializer_class = PunonjesSerializer
    queryset = Punonjes.objects.all()
    permission_classes = (IsAuthenticated)

class DepartamentViewSet(ModelViewSet):
    serializer_class = DepartamentSerializer
    queryset = Departament.objects.all()
    permission_classes = (IsAuthenticated, IsHR)

class Departament_per_punonjesViewSet(ModelViewSet):
    serializer_class = Departament_per_punonjesSerializer
    queryset = Departament_per_punonjes.objects.all()
    permission_classes = (IsAuthenticated, IsHRORIsOwner)

class LejetCreateView(CreateAPIView):
    serializer_class = LejetCreateSerializer
    queryset = Lejet.objects.all()
    permission_classes = (IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save(punonjes= Punonjes.objects.get(username= self.request.user), statusi= 'Ne pritje')

class LejetRetrieveView(RetrieveAPIView):
    serializer_class = LejetViewSerializer
    queryset = Lejet.objects.all()
    permission_classes = (IsAuthenticated,IsOwnerLeje)
    lookup_field = 'id'

class LejetDestroyView(DestroyAPIView):
    serializer_class = LejetViewSerializer
    queryset = Lejet.objects.filter(statusi= "Ne pritje")
    permission_classes = (IsAuthenticated,IsOwnerLeje)
    lookup_field = 'id'

class LejetListView(ListAPIView):
    serializer_class = LejetViewSerializer
    #queryset = Lejet.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        x=self.request.user
        punonjes= Punonjes.objects.get(username= x)
        queryset = Lejet.objects.filter(punonjes=punonjes)
        return queryset

class LejetListViewA(ListAPIView):
    serializer_class = LejetViewSerializer
    queryset = Lejet.objects.filter(statusi= "Ne pritje")
    permission_classes = (IsAuthenticated, IsHR,)


class LejetRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = LejetViewSerializerA
    queryset = Lejet.objects.all()
    permission_classes = (IsAuthenticated, IsHR,)
    lookup_field = 'id'
