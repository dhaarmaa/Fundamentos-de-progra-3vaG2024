import os
import json
import random
import statistics
import globales
from math import prod

productos = [
    "Café Americano",
    "Té Chai",
    "Croissant",
    "Jugo Naranja",
    "Panini de Pavo y Queso",1
    "Pastel de Zanahoria",
    "Espresso Doble",
    "Baño de Frutas",
    "Muffin",
    "Ensalada",
    "Chocolate Caliente",
    "Tarta de Frambuesa",
    "Sándwich de Huevo",
    "Galletas de Avena",
    "Frappé de Caramelo"
]

def asignar_valores_aleatorios():
    items = []

    ##realizamos una iteracion ente el array vacio y el array productos
    for producto in productos:

         ##en la variable "valores" asignamos un valor aleatorio y lo multiplicamos por 100 para redondear
        valores = random.randint(2000, 10000) * 100

        # en productoIvaRedondeado tomamos el valor aletarorio que nos arrojo la variable valores y la multiplicamos por 0.19 para sacar el iva
        productoIva = int(valores * 0.19)

        #Agregar al array items
        items.append({
            "nombre": producto,
            "valor": valores,
            "iva": productoIva
        })
        
    with open("valores.json", "w") as file:
        json.dump(items, file)

    print("Valores aleatorios asignados y guardados en valores.json")

def cargar_valores():
    with open("valores.json", 'r') as file:
        items = json.load(file)
    return items

def ver_estadisticas():
    productos = cargar_valores()
    valoresItems = [item["valor"] for item in productos]
    valoresIva = [item["iva"] for item in productos]
    valorMax = max(valoresItems)
    valorMin = min(valoresItems)
    promedioValor = statistics.mean(valoresItems)
    mediaGeometrica = prod(valoresItems) ** (1 / len(valoresItems))
    
    print("-----------------------------------")
    print("--- Estadísticas de los productos ---")
    print("-----------------------------------")
    print(f"Item más alto: ${valorMax}")
    print("-----------------------------------")
    print(f"Item más bajo: ${valorMin}")
    print("-----------------------------------")
    print(f"Promedio: ${promedioValor}")
    print("-----------------------------------")
    print(f"Media geométrica: {mediaGeometrica}")
    print("-----------------------------------")

def menu():
    os.system("cls" if os.name == "nt" else "clear")
    while True:
        print("******* MENU PRINCIPAL *******")
        print("1) Asignar ventas aleatorias.")
        print("2) Ver estadísticas.")
        print("3) Salir del programa.")

        opcion = globales.seleccionar_opcion(3)

        if opcion == 1:
            print("1. Asignar ventas aleatorias.")
            asignar_valores_aleatorios()
        elif opcion == 2:
            print("2. Ver estadísticas.")
            ver_estadisticas()
        elif opcion == 3:
            print("3. Salir del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
