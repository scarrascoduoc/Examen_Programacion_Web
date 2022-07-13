from django.urls import path
from .views import camas, collares, form_del_producto, home, nosotros, ropa,tienda,contacto,form_producto,form_mod_producto,inicio,compra
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('inicio',inicio,name="inicio"),
    path('',home,name="home"),
    path('nosotros', nosotros,name="nosotros"),
    path('tienda', tienda,name="tienda"),
    path('contacto', contacto,name="contacto"),
    path('form-producto',form_producto,name="form-producto"),
    path('form-mod-producto/<id>',form_mod_producto,name="form-mod-producto"),
    path('form-del-producto/<id>', form_del_producto, name='form-del-producto'),
    path('collares',collares,name="collares"),
    path('camas',camas,name="camas"),
    path('ropa',ropa,name="ropa"),
    path('compra',compra,name="compra"),
    path('add_donacion', views.DonacionCreate.as_view(), name="add_donacion"),
    path('list_donacion', views.DonacionList.as_view(), name="list_donacion"),
    path('registrar', views.RegistroUsuario.as_view(), name="registrar"),
    path('listar', views.UserList.as_view(), name="list_user"),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),

    # Login and Logout
    path('login/', LoginView.as_view(redirect_authenticated_user=True,template_name='core/home.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='core/home.html'), name='logout'),
]