systeme_pieces = [200, 100, 50, 20, 10, 5, 2, 1]
    
def rendu_monnaie(rendu, systeme_pieces):
    """
    description: rendu de la monnaie
    parametre : int,lst
    renvoie: ca renvoie une liste des pieces qu'on va prendre
    >>> rendu_monnaie(55, systeme_pieces)
    [50, 5]
    >>> rendu_monnaie(43, systeme_pieces)
    [20, 20, 2, 1]
    """
    liste_piece = []
    i = 0
    while rendu > 0:
        valeur = systeme_pieces[i]
        if rendu < valeur:
            i = i + 1
        else:
            liste_piece.append(valeur)
            rendu = rendu - valeur
    return liste_piece
     
     
if __name__ == '__main__':
    # Validation des tests
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
