import os
import json
import random
import globales
import statistics
from math import prod
os.system("cls")

trabajadores = [
    "Juan Pérez", "María García", "Carlos López", "Ana Martínez",
    "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", 
    "Isabel Gómez", "Francisco Díaz", "Elena Fernández"
]

def asignar_ventas_aleatorias():
    os.system("cls")
    empleados = []
    for trabajador in trabajadores:
        ventas = random.randint(1500000, 5000000)
        empleados.append({"nombre": trabajador, "ventas": ventas})
    with open("ventas.json", "w") as file:
        json.dump(empleados, file)
    print("Ventas aleatorias asignadas y guardadas en ventas.json")


def cargar_ventas():
    with open("ventas.json", 'r') as file:
        empleados = json.load(file)
    return empleados


def ver_estadisticas():
    while True:
        os.system("cls")
        empleados = cargar_ventas()
        ventas = [empleado["ventas"] for empleado in empleados]
        venta_mas_alta = max(ventas)
        venta_mas_baja = min(ventas)
        promedio_ventas = statistics.mean(ventas)
        media_geometrica = prod(ventas) ** (1/len(ventas))
    
        print("\n--- Estadísticas de Ventas ---")
        print(f"Venta más alta: ${venta_mas_alta}")
        print(f"Venta más baja: ${venta_mas_baja}")
        print(f"Promedio de las ventas: ${promedio_ventas:.2f}")
        print(f"Media geométrica de las ventas: ${media_geometrica:.2f}")

        input()

       

def menu():
    os.system("cls")
    while True:
        print("=== MENU PRINCIPAL===")
        print("1. Asignar ventas aleatorias.")
        print("2. Ver estadísticas.")
        print("3. Salir del programa.")

        opcion = globales.seleccionar_opcion(3)

        if opcion == 1:
            print("1. Asignar ventas aleatorias.")
            asignar_ventas_aleatorias()
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



