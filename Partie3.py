#fonction nbMotsAvecVoyelle(nomf)
def nbMotsAvecVoyelle(nomf):
    voyelles = ['a', 'e', 'i', 'o', 'u']
    nb_mots = 0
    with open(nomf, 'r') as fichier:
        for ligne in fichier:
            mot = ligne.strip()
            if mot[0] in voyelles:
                nb_mots += 1
    return nb_mots
#compterChaqueMot(nomf1,nomf)
def compterchaqueMot(nomf1, nomf2):
    with open(nomf1, 'r') as fichier1, open(nomf2, 'w') as fichier2:
        mot_precedent = ""
        compteur = 0

        for ligne in fichier1:
            mot = ligne.strip()

            if mot == mot_precedent:
                compteur += 1
            else:
                if mot_precedent != "":
                    fichier2.write(mot_precedent + " " + str(compteur) + "\n")
                mot_precedent = mot
                compteur = 1

        fichier2.write(mot_precedent + " " + str(compteur) + "\n")

