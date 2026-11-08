# paginas/tests.py
from django.template.loader import render_to_string
from django.test import SimpleTestCase
from django.urls import reverse


class PruebasPaginaInicio(SimpleTestCase):
    def test_url_existe_en_ubicacion_correcta(self):
        respuesta = self.client.get("/")
        self.assertEqual(respuesta.status_code, 200)

    def test_url_disponible_por_nombre(self):
        respuesta = self.client.get(reverse("inicio"))
        self.assertEqual(respuesta.status_code, 200)

    def test_plantilla_correcta(self):
        respuesta = self.client.get(reverse("inicio"))
        self.assertTemplateUsed(respuesta, "inicio.html")
        self.assertTemplateUsed(respuesta, "base.html")

    def test_contenido_plantilla(self):
        respuesta = self.client.get(reverse("inicio"))
        self.assertContains(respuesta, "<h1>Página de inicio</h1>")


class PruebasPaginaAcercaDe(SimpleTestCase):
    def test_url_existe_en_ubicacion_correcta(self):
        respuesta = self.client.get("/acerca-de/")
        self.assertEqual(respuesta.status_code, 200)

    def test_url_disponible_por_nombre(self):
        respuesta = self.client.get(reverse("acerca_de"))
        self.assertEqual(respuesta.status_code, 200)

    def test_plantilla_correcta(self):
        respuesta = self.client.get(reverse("acerca_de"))
        self.assertTemplateUsed(respuesta, "acerca_de.html")

    def test_contenido_plantilla(self):
        respuesta = self.client.get(reverse("acerca_de"))
        self.assertContains(respuesta, "Me llamo Melanie")


class PruebasPaginaProyectos(SimpleTestCase):
    def test_url_existe_en_ubicacion_correcta(self):
        respuesta = self.client.get("/proyectos/")
        self.assertEqual(respuesta.status_code, 200)

    def test_url_disponible_por_nombre(self):
        respuesta = self.client.get(reverse("proyectos"))
        self.assertEqual(respuesta.status_code, 200)

    def test_plantilla_correcta(self):
        respuesta = self.client.get(reverse("proyectos"))
        self.assertTemplateUsed(respuesta, "proyectos.html")

    def test_contenido_plantilla(self):
        respuesta = self.client.get(reverse("proyectos"))
        self.assertContains(respuesta, "<h1>Proyectos</h1>")
        self.assertContains(respuesta, "Hay 3 proyectos")
        self.assertContains(respuesta, "TABLERO DE MENSAJES")

    def test_lista_vacia_muestra_mensaje(self):
        # Revisa el {% empty %} mostrando la plantilla sin proyectos
        html = render_to_string("proyectos.html", {"proyectos": []})
        self.assertIn("Todavía no hay proyectos.", html)


class PruebasPaginaCuadrado(SimpleTestCase):
    def test_url_existe_en_ubicacion_correcta(self):
        respuesta = self.client.get("/cuadrado/7/")
        self.assertEqual(respuesta.status_code, 200)

    def test_url_disponible_por_nombre(self):
        respuesta = self.client.get(reverse("cuadrado", args=[7]))
        self.assertEqual(respuesta.status_code, 200)

    def test_plantilla_correcta(self):
        respuesta = self.client.get(reverse("cuadrado", args=[7]))
        self.assertTemplateUsed(respuesta, "cuadrado.html")

    def test_calcula_el_cuadrado(self):
        respuesta = self.client.get(reverse("cuadrado", args=[7]))
        self.assertContains(respuesta, "El cuadrado de 7 es 49")

    def test_texto_en_lugar_de_numero_da_404(self):
        respuesta = self.client.get("/cuadrado/abc/")
        self.assertEqual(respuesta.status_code, 404)


class PruebasPaginaSaludo(SimpleTestCase):
    def test_saludo_con_nombre(self):
        respuesta = self.client.get(reverse("saludo", args=["luis"]))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "¡Hola, Luis!")


class PruebasMenu(SimpleTestCase):
    def test_menu_tiene_todas_las_paginas(self):
        respuesta = self.client.get(reverse("inicio"))
        self.assertContains(respuesta, 'href="/"')
        self.assertContains(respuesta, 'href="/acerca-de/"')
        self.assertContains(respuesta, 'href="/proyectos/"')
        self.assertContains(respuesta, 'href="/cuadrado/5/"')
