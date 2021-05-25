from django.urls import path
import uuid
from .views import login, PunonjesViewSet, DepartamentViewSet, \
    Departament_per_punonjesViewSet, LejetCreateView, LejetRetrieveView,LejetDestroyView,\
    LejetListView, LejetListViewA, LejetRetrieveUpdateView
from .models import Lejet
from rest_framework.routers import SimpleRouter
router= SimpleRouter()
router.register("punonjes", PunonjesViewSet)
router.register("departament", DepartamentViewSet)
router.register("departament_per_punonjes", Departament_per_punonjesViewSet)
#router.register("lejet", LejetViewSet)

urlpatterns =[
    path('login/', login),
    path('leje/create/', LejetCreateView.as_view()),
    path('leje/<str:id>/', LejetRetrieveView.as_view()),
    path('leje/<str:id>/delete/', LejetDestroyView.as_view()),
    path('lejet/', LejetListView.as_view()),
    path('lejet/hr/', LejetListViewA.as_view()),
    path('lejet/hr/<str:id>/', LejetRetrieveUpdateView.as_view()),
    ]
urlpatterns += router.urls