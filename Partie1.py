"""
def saisie_tab():
    annuaire = []
    while True:
        personne = {}
        personne['nom'] = input("Nom: ")
        personne['prenom'] = input("Prénom: ")
        personne['numero_rue'] = input("Numéro dans la rue: ")
        personne['nom_rue'] = input("Nom de rue: ")
        personne['num_tel'] = input("Numéro de téléphone: ")
        personne['code_postal'] = input("Code postal: ")
        personne['ville'] = input("Ville: ")
        annuaire.append(personne)
        continuer = input("Voulez-vous ajouter une autre personne à l'annuaire ? (oui/non) ")
        if continuer.lower() != 'oui':#lower() méthode de chaîne de caractères (string) qui renvoie une nouvelle chaîne où tous les caractères alphabétiques sont convertis en minuscules.
            break
    return annuaire
def critere_recherche():
    print("Quelle critère de recherche choisissez-vous?")
    print("1. Nom")
    print("2. Prénom")
    print("3. Numéro de téléphone")
    print("4. Code postal")
    print("5. Ville")
    choix = input("Entrez votre choix entre 1-5: ")
    return choix
def recherche(annuaire, critere):
    recherche = input("Saisisser la valeur de recherche: ")
    resultats = []
    for personne in annuaire:
        if personne[critere] == recherche:
            resultats.append(True)
        else:
            resultats.append(False)
    return resultats
def affiche_tab(annuaire, resultats):
    print("Résultats de la recherche:")
    for personne, resultat in zip(annuaire, resultats):#for...zip() permetde parcourir les listes et de regrouper les éléments de plusieurs itérables (listes) 
        if resultat:
            print("Nom: ", personne['nom'])
            print("Prénom: ", personne['prenom'])
            print("Numéro dans la rue: ", personne['numero_rue'])
            print("Nom de rue: ", personne['nom_rue'])
            print("Numéro de téléphone: ", personne['num_tel'])
            print("Code postal: ", personne['code_postal'])
            print("Ville: ", personne['ville'])
            print(affiche_tab)
"""
def saisie_tab():
    annuaire = []
    while True:
        personne = {}
        personne["nom"] = input("Nom: ")
        personne["prenom"] = input("Prénom: ")
        personne["numero"] = input("Numéro dans la rue: ")
        personne["nom_rue"] = input("Nom de rue: ")
        personne["num_tel"] = input("Numéro de téléphone: ")
        personne["code_postal"] = input("Code postal: ")
        personne["ville"] = input("Ville: ")
        annuaire.append(personne)

        continuer = input("Souhaitez-vous ajouter une autre personne à l'annuaire ? (oui/non): ")
        if continuer.lower() != "oui":
            break

    return annuaire

def critere_recherche():
    critere = input("Choisissez le critère de recherche (nom, prenom, nom_rue, num_tel, code_postal, ville): ")
    return critere.lower()

def recherche(annuaire, critere):
    recherche = input("Entrez la valeur de recherche: ")
    resultat = [False] * len(annuaire)

    for i, personne in enumerate(annuaire):
        if recherche.lower() in personne[critere]:
            resultat[i] = True

    return resultat

def affiche_tab(annuaire, resultat):
    print("resultat de la recherche")
    for i, personne in enumerate(annuaire):
        if resultat[i]:
            print("Nom:", personne["nom"])
            print("Prénom:", personne["prenom"])
            print("Numéro dans la rue:", personne["numero"])
            print("Nom de rue:", personne["nom_rue"])
            print("Numéro de téléphone:", personne["num_tel"])
            print("Code postal:", personne["code_postal"])
            print("Ville:", personne["ville"])
            print(affiche_tab)

annuaire = saisie_tab()

while True:
    critere = critere_recherche()
    resultat = recherche(annuaire, critere)
    affiche_tab(annuaire, resultat)

    continuer = input("Souhaitez-vous effectuer une nouvelle recherche ? (oui/non): ")
    if continuer.lower() != "oui":
        break

# Programme principal
annuaire = saisie_tab()
critere = critere_recherche()
resultats = recherche(annuaire, critere)
affiche_tab(annuaire, resultats)
