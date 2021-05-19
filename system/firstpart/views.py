from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import  Punonjes, Departament
from .serializers import  PunonjesSerializer, DepartamentSerializer

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
