import sys
import json
import requests
import os
import errno
import makeup_api
import categorias
import marcas
import etiquetas
import money
import informacion
import graficas
import reportes

makeup_api.crearCarpeta("Consulta")
makeup_api.crearCarpeta("Reportes")
makeup_api.crearCarpeta("Graficas")

#Variables
opc0="0"

def make(data, carpeta):
    makeup_api.makePrint(data)
    makeup_api.makeWrite(data, carpeta)


while opc0!="10" :
    opc0=input("\n------Menu Principal------ \n1.- Consultas en MakeUp\n2.- Ver la Informacion guardada anteriormente de Consulta\n3.- Hacer reporte sobre consultas guardadas\n4.- Leer los Reportes Almacenados\n5.- Analizar la informacion\n6.- Visualizar la informacion en graficas\n10.- Salir\n-Eliga lo que quiere hacer:")
    
    if opc0=="1" :
        opc1="0"
        while opc1!="10":
            opc1=(input("\n1.- Consultar Productos por Categoria\n2.- Consultar Productos por Marca\n3.- Consultar Productos por Etiqueta\n4.- Consultar por Precio Menor Que\n5.- Consultar por Precio Mayor Que\n10.- Atras\nElija lo que quiere consultar:"))
            if opc1=="1":
                cat=categorias.categoria()
                data = makeup_api.makeConsultarCategoria(cat)
                make(data, "Consulta/")
            elif opc1=="2":
                cat=marcas.marca()
                data = makeup_api.makeConsultarMarca(cat)
                make(data, "Consulta/")
            elif opc1=="3":
                cat=etiquetas.etiqueta()
                data = makeup_api.makeConsultarEtiqueta(cat)
                make(data, "Consulta/")
            elif opc1=="4":
                print("\n--Precio Menor Que")
                cat=money.precio()
                data = makeup_api.precioMenorQue(cat)
                make(data, "Consulta/")
            elif opc1=="5":
                print("\n--Precio Mayor Que")
                cat=money.precio()
                data = makeup_api.precioMayorQue(cat)
                make(data, "Consulta/")
    
    elif opc0=="2" :
        makeup_api.leerInfo()
    elif opc0=="3" :
        reportes.reescribirArchivos()
    elif opc0=="4" :
        reportes.leerReportes()
    elif opc0=="5" :
        informacion.leerInfo()
    elif opc0=="6" :
        graficas.graf0()
    elif opc0=="10" :
        print("Cerrado con exito. :)")
        sys.exit(0)
    
    opc0=0;
