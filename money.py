import makeup_api
import json
import requests

def prin():
    opc0=0
    opc1=-1
    while opc1!=0:
        opc0=(input("\n ------Precio------\nIndique el Precio: "))
        if opc0.isalpha():
            opc1=1
        else:
            opc1=0
            opc0=float(opc0)
            
    return opc0
    
def precio():
    cat=str(prin())
    return cat