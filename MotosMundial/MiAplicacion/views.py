from django.shortcuts import render,HttpResponse

# Create your views here.

def hola_mundo(request):
    return HttpResponse("""
                            <h1> Hola Mundo </h1>
                        """)

def pagina(request):
    return HttpResponse("""
                            <h1> Sitio Web MOTOS MUNDIAL </h1>
                            <h3> Porque nosotros si sabemos de motos </h3>
                        """)