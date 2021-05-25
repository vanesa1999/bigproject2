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

@api_view(["POST"])
def login(request):
    username= request.data.get("username")
    password= request.data.get("password")

    user= authenticate(username=username, password= password)
    if not user:
        return Response({"error": "Login failed"}, status= HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})




@api_view (['GET', ])
def punonjes_detail_view (request, pk):
    try:
        punonjes= Punonjes.objects.get(pk=pk)
    except Punonjes.DoesNotExist:
        return Response (status= status.HTTP_404_NOT_FOUND)


    if request.method == "GET":
        serializer= PunonjesSerializer( punonjes)
        return  Response(serializer.data)

@api_view(['PUT',])
def punonjes_update_view( request, pk):
    try:
        punonjes= Punonjes.objects.get(pk=pk)
    except Punonjes.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer= PunonjesSerializer(punonjes, data= request.data)
        data= {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response (data= data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE',])
def punonjes_delete_view( request, pk):
    try:
        punonjes= Punonjes.objects.get(pk=pk)
    except Punonjes.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation= punonjes.delete()
        data= {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"]= "delete failed"
        return Response(data=data)

@api_view(['POST'],)
def punonjes_create_view(request):
    if request.method == "POST":
        serializer= PunonjesSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


@api_view (['GET', ])
def departament_detail_view (request, pk):
    try:
        departament= Departament.objects.get(pk=pk)
    except Departament.DoesNotExist:
        return Response (status= status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer= DepartamentSerializer( departament)
        return  Response(serializer.data)

@api_view(['PUT',])
def departament_update_view( request, pk):
    try:
        departament= Departament.objects.get(pk=pk)
    except Departament.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer= DepartamentSerializer(departament, data= request.data)
        data= {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response (data= data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'],)
def departament_create_view(request):
    if request.method == "POST":
        serializer= DepartamentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'],)
def user_create_view(request):
    if request.method == "POST":
        serializer= UserSerializer(data= request.data)
        data= {}
        if serializer.is_valid():
            serializer.create(request.data)
            data['response']= "successfully registered new user"

        else:
            data= serializer.errors
        return Response(data)
