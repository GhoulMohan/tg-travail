from visualisation_arbre import *
from random import randint

# PARTIE 1 - TRAVAIL PRELIMINAIRE Question 2
arbre = [2, [8, [6, [], []], [9, [], []]], [1, [7, [], []], []]]
show(arbre, "arbre_du_cours")

# PARTIE 1 - TRAVAIL PRELIMINAIRE Question 3
arbre_feuille = [1, [], []]
show(arbre_feuille, "feuille")

# # PARTIE 2 - CODE ET TESTS A ECRIRE


def est_vide(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Détermine si un arbre est vide
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (bool) : True si l'arbre est vide, False sinon
    
    TESTS :
    >>> est_vide([])
    True
    >>> est_vide([1, [], [])
    False
    >>> est_vide([2, [8, [6, [], []], [9, [], []]], [1, [7, [], []], []]])
    False
    '''
    return arbre == []

def est_feuille(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Détermine si l'arbre est une feuille
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (bool) : True si l'arbre est une feuille, False sinon
    
    TESTS :
    >>> est_feuille([])
    True
    >>> est_feuille([2, [8, [6, [], []], [9, [], []]], [1, [7, [], []], []]])
    False
    >>> est_feuille([1, [], [])
    True
    '''
    if arbre == [1, [], []]:
        return True
    else:
        return False  

def racine(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Renvoie la valeur du noeud racine
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (int, str, etc...) : Valeur du noeud racine
    précondition : arbre != 0
    
    TESTS :
    >>> racine([2, [8, [6, [], []], [9, [], []]], [1, [7, [], []], []]])
    2
    >>> racine([1, [], []])
    1
    '''
    # Vérification de la précondition (voir énoncé : remarques importantes sur le travail)
    assert est_vide != 0 , "l'arbre ne peut etre vide"
    # Code de la fonction à compléter
    return racine[0]
    

def SAG(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Renvoie le sous-arbre gauche de l'arbre
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (list) : sous-arbre gauche
    précondition : arbre != 0
    
    TESTS :
    >>> SAG([2, [8, [6, [], []], [9, [], []]], [1, [7, [], []], []]])
    [2, [8, [6, [], []], [9, [], []]
    >>> SAG([1, [], []])
    []
    '''
    # Vérification de la précondition (voir énoncé : remarques importantes sur le travail)
    assert est_vide != 0 ," l'arbre ne peut etre vide"
    # Code de la fonction à compléter
    return racine[1]

def SAD(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Renvoie le sous-arbre droit de l'arbre
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (list) : sous-arbre droit
    précondition : arbre != 0
    
    TESTS :
    >>> SAD([2, [8, [6, [], []], [9, [], []]], [1, [7, [], []], []]])
    [1, [7, [], []], []]])
    >>> SAD([1, [], []])
    []
    '''
    # Vérification de la précondition (voir énoncé : remarques importantes sur le travail) 
    assert est_vide != 0, "l'arbre ne peut etre vide"
    # Code de la fonction à compléter
    return racine[2]

def taille(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Calcule la taille d'un arbre
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (int) : Taille de l'arbre
    
    TESTS :
    >>> taille([2, [8, [6, [], []], [9, [], []]], [1, [7, [], []], []]])
    6
    >>> taille([1, [], []])
    1
    >>> taille([])
    0
    '''
    if not est_vide(arbre):
        return 0
    else:
        return 1 + taille(arbre(SAG)) + taille(arbre(SAD))
    
def hauteur(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Calcule la hauteur d'un arbre en respectant la convention
            donnée dans l'énoncé
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (int) : Hauteur de l'arbre
    
    TESTS :
    >>> hauteur([2, [8, [6, [], []], [9, [], []]], [1, [7, [], []], []]])
    
    >>> hauteur([1, [], []])
    
    >>> hauteur([])
    '''
    if arbre == None:
        return -1
    return 1 + max(hauteur(SAG(arbre)), hauteur(SAD(arbre)))

def cree_arbre_complet(h, maxi):
    '''
    DOCUMENTATION :
    Description de la fontion : crée un arbre complet de hauteur h
            avec des valeurs de noeud aléatoires comprises entre 0 et maxi inclus
    h (int) : hauteur de l'arbre
    maxi (int) : valeur maximale des noeuds
    return (list) : arbre créé
    '''
    

def cree_peigne_gauche(h, maxi):
    '''
    DOCUMENTATION :
    Description de la fontion : crée un arbre peigne gauche de hauteur h
            avec des valeurs de noeud aléatoires comprises entre 0 et maxi inclus
    h (int) : hauteur de l'arbre
    maxi (int) : valeur maximale des noeuds
    return (list) : arbre créé
    '''
    if h == 0:
        return None
    else:
        return racine("", SAG = cree_peigne_gauche(h - 1))

def cree_peigne_droit(h, maxi):
    '''
    DOCUMENTATION :
    Description de la fontion : crée un arbre peigne droit de hauteur h
            avec des valeurs de noeud aléatoires comprises entre 0 et maxi inclus
    h (int) : hauteur de l'arbre
    maxi (int) : valeur maximale des noeuds
    return (list) : arbre créé
    '''
    if h == 0:
        return None
    else:
        return racine("", SAG = cree_peigne_droite(h - 1))

def est_egal(arbre1, arbre2):
    '''
    DOCUMENTATION :
    Description de la fontion : détermine si deux arbres sont identiques ou différents
    arbre1 (list) : Arbre implémenté sous forme de listes imbriquées
    arbre2 (list) : Arbre implémenté sous forme de listes imbriquées
    return (bool) : True si les deux arbres sont identiques, False sinon 
    
    TESTS :
    '''
    # A compléter

if __name__ == '__main__':
    # Lancement des tests (laisser ces deux lignes de code inchangées)
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
    
    # PARTIE 2 - Question 3
    
    # Creation d'un arbre complet de hauteur 3
        # A compléter
    
    # Creation d'un peigne gauche de hauteur 3
        # A compléter
    
    # Creation d'un peigne droit de hauteur 3
        # A compléter
    
    # PARTIE 2 - Question 4 
    # A compléter.ghoul