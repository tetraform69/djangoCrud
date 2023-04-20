from django.shortcuts import render, redirect
from django.db import Error
from apptienda.models import Categoria
from apptienda.models import Producto


# Create your views here.


def formCategoria(request):
    return render(request, "formCategoria.html")


def formProducto(request):
    try:
        categorias = Categoria.objects.all()
        mensaje = ""

    except Error as err:
        mensaje = f"error {err}"

    json = {
        "mensaje": mensaje,
        "categorias": categorias,
        "producto": None,
    }

    return render(request, "formProducto.html", json)


def listarProductos(request):
    try:
        productos = Producto.objects.all()
        mensaje = ""
    except Error as err:
        mensaje = f"Problemas al listar {err}"

    json = {"mensaje": mensaje, "productos": productos}
    return render(request, "listProducts.html", json)


def addCategoria(request):
    nombre = request.POST["nombre"]

    try:
        categoria = Categoria(nombreCat=nombre)
        categoria.save()
        mensaje = "Agregada La Categoria"

    except Error as err:
        mensaje = f"Problemas al agregar {err}"

    json = {"mensaje": mensaje}
    return render(request, "formCategoria.html", json)


def addProducto(request):
    codigo = int(request.POST["codigo"])
    nombre = request.POST["nombre"]
    precio = int(request.POST["precio"])
    idCat = int(request.POST["categoria"])
    foto = request.FILES["foto"]
    try:
        categoria = Categoria.objects.get(id=idCat)
        producto = Producto(
            codigoPro=codigo,
            nombrePro=nombre,
            precioPro=precio,
            categoriaPro=categoria,
            fotoPro=foto,
        )

        producto.save()

        return redirect("/listarProductos/")

    except Error as err:
        mensaje = f"Problemas al agregar {err}"

    categorias = Categoria.objects.all()

    json = {
        "mensaje": mensaje,
        "categorias": categorias,
        "producto": producto,
    }

    return render(request, "formProducto.html", json)


def getProducto(request, id):
    try:
        producto = Producto.objects.get(id=id)
        categorias = Categoria.objects.all()
        mensaje = ""

    except Error as err:
        mensaje = f"Error: {err}"

    json = {"mensaje": mensaje, "producto": producto, "categorias": categorias}

    return render(request, "formEditarProducto.html", json)


def updateProducto(request):
    idPro = int(request.POST["id"])
    nombre = request.POST["nombre"]
    codigo = request.POST["codigo"]
    precio = request.POST["precio"]
    idCat = request.POST["categoria"]
    foto = request.FILES.get("foto", False)

    try:
        categoria = Categoria.objects.get(id=idCat)

        producto = Producto.objects.get(id=idPro)
        producto.codigoPro = codigo
        producto.nombrePro = nombre
        producto.precioPro = precio
        producto.categoriaPro = categoria

        if foto != False:
            producto.fotoPro = foto

        producto.save()
        mensaje = "Producto actualizado"

        return redirect("/listarProductos/")

    except Error as err:
        mensaje = f"Error: {err}"

    categorias = Categoria.objects.all()
    json = {
        "mensaje": mensaje,
        "categorias": categorias,
        "producto": producto,
    }

    return render(request, "formEditarProducto.html", json)


def deleteProducto(request, id):
    try:
        producto = Producto.objects.get(id=id)
        producto.delete()
        mensaje = "Producto Eliminado"

    except Error as err:
        mensaje = f"Error: {err}"

    json = {"mensaje": mensaje}
    
    return redirect("/listarProductos/", json)
