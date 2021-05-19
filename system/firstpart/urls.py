from django.urls import path
from .views import punonjes_detail_view, punonjes_delete_view, punonjes_update_view,\
    punonjes_create_view, departament_detail_view, departament_create_view,departament_update_view

urlpatterns= [
    path('punonjes/<int:pk>/', punonjes_detail_view , name= 'punonjes-detail'),
    path('punonjes/<int:pk>/update', punonjes_update_view, name= 'punonjes-update'),
    path('punonjes/<int:pk>/delete/', punonjes_delete_view, name= 'punonjes-delete'),
    path('punonjes/create/', punonjes_create_view, name= 'punonjes-create'),
    path('departament/<int:pk>/', departament_detail_view , name= 'departament-detail'),
    path('departament/<int:pk>/update', departament_update_view, name='departament-update'),
    path('departament/create/', departament_create_view, name='departament-create'),
]
