import random
import os

def jouer_blackjack():

    #Constantes pour déterminer les cartes existantes
    numeros_carte = list(range(2, 11))
    types_carte = ["Valet", "Dame", "Roi", "As"]

    #Créer le paquet de cartes
    paquet_cartes = []

    for _ in range(4):
        paquet_cartes += numeros_carte
        paquet_cartes += types_carte
    #print(len(paquet_cartes)) pour vérifier qu'il y a bien 52 cartes

    #Fonction pour définir la valeur d'une carte
    def valeur_carte(carte):
        valeurs = {
            "Valet": 10,
            "Dame": 10,
            "Roi": 10,
            "As": [1, 11],
        }

        if isinstance (carte, int) and carte in numeros_carte:
            return carte
        elif carte in types_carte:
            return valeurs[carte]
        else:
            print("Carte inconnue !")
            return 0

    #Fonction pour définir la valeur de la main
    def valeur_main(main):
        total_main = 0
        nombre_as = 0

        for carte in main:
            valeurs = valeur_carte(carte)

            if carte == "As":
                total_main += 11
                nombre_as += 1
            else:
                total_main += valeurs

        while total_main > 21 and nombre_as > 0:
            total_main -= 10
            nombre_as -= 1

        return total_main

    #Mélange et distribue des cartes
    random.shuffle(paquet_cartes)
    main_joueur = [paquet_cartes.pop(), paquet_cartes.pop()]
    main_croupier = [paquet_cartes.pop()]

    while valeur_main(main_croupier) < 17:
        main_croupier.append(paquet_cartes.pop())

    #Annonce des cartes tirées
    print(f"Main du Croupier: {main_croupier}, Valeur: {valeur_main(main_croupier)}")
    print(f"Main du Joueur: {main_joueur}, Valeur: {valeur_main(main_joueur)}")

    #Annonce des résultats de ce premier tirage
    if (valeur_main(main_croupier)) > 21:
        print("Vous avez gagné !")

    elif (valeur_main(main_croupier)) == 21:
        print("Vous avez perdu !")

    elif (valeur_main(main_joueur)) > 21:
        print("Vous avez perdu !")

    elif (valeur_main(main_joueur)) == 21:
        print ("Vous avez gagné !")

    #Demande au Joueur de Tirer ou Non une nouvelle carte
    else:
        while True:
            if valeur_main(main_joueur) >= 21:
                break

            choix_joueur = input("Souhaitez-vous tirer une carte? (O / N): ").strip()
            if choix_joueur == "O":
                carte_tiree = paquet_cartes.pop()
                main_joueur.append(carte_tiree)
                print(f"Main du Croupier: {main_croupier}, Valeur: {valeur_main(main_croupier)}")
                print(f"Main du Joueur: {main_joueur}, Valeur: {valeur_main(main_joueur)}")
                print(f"Vous avez tiré: {carte_tiree}")
            else:
                break

        valeur_joueur = valeur_main(main_joueur)
        valeur_croupier = valeur_main(main_croupier)

        #Annonce des résultats
        if valeur_joueur > 21:
            print("Vous avez perdu !")

        elif valeur_croupier > 21 or valeur_joueur > valeur_croupier:
            print("Vous avez gagné !")

        elif valeur_joueur == valeur_croupier:
            print("Match nul...")

        else:
            print("Vous avez perdu !")

#Donne la possibilité de recommencer le Jeu
while True:
    jouer_blackjack()
    input("Appuyez sur Entrée pour recommencer une partie")
    os.system('cls' if os.name == 'nt' else 'clear')