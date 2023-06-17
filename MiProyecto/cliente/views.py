from django.shortcuts import render
from .models import Cliente
<<<<<<< HEAD
# Create your views here.
def index(request):
    clientes = Cliente.objects.all()
    datos={"clientes":clientes}
=======

# Create your views here.
def index(request):
    clientes = Cliente.objects.all()
    datos = {"clientes" : clientes}
>>>>>>> 1575d2a5096c46067b16c9cea0c88fa73f1ec4ec
    return render(request, "cliente/index_cliente.html", datos)

