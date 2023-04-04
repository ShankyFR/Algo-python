infoCrepe = {"Crêpe Confiture Fraise" :  1, 
    'Crêpe Nutela' : 2,
    'Crêpe Sarasin au trois fromage' :  3,
    'Crêpe Sarasin Kebab poulet' : 4,
    'Crêpe Sarasin Jambon Emmental' :5,
    "Crêpe Sarasin Saucisse" : 6
    }
    # Listes dictionnaire des crepes proposées au menu (oui le menu est petit) 

infoCrepePrix = {'Crêpe Confiture Fraise' : 2, 
    'Crêpe Nutela' : 2.5,
    'Crêpe Sarasin au trois fromage' :  8,
    'Crêpe Kebab poulet' : 10,
    'Crêpe Jambon Fromage' : 8,
    'Crêpe Saucisse' : 8    
    }
prixCrepe = [2,2.50,8,10,8,8]
# liste des prix
ingrédientCrêpeConfitureFraise = ["Confiture Fraise"]
ingrédientCrêpeNutela = ["Nutella"]
ingrédientCrêpeSarasinAuTroisFromage = ["Fromage de chèvre","Mozzarella","Cheddar"]
ingrédientCrêpeKebabPoulet = ["Kebab","Poulet",]
ingrédientCrêpeJambonFromage = ["Jambon","Emmental"]
ingérdientsCrêpeSaucisse = ["Saucisse", "Emmental"]
choixCrepe = {"Pate a crepe" : 1.0, "Crepe sarasin" :2.0}
ingrédient = {"Sucre Glace" : 0.5,"Confiture Fraise" : 1.0, "Nutella" : 1.5 ,"Chantilly" :1.0 , "Fromage de chèvre" :2.0 ,"Mozzarella" :2.0 ,
"Cheddar" :2.0 , "Kebab" :4.0 ,"Poulet" :4.0,"Tomate" :1.5,"Emmental": 2.0 , "Jambon" : 4.0, "Saucisse" :4.0}
# Listes des ingrédients dans chaques crepes et les suppléments si le client en demande
panier = 0
choixIngr = []

def liste():
    action = ["liste par ordre alphabetique","liste par prix croissant","crêpe la plus chère","crêpe la moins chère", "Crêpe personnalisée de A à Z", "Pas interressé par le menu"] 
    # Liste pour que le client choisisse comment il veux voir la carte

    print("Faites votre choix pour voir le menu.")

    for i, element in enumerate(action):
        print(i+1, element)
    # Ici le I sert pour permettre au code de commencer au debut de la liste a 1 au lieu de 0 puis ensuite affiche les options possible
    try:
        votreAction = int(input("Entre le chiffre a faire sur la carte: "))
    except ValueError: # cas ou l'utilisateur rentre une action eroné
        return liste()

    match votreAction :
        case 1: # affiche la liste par ordre alphabetique
            sorted(infoCrepe)
            print(infoCrepe)
            try:
                choix = float(input("entre le numero de la crepe voulu: "))
            except ValueError:
                return liste()
            
            panier = choix
            for crep, val in infoCrepe.items():#Cherche le prix de la crêpe selectionnée par le client
                if panier == val:
                    macrepe = crep
                    prix = prixCrepe[val-1]
                    print("Vous avez commander une :", macrepe)
                    print("merci pour votre achat")

                    # Overture du fichier texte et écriture des informations voulu
                    fichier = open("crepe.txt", "w")
                    fichier.write(str("Ma crepe: "))
                    fichier.write(str( macrepe))
                    fichier.write(str(" coute "))
                    fichier.write(str(prix))
                    fichier.write(str("€ et les ingrediants sont "))
                    if val == 1:
                        fichier.write(str(ingrédientCrêpeConfitureFraise))
                    elif val == 2:
                        fichier.write(str(ingrédientCrêpeNutela))
                    elif val == 3:
                        fichier.write(str(ingrédientCrêpeSarasinAuTroisFromage))
                    elif val == 4:
                        fichier.write(str(ingrédientCrêpeKebabPoulet))
                    elif val == 5:
                        fichier.write(str(ingrédientCrêpeJambonFromage))
                    elif val == 6:
                        fichier.write(str(ingérdientsCrêpeSaucisse))                    
                    fichier.close()# fermeture du fichier

        case 2: # affiche la liste par prix croissant
            def tri_selection(tab): # fonction du trie selectif
                for i in range(len(tab)):
                    # Trouver le min
                    min = i
                    for j in range(i+1, len(tab)):
                        if tab[min] > tab[j]:
                            min = j
                                
                    tmp = tab[i]
                    tab[i] = tab[min]
                    tab[min] = tmp
                return tab

            def tri_bulle(tab):# fonction du trie bulle
                n = len(tab)
                # Traverser tous les éléments du tableau
                for i in range(n):
                    for j in range(0, n-i-1):
                        # échanger si l'élément trouvé est plus grand que le suivant
                        if tab[j] > tab[j+1] :
                            tab[j], tab[j+1] = tab[j+1], tab[j]
                return tab

            try:
                trie = int(input("Choissir tri selectif(1) ou tri à bulle(2)"))
            except ValueError: # cas ou l'utilisateur rentre une action eroné
                return liste()

            if trie == 1:# affiche le tri selectif
                tri_selection(prixCrepe)
                trieSelec = sorted(infoCrepePrix.items(), key=lambda t: t[1])
                print(trieSelec)
                liste()
            
            elif trie == 2:# affiche le tri bulle
                tri_bulle(prixCrepe)
                trieBulle = sorted(infoCrepePrix.items(), key=lambda t: t[1])
                print(trieBulle)
                liste()

        case 3: # afficher la crêpe la plus chère
            max = 0
            laCrepe = ""
            for cre , prix in infoCrepe.items():
                if prixCrepe[prix-1] > max:
                    max = prixCrepe[prix-1]
                    laCrepe = cre

            print("La crêpe la plus chère est : " + laCrepe + "pour ", max, "€.")
            liste()

        case 4: # affiche la crêpe la moins chère
            min = 100
            laCrepe = ""
            for cre , prix in infoCrepe.items():
                if prixCrepe[prix-1] < min:
                    min = prixCrepe[prix-1]
                    laCrepe = cre

            print("La crêpe la moins chère est : " + laCrepe + "pour ", min, "€.")
            liste()

        case 5: #crepe personnalisée
            choixIngr = []
            prix = 0
            while True: # donne une condition en fonction de l'entrée donnée
                Confirm = input("T'as fini ta crepe? 1: non 2: oui 3: Supprimer un ingrédient " )
                reponse = int(Confirm)
                # la boucle reviens ici a chaque fois pour avoir la confirmation d'ajout ou suppression d'un ingredient ou si cette phase est finie
                if reponse == 1:
                    # 1 a été tapé donc lance tout la procédure de choix d'ingrédient
                    print("Fait ta crepe comme tu le veux")
                    print(ingrédient)
                    print("Votre crepe")
                    if choixIngr == "":
                        print("Vous avez encore rien mis")
                    else:
                        print(choixIngr)
                    while choixIngr != 0:
                        try:
                            mesIngre = input("Ingrédients voulu: ")
                            choixIngr.append(mesIngre) 
                            prix = prix + ingrédient[mesIngre]
                            break
                        except KeyError :
                            print("Prenez un ingrédient de la liste")
                            # Affiche les ingrédients disponibles (a ecrire comme affichés) ainsi que les ingrédients si il y en a dans la crepe
                            # (le programme pour cette partie n'as pas pu etre fini pour cause d'un manque de disponibilité hors des cours des 2 membres du groupe)
                if reponse == 2:
                    # 2 a été tapé donc lance tout la procédure de choix d'ingrédient
                    print("Quelle crepe tu veux?")
                    print(choixCrepe)
                    maPate = input("La pate a crepe voulu: ")
                    choixIngr.append(maPate)
                    prix = prix + choixCrepe[maPate]
                    #prix = prix + choixIngr
                    print("Vous payerez " + str(prix) + " pour votre crepe au choix contenant : " + str(choixIngr))
                    # Overture du fichier texte et écriture des informations voulu
                    fichier = open("crepe.txt", "w")
                    fichier.write(str("Ma crepe perso coute "))
                    fichier.write(str(prix))
                    fichier.write(str("€ et les ingrediants sont "))
                    fichier.write(str(choixIngr))
                    fichier.close()# fermeture du fichier
                    exit()
                    # lorsque la personne a choisis d'arreter de mettre des ingrédients il peut choisir le type de crepe qu'il veux et ensuite affichera le prix total
                    # (le programme pour cette partie n'as pas pu etre fini pour cause d'un manque de disponibilité hors des cours des 2 membres du groupe)
                if reponse == 3:
                    # 3 a été tapé donc lance tout la procédure de choix d'ingrédient
                    if not choixIngr:
                        print("T'as pas encore commencé ta crepe met y des ingredients avant")
                    else:
                        print(choixIngr)
                        suppIngr = input("Lequel vouslez vous supprimer ? (0 to x) ")
                        del choixIngr[int(suppIngr)]
                        # Cette section permet de supprimer des ingrédients UNIQUEMENT si il y en a
        case 6:
            print("Bonne journée")
            exit()
            # le client etait juste pas satisfait des propositions

liste()