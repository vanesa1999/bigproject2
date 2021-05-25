from rest_framework import permissions
from .models import Punonjes
from django.contrib.auth.models import User
class IsHR(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        x= request.user
        punonjes = Punonjes.objects.get(username= x)
        print(punonjes.username)
        return punonjes.pozicioni== "HR"


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.username == request.user

class IsOwnerLeje(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        x=obj.punonjes
        return x.username == request.user

class IsHRORIsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        x = request.user
        punonjes = Punonjes.objects.get(username=x)
        print(punonjes.username)
        #print(obj.username)
        return ((punonjes.pozicioni == "HR") or (obj.username == request.user))
