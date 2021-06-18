
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.permissions import IsAuthenticated, BasePermission
from django.contrib.auth.models import User
from .models import  Punonjes, Departament, Departament_per_punonjes, Lejet, DitePushimi, Pozicionet
from .serializers import PunonjesHrSerializer, DepartamentHrSerializer, UserHrSerializer, \
    DepartamentPerPunonjesSerializer, LejetCreateSerializer, LejetViewSerializer, LejetHrViewSerializer,\
    DitePushimiHrSerializer, LejetHrViewSerializer2
from .permissions import IsOwner, IsHR, IsHRORIsOwner, IsOwnerLeje, IsOwnerDepartament, Is48hours
from .mixins import HrMixin, PergjegjesMixin
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView, DestroyAPIView
from django.db.models import Q
from rest_framework.viewsets import ReadOnlyModelViewSet
from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer

class IsHr(BasePermission):
    def has_object_permission(self, request, view, obj):
        return True
    def has_permission(self, request, view):
        return True


@api_view(["POST"])
def Login(request):
    username= request.data.get("username")
    password= request.data.get("password")

    user= authenticate(username=username, password= password)
    if not user:
        return Response({"error": "Login failed"}, status= HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})


class PunonjesHrViewSet(HrMixin,ModelViewSet):
    serializer_class = PunonjesHrSerializer
    queryset = Punonjes.objects.all()
    permission_classes = (IsAuthenticated,)

class PunonjesRetriveView(RetrieveAPIView):
    serializer_class = PunonjesHrSerializer
    queryset = Punonjes.objects.all()
    permission_classes = (IsOwner,IsAuthenticated)

class DepartamentHrViewSet(HrMixin,ModelViewSet):
    serializer_class = DepartamentHrSerializer
    queryset = Departament.objects.all()
    permission_classes = (IsAuthenticated,)

class DepartamentPerPunonjesHrViewSet(HrMixin,ModelViewSet):
    serializer_class = DepartamentPerPunonjesSerializer
    queryset = Departament_per_punonjes.objects.all()
    permission_classes = (IsAuthenticated, IsHR)

class DepartamentPerPunonjesRetriveView(RetrieveAPIView):
    serializer_class = DepartamentPerPunonjesSerializer
    queryset = Departament_per_punonjes.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerDepartament)

class UserHrViewSet(HrMixin, ModelViewSet):
    serializer_class = UserHrSerializer
    queryset = User.objects.all()

class DitePushimiHrViewSet(HrMixin, ModelViewSet):
    serializer_class = DitePushimiHrSerializer
    queryset = DitePushimi.objects.all()
    permission_classes = (IsAuthenticated,)

class ExportHrViewSet(HrMixin, XLSXFileMixin, ReadOnlyModelViewSet):
    queryset = Lejet.objects.all()
    serializer_class = LejetHrViewSerializer
    renderer_classes = (XLSXRenderer,)
    filename = 'my_export.xlsx'

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
    queryset = Lejet.objects.filter(Q(statusi= 'Pranuar') | Q(statusi= 'Ne pritje'))
    permission_classes = (IsAuthenticated,IsOwnerLeje, Is48hours,)
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
    serializer_class = LejetHrViewSerializer2
    queryset = Lejet.objects.filter()
    permission_classes = (IsAuthenticated, )

class LejetRetrieveUpdateView(HrMixin,RetrieveUpdateAPIView):
    serializer_class = LejetHrViewSerializer
    #queryset = Lejet.objects.all()
    #permission_classes = (IsAuthenticated, IsHR,)
    lookup_field = 'id'
    def get_queryset(self):
        p = Pozicionet.objects.get(pozicioni='Pergjegjes Departamenti')
        punonjes = Punonjes.objects.filter(pozicioni=p)
        queryset = Lejet.objects.filter(punonjes__in=punonjes)
        return queryset

class LejetPergjegjesListView(PergjegjesMixin,ListAPIView):
    serializer_class = LejetHrViewSerializer2
    #queryset = Lejet.objects.filter()
    permission_classes = (IsAuthenticated, )
    def get_queryset(self):
        x= self.request.user
        punonjes= Punonjes.objects.get(username= x)
        d= punonjes.departamenti
        p=Punonjes.objects.filter(departamenti=d)
        queryset= Lejet.objects.filter(punonjes__in=p)
        return queryset
class LejetPergjegjesRetrieveUpdateView(PergjegjesMixin,RetrieveUpdateAPIView):
    serializer_class = LejetHrViewSerializer
    #queryset = Lejet.objects.all()
    #permission_classes = (IsAuthenticated, IsHR,)
    lookup_field = 'id'
    def get_queryset(self):
        p= Pozicionet.objects.get(pozicioni = 'Punonjes Departamenti')
        punonjes= Punonjes.objects.filter(pozicioni= p)
        queryset= Lejet.objects.filter(punonjes__in= punonjes)
        return queryset

class DitePushimiListView(ListAPIView):
    serializer_class = DitePushimiHrSerializer
    queryset = DitePushimi.objects.all()






