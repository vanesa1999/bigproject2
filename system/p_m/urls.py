from django.urls import path, include
from .views import Login, PunonjesRetriveView,PunonjesHrViewSet, DepartamentHrViewSet, \
    DepartamentPerPunonjesHrViewSet, LejetCreateView, LejetRetrieveView,LejetDestroyView,\
    LejetListView, DitePushimiListView, LejetHrListView, LejetRetrieveUpdateView, UserHrViewSet,\
    DepartamentPerPunonjesRetriveView, DitePushimiHrViewSet, LejetPergjegjesListView, LejetPergjegjesRetrieveUpdateView,\
    ExportHrViewSet

from rest_framework.routers import SimpleRouter
router= SimpleRouter()
router.register("hr/punonjes", PunonjesHrViewSet)
router.register("hr/departament", DepartamentHrViewSet)
router.register("hr/departament_per_punonjes", DepartamentPerPunonjesHrViewSet)
router.register("hr/user", UserHrViewSet)
router.register("hr/dite_pushimi", DitePushimiHrViewSet)
router.register("hr/export", ExportHrViewSet)


urlpatterns =[
    path('rest-auth/', include('rest_auth.urls')),
    path('login/', Login),
    path('self/punonjes/<int:pk>/', PunonjesRetriveView.as_view()),
    path('self/departament_per_punonjes/<int:pk>/', DepartamentPerPunonjesRetriveView.as_view()),
    path('self/leje/create/', LejetCreateView.as_view()),
    path('self/leje/<str:id>/', LejetRetrieveView.as_view()),
    path('self/leje/<str:id>/delete/', LejetDestroyView.as_view()),
    path('self/lejet/', LejetListView.as_view()),
    path('hr/lejet/', LejetHrListView.as_view()),
    path('hr/lejet/<str:id>/', LejetRetrieveUpdateView.as_view()),
    path('pergjegjes/lejet/', LejetPergjegjesListView.as_view()),
    path('pergjegjes/lejet/<str:id>/', LejetPergjegjesRetrieveUpdateView.as_view()),
    path('self/dite_pushimi/', DitePushimiListView.as_view()),
    ]
urlpatterns += router.urls