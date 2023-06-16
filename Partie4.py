def saisie():
    t = []
    while True:
        nom = input("Entrez le nom de la personne (ou 'q' pour quitter) : ")
        if nom == "q":
            break
        t.append({"nom": nom, "annee": 0, "temps": 0})
    return t
import random
def calculAnnee(t):
    for personne in t:
        annee_min = personne["annee"] - 10
        annee_max = personne["annee"] + 10
        periode = input(f"{personne['nom']}, dans quelle période souhaitez-vous faire un voyage dans le temps (entre {annee_min} et {annee_max}) ? ")
        periode_split = periode.split("-")
        annee_debut = int(periode_split[0])
        annee_fin = int(periode_split[1])
        personne["annee"] = random.randint(annee_debut, annee_fin)
def saisie():
    t = []
    while True:
        nom = input("Entrez le nom de la personne (ou 'q' pour quitter) : ")
        if nom == "q":
            break
        t.append({"nom": nom, "annee": 0, "temps": 0})
    return t
def calculTemps(t):
    for personne in t:
        annee_depart = personne["annee"]
        personne["temps"] = abs(2017 - annee_depart) * 10
def affichage(t):
    for personne in t:
        print(f"Nom: {personne['nom']}, Année: {personne['annee']}, Temps: {personne['temps']} secondes")
    print(affichage(t))
#programme principal
personnes = saisie()
calculAnnee(personnes)
calculTemps(personnes)
affichage(personnes)

