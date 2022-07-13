from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Producto
from .serializers import ProductoSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def lista_productos(request):
    """
    GET = Lista todos los productos
    POST = Agrega Registro
    """
    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_producto(request,id):
    """
    get,update o delete
    """
    try:
        producto=Producto.objects.get(idProducto=id)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer=ProductoSerializer(producto)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(producto,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def login(request):
    data=JSONParser().parse(request)

    username=data['username']
    password=data['password']

    try:
        user= User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("Usuario inválido")
    pass_valido=check_password(password,user.password)
    if not pass_valido:
        return Response("Password incorrecta")
    
    token, created=Token.objects.get_or_create(user=user)
    return Response(token.key)
