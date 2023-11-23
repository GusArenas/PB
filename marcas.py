import makeup_api
import json
import requests

def prin():
    opc0=0
    opc1=-1
    while opc1!=0:
        opc0=(input("\n ------Marcas------\n1.- almay\t2.- alva\t3.- anna sui\n4.- annabelle\t5.- benefit\t6.- boosh\n7.- burt's bees\t8.- butter london\t9.- c'est moi\n10.- cargo cosmetics\t11.- china glaze\t12.- clinique\n13.- coastal classic creation\t14.- colourpop\t15.- covergirl\n16.- dalish\t17.- deciem\t18.- dior\n19.- dr. hauschka\t20.- e.l.f.\t21.- essie\n22.- fenty\t23.- glossier\t24.- green people\n25.- iman\t26.- l'oreal\t27.- lotus cosmetics usa\n28.- maia's mineral galaxy\t29.- marcelle\t30.- marienatie\n31.- maybelline\t32.- milani\t33.- mineral fusion\n34.- misa\t35.- mistura\t36.- moov\n37.- nudus\t38.- nyx\t39.- orly\n40.- pacifica\t41.- penny lane organics\t42.- physicians formula\n43.- piggy paint\t44.- pure anada\t45.- rejuva minerals\n46.- revlon\t47.- sally b's skin yummies\t48.- salon perfect\n49.- sante\t50.- sinful colours\t51.- smashbox\n52.- stila\t53.- suncoat\t54.- w3llpeople\n55.- wet n wild\t56.- zorah\t57.- zorah biocosmetiques\nElije tu Marca Favorita: "))
        if opc0.isalpha():
            opc1=1
        else:
            opc0=int(opc0)
            if opc0>=1 and opc0<=57:
                opc1=0
    return opc0
    
def marca():
    cat=" ";
    numero=int(prin())
    if numero==1:
        cat="almay"
    elif numero==2:
        cat="alva"
    elif numero==3:
        cat="anna_sui"
    elif numero==4:
        cat="annabelle"
    elif numero==5:
        cat="benefit"
    elif numero==6:
        cat="boosh"
    elif numero==7:
        cat="burt's_bees"
    elif numero==8:
        cat="butter_london"
    elif numero==9:
        cat="c'est_moi"
    elif numero==10:
        cat="cargo_cosmetics"
    elif numero==11:
        cat="china_glaze"
    elif numero==12:
        cat="clinique"
    elif numero==13:
        cat="coastal_classic_creation"
    elif numero==14:
        cat="colourpop"
    elif numero==15:
        cat="covergirl"
    elif numero==16:
        cat="dalish"
    elif numero==17:
        cat="deciem"
    elif numero==18:
        cat="dior"
    elif numero==19:
        cat="dr._hauschka"
    elif numero==20:
        cat="e.l.f."
    elif numero==21:
        cat="essie"
    elif numero==22:
        cat="fenty"
    elif numero==23:
        cat="glossier"
    elif numero==24:
        cat="green_people"
    elif numero==25:
        cat="iman"
    elif numero==26:
        cat="l'oreal"
    elif numero==27:
        cat="lotus_cosmetics_usa"
    elif numero==28:
        cat="maia's_mineral_galaxy"
    elif numero==29:
        cat="marcelle"
    elif numero==30:
        cat="marienatie"
    elif numero==31:
        cat="maybelline"
    elif numero==32:
        cat="milani"
    elif numero==33:
        cat="mineral_fusion"
    elif numero==34:
        cat="misa"
    elif numero==35:
        cat="mistura"
    elif numero==36:
        cat="moov"
    elif numero==37:
        cat="nudus"
    elif numero==38:
        cat="nyx"
    elif numero==39:
        cat="orly"
    elif numero==40:
        cat="pacifica"
    elif numero==41:
        cat="penny_lane_organics"
    elif numero==42:
        cat="physicians_formula"
    elif numero==43:
        cat="piggy_paint"
    elif numero==44:
        cat="pure_anada"
    elif numero==45:
        cat="rejuva_minerals"
    elif numero==46:
        cat="revlon"
    elif numero==47:
        cat="sally b's_skin_yummies"
    elif numero==48:
        cat="salon_perfect"
    elif numero==49:
        cat="sante"
    elif numero==50:
        cat="sinful_colours"
    elif numero==51:
        cat="smashbox"
    elif numero==52:
        cat="coastal_classic_creation"
    elif numero==53:
        cat="suncoat"
    elif numero==54:
        cat="w3llpeople"
    elif numero==55:
        cat="wet_n_wild"
    elif numero==56:
        cat="zorah"
    elif numero==57:
        cat="zorah biocosmetiques"
    return cat