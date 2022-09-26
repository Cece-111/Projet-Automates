def traitementFichier():

    ###---Ouverture et récupération des données du fichier---###
    donnees=open("donnees.txt",'r', encoding='utf-8')
    listeDonnees=donnees.readlines()
    ###------------------------------------------------------###

    ###---Création des listes---###
    indice=[]
    indice2=-1
    listTuple=[]
    listFinale=[]
    numFin=listeDonnees[0].split(" ")
    numFin[1]=numFin[1].split("\n")
    numFin[1]=numFin[1][0]
    for i in range(1,len(listeDonnees)):                # Boucle qui tourne sur toutes les lignes des donnees sauf sur la première

        ###---Séparation des 3 données---###
        listSplit=listeDonnees[i].split(" ")
        listSplit2=listSplit[2].split("\n")
        listSplit[2]=listSplit2[0]
        ###------------------------------###

        ###---Redistribution des données---###
        indice.append(listSplit[0])                     # Remplit indice avec les indices
        tuples=(listSplit[1],listSplit[2])              # Remplit la liste avec les tuples avec les valeurs ex: (a,3)
        listTuple.append(tuples)                        # Ajoute tuples à la list des tples

        indice2+=1                                      # Permet d'aller chercher lebon indice dans indice
        while len(listFinale)<int(indice[indice2])+1:    # Ajoute [] pour pouvoir append les tuples
            listFinale.append([])
        listFinale[int(indice[indice2])].append(tuples)  # Ajoute les tuples dans listFinale de façon ordonné

        ###--------------------------------###
    return(listFinale,numFin)
    ###-------------------------###
    donnees.close()

def cheminPossible(cheminDemande):
    listFinal,numFin=traitementFichier()
    position=[0]                                          # Position de départ
    ###---Gestion des chemins possibles---###
    positionBis=[]
    positionFinal=cheminDemande[-1]
    for indexchemin in cheminDemande:                 # Boucle sur les valeurs du chemin
        for indexPosition in position:                  # Boucle sur lesvaleurs des positions
            for indexListFinal in range(len(listFinal[int(indexPosition)])):        # Boucle sur le nombre d'éléments de la listeFinal de position
                if listFinal[int(indexPosition)][indexListFinal][0]==indexchemin:  # Si le chemin y est compris, il ajoute la position a positionBis
                    positionBis.append(listFinal[int(indexPosition)][indexListFinal][1])
        position=positionBis
        positionBis=[]
    if position==[]:                                    # Si la derniere position n'est pas une position final, il affiche False
        print(False)
    for laFin in numFin:
        for bonnePosition in position:                  # Si la derniere position est une position final, il affiche True
            if bonnePosition==laFin:
                print(True)
    ###------------------------------------###



cheminPossible("ada")

# Code by VIGNAUD Célian, SOMASUNDARAM Jonathan and CIVILISE Noah