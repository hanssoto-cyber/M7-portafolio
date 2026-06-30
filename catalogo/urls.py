from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    path('', views.listar_productos, name='listar_productos'),
    path('create/', views.crear_producto, name='crear_producto'),
    path('edit/<int:pk>/', views.editar_producto, name='editar_producto'),
]