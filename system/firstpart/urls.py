from django.urls import path
import uuid
from .views import login, PunonjesRetriveView,PunonjesHrViewSet, DepartamentHrViewSet, \
    DepartamentPerPunonjesHrViewSet, LejetCreateView, LejetRetrieveView,LejetDestroyView,\
    LejetListView, DitePushimiListView, LejetHrListView, LejetRetrieveUpdateView, UserViewSet, DepartamentPerPunonjesRetriveView, DitePushimiViewSet
from .models import Lejet
from rest_framework.routers import SimpleRouter
router= SimpleRouter()
router.register("punonjes", PunonjesHrViewSet)
router.register("departament", DepartamentHrViewSet)
router.register("departament_per_punonjes", DepartamentPerPunonjesHrViewSet)
router.register("user", UserViewSet)
router.register("dite_pushimi", DitePushimiViewSet)

urlpatterns =[
    path('login/', login),
    path('self/punonjes/<int:pk>/', PunonjesRetriveView.as_view()),
    path('self/departament_per_punonjes/<int:pk>/', DepartamentPerPunonjesRetriveView.as_view()),
    path('leje/create/', LejetCreateView.as_view()),
    path('leje/<str:id>/', LejetRetrieveView.as_view()),
    path('leje/<str:id>/delete/', LejetDestroyView.as_view()),
    path('lejet/', LejetListView.as_view()),
    path('lejet/hr/', LejetHrListView.as_view()),
    path('lejet/hr/<str:id>/', LejetRetrieveUpdateView.as_view()),
    path('user/dite_pushimi/', DitePushimiListView.as_view()),
    ]
urlpatterns += router.urls