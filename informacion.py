import json
import requests
import time
import os
import errno

def maximo(precio, producto):
    suma=0
    print("\nProductos:\n")
    for numero in range(len(producto)):
        print(producto[numero])
        suma=max(precio)
    print("\nLa Maxima de los precios es de: " + str(max(precio)) + "\n")

def minimo(precio, producto):
    suma=0
    print("\nProductos:\n")
    for numero in range(len(producto)):
        print(producto[numero])
        suma=min(precio)
    print("\nLa Minima de los precios es de: " + str(min(precio)) + "\n")

def promedio(precio, producto):
    suma=0
    print("\nProductos:\n")
    for numero in range(len(precio)):
        suma+=float(precio[numero])
        print(producto[numero])
    
    print("\nEl Promedio de los precios es de: " + str(suma/len(precio)) + "\n")
    

def leerInfo():
    precio = []
    producto = []
    nombredelarchivo=input("\nQue archivo quiere comprobar informacion?(Solo Consultas): ")
    try:
        with open("Consulta/" + nombredelarchivo + ".txt","r") as archivo:
            for linea in archivo:
                print(linea)
                principio=linea.find("Precio:")
                fin=linea.find(",\tEtiquetas:")
                precio.append(float(linea[principio+8:fin-1]))
                principio=linea.find("Nombre:")
                fin=linea.find(",\tPrecio:")
                producto.append(linea[principio+8:fin-1])
            for numero in range(len(precio)):
                print(producto[numero]+ " - " + str(precio[numero]))           
            print("\n\nArchivo leido correctamente.")
    except FileNotFoundError:
        print("\nError: El archivo con el nombre " + nombredelarchivo + " no se encontró.\n")
    opc0=0
    opc1=-1
    while opc1!=0 :
        opc0=input("----Calculos-----\n1.- Promedio\n2.- Minimo\n3.- Maximo\nElija una de las opciones: ")
        if opc0.isalpha():
            opc1=1
        else:
            opc0=int(opc0)
            if opc0>=1 and opc0<=3:
                opc1=0
    if opc0==1:
        promedio(precio, producto)
    elif opc0==2:
        minimo(precio, producto)
    elif opc0==3:
        maximo(precio, producto)
