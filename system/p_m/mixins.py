from .models import Punonjes, Pozicionet
from django.core.exceptions import  PermissionDenied


class HrMixin(object):
    def dispatch(self, request, *args, **kwargs):
        b = Pozicionet.objects.get(pozicioni="HR")
        a = Punonjes.objects.get(pozicioni=b)
        print(a.username)
        print(self.request.user)
        # if 1<0:
        if self.request.user != a.username:
            raise PermissionDenied
        return super(HrMixin, self).dispatch(request, *args, **kwargs)


class PergjegjesMixin(object):
    def dispatch(self, request, *args, **kwargs):
        b = Pozicionet.objects.get(pozicioni="Pergjegjes Departamenti")
        x = self.request.user
        a = Punonjes.objects.get(username=x)
        c = a.departamenti
        e = Punonjes.objects.get(pozicioni=b, departamenti=c)
        print(e.username)
        print(self.request.user)
        # if 1<0:
        if self.request.user != e.username:
            raise PermissionDenied
        return super(PergjegjesMixin, self).dispatch(request, *args, **kwargs)
