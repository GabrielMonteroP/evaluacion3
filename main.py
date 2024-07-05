import os
import globales

def menu_estadisticas():
    while True:
        os.system("cls")
        print("== Menú estadisticas ==")
        print("1.Producto mas alto")
        print("2.producto mas bajo")
        print("3.")
        print("3.Salir")
        opcion = globales.seleccionar_opcion(3)

        if opcion == 1:
            print("Montos Asignados correctamente")
        elif opcion == 2:
            print("Menu Estadisticas")
        elif opcion == 3:
            return
    

def menu_general():
    while True:
        os.system("cls")
        print("== Menú General ==")
        print("1.Asignar Montos Aleatorios")
        print("2.Ver Estadisticas")
        print("3.Salir")
        opcion = globales.seleccionar_opcion(3)

        if opcion == 1:
            print("Montos Asignados correctamente")
        elif opcion == 2:
            print("Menu Estadisticas")
        elif opcion == 3:
            return



menu_general()