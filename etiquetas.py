import makeup_api
import json
import requests

def prin():
    opc0=0
    opc1=-1
    while opc1!=0:
        opc0=(input("\n ------Etiquetas------\n1.-Canadian\t\t2.-CertClean\t\t3.-Chemical Free"\
        "\n4.-Dairy Free\t\t5.-EWG Verified\t\t6.-EcoCert"\
        "\n7.-Fair Trade\t\t8.-Gluten Free\t\t9.-Hypoallergenic"\
        "\n10.-Natural\t\t11.-No Talc\t\t12.-Non-GMO"\
        "\n13.-Organic\t\t14.-Peanut Free Product\t15.-Sugar Free"\
        "\n16.-USDA Organic\t17.-Vegan\t\t18.-alcohol free"\
        "\n19.-cruelty free\t20.-oil free\t\t21.-purpicks"\
        "\n22.-silicone free\t23.-water free"\
        "\nElije tu Etiqueta Favorita: "))
        if opc0.isalpha():
            opc1=1
        else:
            opc0=int(opc0)
            if opc0>=1 and opc0<=23:
                opc1=0
    return opc0
    
def etiqueta():
    cat=" ";
    numero=int(prin())
    if numero==1:
        cat="Canadian"
    elif numero==2:
        cat="CertClean"
    elif numero==3:
        cat="Chemical_Free"
    elif numero==4:
        cat="Dairy_Free"
    elif numero==5:
        cat="EWG_Verified"
    elif numero==6:
        cat="EcoCert"
    elif numero==7:
        cat="Fair_Trade"
    elif numero==8:
        cat="Gluten_Free"
    elif numero==9:
        cat="Hypoallergenic"
    elif numero==10:
        cat="Natural"
    elif numero==11:
        cat="No_Talc"
    elif numero==12:
        cat="Non_GMO"
    elif numero==13:
        cat="Organic"
    elif numero==14:
        cat="Peanut_Free_Product"
    elif numero==15:
        cat="Sugar_Free"
    elif numero==16:
        cat="USDA_Organic"
    elif numero==17:
        cat="Vegan"
    elif numero==18:
        cat="alcohol_free"
    elif numero==19:
        cat="cruelty_free"
    elif numero==20:
        cat="oil_free"
    elif numero==21:
        cat="purpicks"
    elif numero==22:
        cat="silicone_free"
    elif numero==23:
        cat="water_free"
    return cat