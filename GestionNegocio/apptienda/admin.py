from django.contrib import admin
from apptienda.models import Producto, Categoria

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)