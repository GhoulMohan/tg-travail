def occurence(texte):
    dico = []
    for c in texte:
        if c not in dico_keys():
            dico[c] = 1
        else:
            dicoc[c] += 1
            
    return dico

def lecture(nom_fichier):
    """
    description : ouvre un fichier texte et renvoie son contenu sous la forme d'une chaîne de caractère
    paramètre nom_fichier(str) : nom du fichier
    return (str) : contenu du fichier
    """
    with open(nom_fichier,'r') as fichier:
        return fichier.read()


def occurence_lower(texte):
    dico = []
    for c in lower:
        if c not in dico_keys() and c not in  ",;:!?.’«»- \n":
            dico[c] = 1
        elif c not in  ",;:!?.’«»- \n":
            dicoc[c] += 1
            
    return dico