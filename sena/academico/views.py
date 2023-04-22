import os
from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
from django.template import Template, Context
from django.template import loader
from .models import *

# Create your views here.


def index(request):
    return HttpResponse("Hola")


def coor(request, N, R):
    documento = ""
    if N == '0':
        todo = COORDINACION.objects.all()
        plt = loader.get_template('coordinacion.html')
        documento = plt.render({"lista": todo, "N": N})
    if N == '1':
        plt = loader.get_template('coordinacion.html')
        documento = plt.render({"N": N})
    if N == '2':
        plt = loader.get_template('coordinacion.html')
        documento = plt.render({"N": N})
        p = COORDINACION.objects.get(id=R)
        plt = loader.get_template('coordinacion.html')
        documento = plt.render({"lista": p, "N": N})
    if N == '21':
        p = COORDINACION.objects.get(id=R)
        nombre = request.GET["nombre"]
        p.nom = nombre
        p.save()
        documento = """<h2>COORDINACION GUARDADA SATISFACTORIAMENTE...</h2>
        <script>
        function Ir(){
            location.href="/coor/0/0";
            }
            setTimeout('Ir()',2000);
            </script>"""
    if N == '3':
        p = COORDINACION.objects.get(id=R)
        p.delete()
        documento = """<h2>COORDINACION BORRADA SATISFACTORIAMENTE...</h2>
        <script>
        function Ir(){
            location.href="/coor/0/0";
            }
            setTimeout('Ir()',2000);
        </script>"""
        plt = loader.get_template('coordinacion.html')
        documento = plt.render({"N": N})
    if N == '11':
        nombre = request.GET["nombre"]
        coordina = COORDINACION(nom=nombre)
        coordina.save()
        documento = """<h2>COORDINACION CREADA SATISFACTORIAMENTE...</h2>
        <script>
        function Ir(){
            location.href="/coor/0/0";
            }
            setTimeout('Ir()',2000);
        </script>"""
    return HttpResponse(documento)
