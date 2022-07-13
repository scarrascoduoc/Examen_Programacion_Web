from django import forms
from django.forms import ModelForm
from .models import Producto,Login,Donaciones
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(ModelForm):
    class Meta:
        model=Producto
        fields=['idProducto','NombreProducto','ValorProducto','CategoriaProducto','StockProducto']
class LoginForm(ModelForm):
    class Meta:
        model=Login
        fields=['usuario','password']

CHOICES=[(1000,'1000'),
         (5000,'5000'),
         (10000,'10000'),
         (20000,'20000')]



class DonacionForm(forms.ModelForm):
    montos = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    class Meta:
        model = Donaciones
        fields = '__all__'
        labels = {
            'nombre': 'Nombre',
            'apellido_pat': 'Apellido Paterno',
            'apellido_mat':'Apellido Materno',
            'monto':'Monto especifico',
            }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_pat': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_mat': forms.TextInput(attrs={'class': 'form-control'}),
            'monto': forms.TextInput(attrs={'class':'form-control', 'value':0}),
        }
    
        def __init__(self, *args,**kwargs):
            super(DonacionForm, self).__init__(*args,**kwargs)
            self.fields['monto'].required = False

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
                'username',
                'first_name',
                'last_name',
                'email',
            ]
        labels = {
                'username': 'Nombre de usuario',
                'first_name': 'Nombre',
                'last_name': 'Apellidos',
                'email': 'Correo',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
           
        }
