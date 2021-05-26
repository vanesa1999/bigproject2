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
from django.contrib.auth.models import User

from .models import  Punonjes, Departament, Departament_per_punonjes, Lejet, DitePushimi
from .serializers import  PunonjesSerializer, DepartamentSerializer, UserSerializer, \
    Departament_per_punonjesSerializer, LejetCreateSerializer, LejetViewSerializer, LejetViewHrSerializer, DitePushimiSerializer
from .permissions import IsOwner, IsHR, IsHRORIsOwner, IsOwnerLeje, IsOwnerDepartament
from .mixins import HrMixin
from rest_framework.generics import CreateAPIView, RetrieveDestroyAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView, DestroyAPIView

class PunonjesHrViewSet(HrMixin,ModelViewSet):
    serializer_class = PunonjesSerializer
    queryset = Punonjes.objects.all()
    permission_classes = (IsAuthenticated,IsHR,)

class PunonjesRetriveView(RetrieveAPIView):
    serializer_class = PunonjesSerializer
    queryset = Punonjes.objects.all()
    permission_classes = (IsOwner,IsAuthenticated)

class DepartamentHrViewSet(HrMixin,ModelViewSet):
    serializer_class = DepartamentSerializer
    queryset = Departament.objects.all()
    permission_classes = (IsAuthenticated, IsHR)

class DepartamentPerPunonjesHrViewSet(HrMixin,ModelViewSet):
    serializer_class = Departament_per_punonjesSerializer
    queryset = Departament_per_punonjes.objects.all()
    permission_classes = (IsAuthenticated, IsHR)

class DepartamentPerPunonjesRetriveView(RetrieveAPIView):
    serializer_class = Departament_per_punonjesSerializer
    queryset = Departament_per_punonjes.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerDepartament)

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

class LejetHrListView(HrMixin,ListAPIView):
    serializer_class = LejetViewSerializer
    queryset = Lejet.objects.filter(statusi= "Ne pritje")
    permission_classes = (IsAuthenticated, IsHR,)


class LejetRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = LejetViewHrSerializer
    queryset = Lejet.objects.all()
    permission_classes = (IsAuthenticated, IsHR,)
    lookup_field = 'id'

@api_view(["POST"])
def login(request):
    username= request.data.get("username")
    password= request.data.get("password")

    user= authenticate(username=username, password= password)
    if not user:
        return Response({"error": "Login failed"}, status= HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})

class UserViewSet(HrMixin, ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,IsHR)

class DitePushimiViewSet(HrMixin, ModelViewSet):
    serializer_class = DitePushimiSerializer
    queryset = DitePushimi.objects.all()
    permission_classes = (IsAuthenticated, IsHR)

class DitePushimiListView(ListAPIView):
    serializer_class = DitePushimiSerializer
    queryset = DitePushimi.objects.all()
