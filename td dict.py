velo1 = {"techno" : "velo_electrique", "id" : 1203, "statut" : "en deplacement", "station" : "champ elyse"}
velo2 = {"techno" : "velo_classique", "id" : 1854, "statut" : "dispo"}
velo3 = {"techno" : "velo_classique", "id" : 9532, "statut" : "dispo"}

parc_velibs = [velo1, velo2, velo3]

def recherche_velo():
    for velo in parc_velibs:
        if velo["statut"] == "dispo":
            return True
        else:
            return False

def recherche_velo2():
	velo_dispo = ()
	 for velo in parc_velibs:
        if velo["statut"] == "dispo":
            return velo_dispo = velo_dispo +
        else:
            return False

    
