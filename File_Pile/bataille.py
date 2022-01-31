from File import *

def tour(f1,f2) :
    """
    Fonction qui simule un tour de bataille
    param f1: (File) File contenant le jeu n°1
    param f2: (File) File contenant le jeu n°2
    return : Aucun retour, la fonction modifie les files
    """
    # On prend la première carte des joueurs
    c1 = f1.defile()
    c2 = f2.defile()
    res = comp(c1,c2)
    if res == -1 :
        f2.enfile(c1)
        f2.enfile(c2)
        print('Joueur 2 a gagné le tour')
    elif res == 1 :
        f1.enfile(c1)
        f1.enfile(c2)
        print('Joueur 1 a gagné le tour')
    else :
        print('Bataille')
        if f1.size() >=3 and  f2.size() >=3 :
            bataille(i,j,f1,f2)
        else :
            # Si un des deux paquet ne peut pas faire la bataille 
            # alors on le vide pour faire gagner l'autre joueur
            if f1.size() < 3 :
                while not f1.est_vide():
                    f1.defile()
            else :
                while not f2.est_vide():
                    f2.defile()
def bataille(c1,c2,f1,f2) :
    """
    Fonction simulant un tour de bataille
    param c1 : (tuple) Carte n°1 égale a c2
    param c2 : (tuple) Carte n°1 égale a c1
    param f1: (File) File contenant le jeu n°1
    param f2: (File) File contenant le jeu n°2
    return : Aucun retour, la fonction modifie les files
    """
    bataille_tab= []
    while comp(c1,c2) == 0:
        bataille_tab.append(c1)
        bataille_tab.append(c2)
        bataille_tab.append(f1.defile())
        bataille_tab.append(f2.defile())
        c1 = f1.defile()
        c2 = f2.defile()
    if comp(c1,c2) == 1 :
        for carte in bataille_tab :
            f1.enfile(carte)
        f1.enfile(c1)
        f1.enfile(c2)
        print('Joueur 1 a gagné le tour')
    if comp(c1,c2) == -1 :
        for carte in bataille_tab :
            f2.enfile(carte)
        f2.enfile(c1)
        f2.enfile(c2)
        print('Joueur 2 a gagné le tour')     

def est_fini(f1,f2):
    """
    Fonction qui détermine si le jeu est fini
    param f1: (File) File contenant le jeu n°1
    param f2: (File) File contenant le jeu n°2
    return (bool): renvoie True si le jeu est fini, False sinon.
    """
    if f1.size() == 0 : 
        print("JOUEUR 2 A GAGNE")
        return True
    elif f2.size() == 0 : 
        print("JOUEUR 1 A GAGNE")
        return True
    else :
        return False


def game(f1,f2):
    """
    Fonction simulant le jeu de la bataille
    param f1: (File) File contenant le jeu n°1
    param f2: (File) File contenant le jeu n°2
    """
    while not est_fini(f1,f2) :
        tour(f1,f2)