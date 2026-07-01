# Módulo 7 — Administración de Productos (E-commerce)

Proyecto Django que implementa la capa de acceso a datos para la gestión del catálogo de productos de un e-commerce, mediante operaciones CRUD usando el ORM de Django.

## Motor de base de datos

SQLite 3 (motor por defecto de Django, `db.sqlite3` en la raíz del proyecto).

## Modelo de datos

**Categoria**
| Campo  | Tipo         | Detalle           |
|--------|--------------|--------------------|
| nombre | CharField    | único, max 100     |

**Producto**
| Campo          | Tipo               | Detalle                                  |
|----------------|--------------------|--------------------------------------------|
| nombre         | CharField          | max 150                                    |
| descripcion    | TextField          | opcional                                   |
| precio         | DecimalField       | max_digits=10, decimal_places=2, > 0       |
| stock          | PositiveIntegerField | default 0                                |
| categoria      | ForeignKey(Categoria) | on_delete=SET_NULL, null=True, blank=True |
| creado_en      | DateTimeField      | auto_now_add                               |
| actualizado_en | DateTimeField      | auto_now                                   |

Relación: un **Producto** pertenece a una **Categoría** (FK), una Categoría puede tener muchos Productos (`related_name='productos'`). Si se elimina una categoría, los productos no se borran, solo quedan sin categoría asignada.

## Rutas principales

| Método | Ruta                     | Descripción                  |
|--------|---------------------------|-------------------------------|
| GET    | `/products/`               | Listado de productos          |
| GET/POST | `/products/create/`      | Crear producto                |
| GET/POST | `/products/edit/<id>/`   | Editar producto                |
| GET/POST | `/products/delete/<id>/` | Confirmar y eliminar producto  |
| GET    | `/admin/`                  | Panel administrativo Django   |

## Pasos para ejecutar el proyecto

```bash
git clone https://github.com/hanssoto-cyber/M7-portafolio.git
cd M7-portafolio
python -m venv venv
source venv/Scripts/activate   # Git Bash en Windows
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Luego visita `http://127.0.0.1:8000/products/`

## Usuario de prueba

- **Usuario:** admin
- **Contraseña:** (definida al ejecutar `createsuperuser`)

## Evidencias

Ver carpeta `evidencia/` con capturas del listado, formularios de creación/edición, confirmación de eliminación y panel administrativo.