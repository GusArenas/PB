import json
import requests
import time
import os
import errno
import matplotlib.pyplot as plt
import numpy as np
import re

def graf0():
    precio = []
    producto = []
    categoria = []
    nombredelarchivo=input("\nQue archivo quiere comprobar informacion?(Solo Consultas): ")
    try:
        with open("Consulta/" + nombredelarchivo + ".txt","r") as archivo:
            for linea in archivo:
                print(linea)
                principio=linea.find(",\tCategoria:")
                fin=linea.find(",\tNombre:")
                categoria.append(linea[principio+13:fin])
                principio=linea.find("Nombre:")
                fin=linea.find(",\tPrecio:")
                producto.append(linea[principio+8:fin])
                principio=linea.find("Precio:")
                fin=linea.find(",\tEtiquetas:")
                precio.append(float(linea[principio+8:fin]))
            for numero in range(len(categoria)):
                print(categoria[numero] + " - " + producto[numero] + " - " + str(precio[numero])) 
            print("\n\nArchivo leido correctamente.")
    except FileNotFoundError:
        print("\nError: El archivo con el nombre " + nombredelarchivo + " no se encontró.\n")

    opc0=0
    opc1=-1
    while opc1!=0 :
        opc0=input("----Graficas-----\n1.- Mayor que el promedio\n2.- Productos mas caros\n3.- Categorias mas caras\nElija una de las opciones: ")
        if opc0.isalpha():
            opc1=1
        else:
            opc0=int(opc0)
            if opc0>=1 and opc0<=3:
                opc1=0
    if opc0==1:
        promedio=sum(precio)/len(precio)    
        mejor=0
        for numero in range(len(categoria)):
            if precio[numero]>=promedio :
                mejor+=1
        plt.pie([float(len(precio))-mejor,(mejor)], labels=['Precio bajo el promedio','Por encima del promedio'], autopct='%1.1f%%', startangle=90)
        plt.title('Grafico del Archivo: ' + nombredelarchivo)
        plt.show()
    elif opc0==2:
        plt.hist(precio, len(producto), edgecolor="black")
        plt.xlabel("Valor")
        plt.ylabel("Frecuencia")
        plt.title("Histograma de Datos recolectados del Archivo: " + nombredelarchivo)
        plt.show()
        
    elif opc0==3:
        plt.bar(categoria, precio, color='orange')
        plt.xlabel("Categorias")
        plt.ylabel("Valores")
        plt.title("Grafico del Archivo: " + nombredelarchivo)
        plt.show()
        
    opc0=0
    opc1=-1
    while opc1!=0 :
        opc0=input("Desea Guardar la grafica aqui generada? 1.-Si 2.-No: ")
        if opc0.isalpha():
            opc1=1
        else:
            opc0=int(opc0)
            if opc0>=1 and opc0<=2:
                opc1=0
    if opc0==1:
        while opc1!=-1:
            nombredelarchivo=input("\nCon que nombre desea guardar el Archivo?(Solo letras del Alpabeto): ")
            if nombredelarchivo.isalpha():
                opc1=-1
            else:
                opc1=0
        nDAs=str("_" + time.strftime("%d") + "_" + time.strftime("%m") + "_" + time.strftime("%Y") + "_" + time.strftime("%H") + "_" + time.strftime("%M"))
        plt.savefig("Graficas/" + nombredelarchivo+nDAs)
        print("\nLa grafica se guardo con exito en la carpeta de graficas con el nombre:"+ nombredelarchivo + nDAs)