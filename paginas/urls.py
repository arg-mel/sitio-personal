# paginas/urls.py
from django.urls import path

from .views import VistaAcercaDe, VistaCuadrado, VistaInicio, VistaProyectos, vista_saludo

urlpatterns = [
    path("", VistaInicio.as_view(), name="inicio"),
    path("acerca-de/", VistaAcercaDe.as_view(), name="acerca_de"),
    path("proyectos/", VistaProyectos.as_view(), name="proyectos"),
    path("cuadrado/<int:numero>/", VistaCuadrado.as_view(), name="cuadrado"),
    path("saludo/<str:nombre>/", vista_saludo, name="saludo"),
]
