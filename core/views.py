from django.shortcuts import render,redirect
from core.forms import  ProductoForm,DonacionForm,RegistroForm
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from core.models import  Donaciones, Producto
from django.contrib.auth.models import User

# Create your views here.

def inicio(request):
    return render(request,'core/inicio.html') 

def home(request):
    return render(request,'core/home.html')

def nosotros(request):
    return render(request,'core/nosotros.html') 

def tienda(request):
    producto=Producto.objects.all()
    datos = {
        'producto':producto
    }
    return render(request,'core/carrito/index.html',datos) 

def compra(request):
    producto=Producto.objects.all()
    datos = {
        'producto':producto
    }
    return render(request,'core/carrito/compra.html',datos) 

def collares(request):
    return render(request,'core/collarestienda.html')

def camas(request):
    return render(request,'core/camastienda.html')

def ropa(request):
    return render(request,'core/ropatienda.html')

def contacto(request):
    return render(request,'core/contacto.html') 

def form_producto(request):
    datos = {
        'form': ProductoForm
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Guardado Correctamente'
    return render(request,'core/form_producto.html',datos)

def form_mod_producto(request, id):
    producto = Producto.objects.get(idProducto = id)
    
    datos = {
        'form': ProductoForm(instance = producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance = producto)
        
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Modificado Correctamente'
            
    return render(request, 'core/form_mod_producto.html', datos)

def form_del_producto(request, id):
    producto = Producto.objects.get(idProducto = id)
    
    producto.delete()
    
    return redirect(to=home)

class DonacionCreate(CreateView):
    model = Donaciones
    form_class = DonacionForm
    template_name = 'core/donacion.html'
    success_url = reverse_lazy("add_donacion")
    
class DonacionList(ListView):
    model = Donaciones
    template_name = 'core/list_donacion.html'

class RegistroUsuario(CreateView):
    model = User
    template_name = "core/usuario_form.html"
    form_class = RegistroForm
    success_url = reverse_lazy('home')


class UserList(ListView):
    model = User
    template_name = 'core/listar_usuario.html'


