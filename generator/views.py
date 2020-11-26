from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request,'generator/home.html')

def about(request):
    return render(request,'generator/about.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz') #Lista con caracteres a usar para el password

    #Validando si el usuario requiere que el password contenga mayusculas
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')) #Lo que se hace es que se agrega una lista adicional con las letras en mayusculas a la lista original en minusculas

    #Validando si el usuario requiere que el password contenga caracteres especiales
    if request.GET.get('special'):
        characters.extend(list('@#$%^&*()+~'))

    #Validando si el usuario requiere que el password contenga numeros
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    lenght = int(request.GET.get('lenght')) #asignando el valor que proviene del valor indicado por el usuario de cuantos caracteres se necesitan y proviene del nombre del control html que contiene el dato
    thepassword = '' #Se declara e inicializa la variable que contendra el password

    for x in range(lenght):
        thepassword += random.choice(characters) #De los valores contenidos en la variable characters toma uno aleatorio mientras no se llegue a la cantidad de caracteres indicada por el usuario

    return render(request,'generator/password.html',{'password':thepassword}) # regresa la pagina password.html y le comparte el valor obtenido en el password
