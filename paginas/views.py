# paginas/views.py
from django.shortcuts import render
from django.views.generic import TemplateView


class VistaInicio(TemplateView):
    template_name = "inicio.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["habilidades"] = ["Python", "Django", "Git"]
        contexto["mensaje"] = "GRACIAS por VISITAR mi sitio."
        return contexto


class VistaAcercaDe(TemplateView):
    template_name = "acerca_de.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["nombre"] = "Melanie"
        contexto["edad"] = 22
        return contexto


class VistaProyectos(TemplateView):
    template_name = "proyectos.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["proyectos"] = [
            {"nombre": "Sitio personal", "descripcion": "Este sitio, hecho con Django."},
            {"nombre": "Tablero de mensajes", "descripcion": "Próximamente."},
            {"nombre": "Blog", "descripcion": "Próximamente."},
        ]
        return contexto


class VistaCuadrado(TemplateView):
    template_name = "cuadrado.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        # "numero" llega como entero gracias al convertidor <int:numero>
        numero = kwargs["numero"]
        contexto["numero"] = numero
        contexto["cuadrado"] = numero * numero
        return contexto


def vista_saludo(request, nombre):
    return render(request, "saludo.html", {"nombre": nombre})
