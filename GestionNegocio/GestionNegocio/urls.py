"""
URL configuration for GestionNegocio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apptienda import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.formProducto),
    path('', views.formProducto),
    path('formCategoria/', views.formCategoria),
    path('formProducto/', views.formProducto),
    path('listarProductos/', views.listarProductos),
    path('addCategoria/', views.addCategoria),
    path('addProducto/', views.addProducto),
    path('getProducto/<int:id>/', views.getProducto),
    path('updateProducto/', views.updateProducto),
    path('deleteProducto/<int:id>/', views.deleteProducto),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT
    )
