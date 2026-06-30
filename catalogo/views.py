from django.shortcuts import render
from .models import Producto


def listar_productos(request):
    productos = Producto.objects.select_related('categoria').all()
    return render(request, 'catalogo/listar_productos.html', {
        'productos': productos
    })