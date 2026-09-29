from django.shortcuts import render

def index(request):
    productos = [
        {"id" : 1, "nombre" : "Producto 1", "descripcion": "producto","precio": "$1.000", "stock": 10},
        {"id" : 2, "nombre" : "Producto 2", "descripcion": "producto","precio": "$2.000", "stock": 20},
        {"id" : 3, "nombre" : "Producto 3", "descripcion": "producto","precio": "$3.000", "stock": 30},
        {"id" : 4, "nombre" : "Producto 4", "descripcion": "producto","precio": "$4.000", "stock": 40},
        {"id" : 5, "nombre" : "Producto 5", "descripcion": "producto","precio": "$5.000", "stock": 50}
        ]
    return render(request, 'inicio/default.html', {"productos": productos})
