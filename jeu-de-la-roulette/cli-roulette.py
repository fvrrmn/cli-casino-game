import random

#Constantes = Pour les limites du plateau et de la roue
numeros_case = list(range(37))
numeros_rouges = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

#Fonction pour obtenir la couleur du numéro
def obtenir_couleur (numero):
    if numero == 0:
        return "Vert"
    elif numero in numeros_rouges:
        return "Rouge"
    else:
        return "Noir"

#Fonction pour faire un pari simple
def faire_pari_simple():
    paris_simples = ["Rouge", "Noir", "Pair", "Impair"]
    
    while True:
        print("Voici la liste des paris disponibles:", paris_simples)
        pari = input("Quel pari souhaitez-vous faire? ").capitalize()

        if pari in paris_simples:
            return pari
        else:
            print("Pari invalide. Choisissez parmi la liste. \n")

#Fonction pour faire tourner la roulette
def tourner_roulette():
    numero_obtenu = random.choice(numeros_case)
    couleur_obtenue = obtenir_couleur(numero_obtenu)
    print(f"La bille s'arrête sur {numero_obtenu} {couleur_obtenue}")
    return numero_obtenu, couleur_obtenue

#Fonction pour Jouer
def jouer():
    pari = faire_pari_simple()
    if pari is None:
        return
    
    numero, couleur = tourner_roulette()

    if pari == couleur:
        print("Gagné !")
    elif pari == "Pair" and numero != 0 and numero % 2 == 0:
        print("Gagné !")
    elif pari == "Impair" and numero % 2 == 1:
        print("Gagné !")
    else:
        print("Perdu !")

#Lancer le Jeu
jouer()   