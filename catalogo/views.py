from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Producto
from .forms import ProductoForm


def listar_productos(request):
    productos = Producto.objects.select_related('categoria').all()
    return render(request, 'catalogo/listar_productos.html', {
        'productos': productos
    })


def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado correctamente.')
            return redirect('catalogo:listar_productos')
        else:
            messages.error(request, 'Revisa los errores del formulario.')
    else:
        form = ProductoForm()

    return render(request, 'catalogo/form_producto.html', {
        'form': form,
        'titulo': 'Nuevo producto'
    })