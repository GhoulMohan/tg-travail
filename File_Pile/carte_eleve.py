from File import *
import random
import bataille
   

VAL_CARTE = ['2','3','4','5','6','7','8','9','10','V','D','R','AS']
COL_CARTE = ['Pique','Trefle','Coeur','Carreau']
       
def comp(c1,c2) :
    """
    Fonction de comparaison entre deux cartes
    param c1 : (tuple) Carte 1
    param c2 : (tuple) Carte 2
    return : Renvoie
                    -1 si => c1 < c2
                    1  si => c1 > <2
                    0  si => c1 == c2
    
    """
    if VAL_CARTE.index(c1[0]) < VAL_CARTE.index(c2[0]) :
        return -1
    elif VAL_CARTE.index(c1[0]) > VAL_CARTE.index(c2[0]) :
        return 1
    else :
        return 0
                    
def creer_jeu():
    """
    Fonction qui crée un jeu aléatoire
    return a,b (File) Deux files contenant 26 cartes chacunes
    """
    paquet = []
    for i in range(13):
        for j in range(4):
            carte = (VAL_CARTE[i],COL_CARTE[j])
            paquet.append(carte)
    random.shuffle(paquet)
    f1 = File()
    f2 = File()
    i = 0
    while i < 52 :
        f1.enfile(paquet[i])
        f2.enfile(paquet[i+1])
        i = i + 2
        
    return f1,f2