import random
from collections import Counter

# 1. Le Joueur mise un montant
# 2. La machine génère 3 symboles aléatoires
# 3. La combinaison est évaluée :
    # 3 Symboles identiques = Jackpot
    # 2 Symboles identiques = Petit gain
    # Aucune combinaison = Perdu
# 4. On affiche le résultat et les gains éventuels

symboles = ["🍒", "🍋", "🔔", "💎", "7️⃣"]
multiplicateurs_3 = {
"7️⃣": 7,
"💎": 3,
"🔔": 2,
"🍋": 2,
"🍒": 2    
}
multiplicateur_2 = 1.5
solde = 1000

#Fonction pour miser un montant
def miser(solde):
    while True:  
        mise = float(input(f"Combien voulez-vous miser ? (Vous avez : {solde}) € "))

        if mise > solde:
            print(f"Impossible ! Il vous reste {solde} € ")

        elif mise <= 0:
            print("La mise doit être supérieure à 0.")

        elif mise <= solde:
            solde -= mise
            print(f"Vous avez misé {mise} € ")
            print(f"Il vous reste {solde} € ")  
            return mise, solde
        
#Fonction pour générer 3 symboles aléatoires
def generer_symboles(mise):
    tirage = random.choices(symboles, k=3)
    print(f"Le tirage est : {tirage}")
    #Analyse des combinaisons
    combinaison = Counter(tirage)

    for symbole, count in combinaison.items():
        if count == 3:
            print("Jackpot! 3 Symboles identiques ! ")
            gain = mise * multiplicateurs_3[symbole]
            return gain
           
    for symbole, count in combinaison.items():
        if count == 2:
            print("Pas mal, 2 Symboles identiques ! ")
            gain = mise * multiplicateur_2
            return gain
    
    print("Tu as perdu ! ")
    return 0

#Fonction pour mettre une pause pour lancer la machine à sous par soi-même
def pause (mise, solde):
    input("Appuyez sur Entrée pour lancer la machine à sous... ")
    gain = generer_symboles(mise)
    solde += gain
    print(f"Gain : {gain} € ")
    print(f"Il vous reste {solde} € ")
    return solde

#Boucle pour Rejouer
while solde > 0 :
    mise, solde = miser(solde)
    solde = pause(mise, solde)

    if solde <= 0:
        print("Vous n'avez plus d'argent... Fin de la partie. ")
        break

    choix = input("Voulez-vous rejouer ? O/N ").strip().lower()
    if choix != "o":
        print("Merci d'avoir Joué ! ")
        break