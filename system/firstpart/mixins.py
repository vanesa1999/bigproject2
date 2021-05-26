from .models import Punonjes
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.views import redirect_to_login
from .models import Punonjes
from django.core.exceptions import ImproperlyConfigured, PermissionDenied
class HrMixin(object):
    def dispatch(self, request, *args, **kwargs):
        a= Punonjes.objects.get(pozicioni= "HR")
        if request.user != a.username :
            raise PermissionDenied
        return super(HrMixin, self).dispatch(request,*args,**kwargs)
