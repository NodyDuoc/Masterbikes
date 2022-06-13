from email import message
from tkinter.tix import Tree
from django.shortcuts import render, redirect
from .models import RolUsuario, Usuario
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'Core/index.html')
def login(request):
    return render(request,'Core/login.html')
def perfil(request):
    return render(request,'Core/perfil.html')
def registro(request):
    return render(request,'Core/registro.html')