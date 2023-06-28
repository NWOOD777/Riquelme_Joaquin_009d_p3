import os
from numpy import zeros
import msvcrt

def cs():
    os.system("cls")

habitacion = zeros((2,5), int)
valor_dia = 15000
total = 0

lista_rut = []
lista_nomdue = []
lista_idunico = []
lista_nompet = []
lista_dias = []
lista_habitacion = []
lista_total = []

id_cant = 0

def grabar():
    while True:
        try:
            rut_dueño = int(input("Ingrese su rut(sin puntos ni digito verificador)\n -> "))
            if rut_dueño > 4000000 and rut_dueño < 99999999:
                lista_rut.append(rut_dueño)
                break
            else:
                print("ERROR! su rut no es valido debe tener entre 7 y 8 caracteres!")
        except:
            cs()
            print("ERROR! debe ingresar un número entero!")

    while True:
        nom_dueño = input("Ingrese su nombre\n -> ")
        if len(nom_dueño)>=3 and len(nom_dueño) <= 50:
            lista_nomdue.append(nom_dueño)
            break
        else:
            cs()
            print("ERROR! debe escribir un nombre con al menos 3 digitos!")
    lista_idunico.append(id_cant +1)
    id_cant+1

    while True:
        nom_pet = input("Ingrese el nombre de su mascota\n -> ")
        if len(nom_pet)>=3 and len(nom_pet)<=50:
            lista_nompet.append(nom_pet)
            break
        else:
            cs()
            print("ERROR! debe escribir un nombre con al menos 3 digitos!")

    while True:
        try:
            dias = int(input("Ingrese los días que se quedara su mascota\n -> "))
            if dias >=1:
                lista_dias.append(dias)
                total = 15000 * dias
                lista_total.append(total)
                break
            else:
                cs()
                print("ERROR! debe ingresar por lo menos 1 día!")
        except:
            cs()
            print("ERROR! debe ingesar un número entero!")
    
    cs()
    print("Habitaciones\n")
    for x in range(2):
        print(f"\nFila {x+1}: ", end=" ")
        for y in range(5):
            print(" ",habitacion[x][y], end=" ")

    while True:
        try:
            habitacion_pet = int(input("\nIngrese la habitacion deseada para su mascota\n-> "))
            if habitacion_pet >= 1 and habitacion_pet <= 11:
                if habitacion >= 1 and habitacion <= 5:
                    if habitacion[1][habitacion_pet] <= 0:
                        print("Lo sentimos la habitacion ya esta en uso")
                elif habitacion_pet>=6 and habitacion_pet<=11:
                    if habitacion[1][habitacion_pet] <= 0:
                        print("Lo sentimos la habitacion ya esta en uso")
            else:
                habitacion[1][habitacion_pet] == 1
                break
        except:
            cs()
            print("ERROR! debe ingresar un número entero!")

def buscar():
    while True:
        value = None
        buscar = int(input("Ingrese el rut del dueño\n-> "))
        for x in range(len(lista_rut)):
            if x == buscar:
                value = x
                break
            else:
                pass
        break
    if value == None:
        print(f"Lo sentimos mucho, no se encontro la habitacion de el rut {buscar}")
    else:
        print("La habitacion de su mascota es", lista_habitacion[value])


def retirarse():
    while True:
        value = None
        try:
            buscar = int(input("Ingrese el rut del dueño\n-> "))
            if len(buscar) >= 7 and len(buscar) <= 8:
                break
            else:
                cs()
                print("ERROR! debe ingresar su rut sin puntos ni digito verificador!")
        except:
            print("ERROR! debe ingresar un número entero!")

        for x in range(len(lista_rut)):
            if x == buscar:
                value = x
                break
            else:
                pass
        print("El total a pagar es de", lista_total[value], "pesos")
    
def salir():
    pass

def menu():
    print("""\n\tMenú
    
    1. Grabar
    2. Buscar
    3. Retirar
    4. Salir
    """)

    opcion  = int(input("Ingese la opcion deseada\n-> "))
    if opcion in(1,2,3,4):
        if opcion==1:
            grabar()
        if opcion==1:
            buscar()
        if opcion==1:
            retirarse()
        if opcion==1:
            salir()