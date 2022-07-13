from django.urls import path
from .views import detalle_producto, lista_productos,login

urlpatterns = [
    path('lista_productos',lista_productos,name="lista_productos"),
    path('detalle_producto/<id>',detalle_producto,name="detalle_producto"),
    path('login',login,name="login"),
]