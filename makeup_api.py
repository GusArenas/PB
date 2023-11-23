import json
import requests
import time
import os
import errno

#url = "http://makeup-api.herokuapp.com/api/v1/products.json"
#response = requests.get(url)


#def makeConsultar() :	
#	if response.status_code == 200:
#		data = response.json()
#		return data
#	else:
#		print("Error al consultar la API")
def crearCarpeta(nombre):
    try:
        os.mkdir(nombre)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

def makePrint(data) :
	#if response.status_code == 200:
	#	data = response.json()
	for item in data:
		print(f"ID: {item['id']},\tCategoria: {item['category']},\tNombre: {item['name']},\tPrecio: {item['price']},\tEtiquetas: {item['tag_list']}\n")
            
def makeWrite(data, carpeta):
    opc0="0"
    nombredelarchivo = 1
    while opc0!="1" and opc0!="2":    
        opc0=(input("\nDesea guardar esta informacion? 1.-Si 2.-No: "))
    opc1=-1
    if(opc0=="1"):
        while opc1!=0:
            nombredelarchivo=input("\nCon que nombre desea guardar el Archivo?(Solo letras del Alpabeto): ")
            if nombredelarchivo.isalpha():
                opc1=0
            else:
                opc1=-1
        try:
            nDA=str(carpeta + nombredelarchivo + "_" + time.strftime("%d") + "_" + time.strftime("%m") + "_" + time.strftime("%Y") + "_" + time.strftime("%H") + "_" + time.strftime("%M"))
            nDAs=str(nombredelarchivo + "_" + time.strftime("%d") + "_" + time.strftime("%m") + "_" + time.strftime("%Y") + "_" + time.strftime("%H") + "_" + time.strftime("%M"))
            with open(nDA + ".txt","w") as archivo:
                for item in data:
                    archivo.write(f"ID: {item['id']},\tCategoria: {item['category']},\tNombre: {item['name']},\tPrecio: {item['price']},\tEtiquetas: {item['tag_list']}\n")
                    #archivo.write(json.loads(data))
                print("Archivo creado correctamente con el nombre " + nDAs + " en la carpeta " + carpeta)
        except FileNotFoundError:
            print("\nError: El archivo no se encontró.\n")

def makeConsultarCategoria(categoria):
    url="http://makeup-api.herokuapp.com/api/v1/products.json?product_category="+categoria
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error al consultar la API")

def makeConsultarMarca(marca):
    url="http://makeup-api.herokuapp.com/api/v1/products.json?brand="+marca
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error al consultar la API")

def makeConsultarEtiqueta(etiqueta):
    url="http://makeup-api.herokuapp.com/api/v1/products.json?product_tags="+etiqueta
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error al consultar la API")

def precioMenorQue(precio):
    url="http://makeup-api.herokuapp.com/api/v1/products.json?price_less_than="+str(precio)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error al consultar la API")

def precioMayorQue(precio):
    url="http://makeup-api.herokuapp.com/api/v1/products.json?price_greater_than="+str(precio)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error al consultar la API")
    
        
def leerInfo():
    nombredelarchivo=input("\nQue archivo quiere ver?(Solo Consultas): ")
    try:
        with open("Consulta/" + nombredelarchivo + ".txt","r") as archivo:
            print("\n" + archivo.read())
            print("\nArchivo leido correctamente.")
    except FileNotFoundError:
        print("\nError: El archivo con el nombre " + nombredelarchivo + " no se encontró.\n")


def reescribirArchivos():
    nombredelarchivo=input("\nQue archivo quiere ver?(Solo Consultas): ")
    try:
        with open("Consulta/" + nombredelarchivo + ".txt","r") as archivo:
            print("\nArchivo leido correctamente.")
            texto=input("\nPor favor escriba lo que quiere agregar al reporte: ")
            try:
                reporte=(nombredelarchivo + "_Reporte_" + time.strftime("%d") + "_" + time.strftime("%m") + "_" + time.strftime("%Y") + "_" + time.strftime("%H") + "_" + time.strftime("%M"))
                with open("Reportes/" + reporte + ".xlsx","a") as archivo1:
                    archivo1.write(archivo.read())
                    archivo1.write("\n\nReporte: " + texto)
                    print("El Reporte se guardo correctamente con el nombre " + reporte + " en la carpeta: Reportes")
            except FileNotFoundError:
                print("\nError: No se pudo acceder a Reportes")
    except FileNotFoundError:
        print("\nError: El archivo con el nombre " + nombredelarchivo + " no se encontró.\n")
        
def leerReportes():
    nombredelarchivo=input("\nQue archivo quiere ver?(Solo Reportes): ")
    try:
        with open("Reportes/" + nombredelarchivo + ".txt","r") as archivo:
            print("\n" + archivo.read())
            print("Archivo leido correctamente.")
    except FileNotFoundError:
        print("\nError: El archivo con el nombre " + nombredelarchivo + " no se encontró.\n")