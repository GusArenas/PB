import makeup_api
import json
import requests

def prin():
    opc0=0
    opc1=-1
    while opc1!=0:
        opc0=(input("\n ------Categoria------\n1.- Powder\n2.- Cream\n3.- Pencil\n4.- Liquid\n5.- Gel\n6.- Palette\n7.- Concealer\n8.- Contour\n9.- Bb cc\n10.- Mineral\n11.- Highlighter\n12.- Lipstick\n13.- Lip Gloss\n14.- Lip Stain\nElije tu Categoria Favorita: "))
        if opc0.isalpha():
            opc1=1
        else:
            opc0=int(opc0)
            if opc0>=1 and opc0<=14:
                opc1=0
    return opc0
    
def categoria():
    cat=" ";
    numero=int(prin())
    if numero==1:
        cat="powder"
    elif numero==2:
        cat="cream"
    elif numero==3:
        cat="pencil"
    elif numero==4:
        cat="liquid"
    elif numero==5:
        cat="gel"
    elif numero==6:
        cat="palette"
    elif numero==7:
        cat="concealer"
    elif numero==8:
        cat="contour"
    elif numero==9:
        cat="bb_cc"
    elif numero==10:
        cat="mineral"
    elif numero==11:
        cat="highlighter"
    elif numero==12:
        cat="lipstick"
    elif numero==13:
        cat="lip_gloss"
    elif numero==14:
        cat="lip_stain"
    return cat