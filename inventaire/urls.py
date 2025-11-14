from django.contrib import admin
from django.urls import path
from materiel import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.liste_materiels, name='liste_materiels'),
    path('ajouter/', views.ajouter_materiel, name='ajouter_materiel'),
    path('modifier/<int:id>/', views.modifier_materiel, name='modifier_materiel'),
    path('supprimer/<int:id>/', views.supprimer_materiel, name='supprimer_materiel'),
]
