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
        print(request.user)
        return obj.username == request.user

class IsOwnerDepartament(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.punonjes.username == request.user

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
from datetime import datetime, timezone
class Is48hours(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.statusi != 'Ne pritje':
            now = datetime.now(timezone.utc)
            x = obj.fillimi
            y = now
            delta = x - y
            days = delta.days
            seconds = delta.seconds
            e = days * 86400 + seconds
            print(days)
            print(e >= 172800)
            print(e)
            return e >= 172800
        elif obj.statusi == 'Ne pritje':
            print("fine")
            return True
