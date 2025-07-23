## 🃏 Blackjack

- [x] Créer un paquet : 52 cartes
- [x] Assigner une valeur : Pour chaque carte
- [x] Mélange et Distribution des cartes : Croupier et Joueur
- [x] Calcul : Valeur et Somme des cartes et de la main
- [x] Choix du Joueur : Tirer ou Rester ( O / N )
- [x] Résultat affiché : Gagné ou Perdu ou Nul
- [x] Recommencer une partie
 
---

### Règles 

Le but est d'avoir une main dont la valeur totale est la plus proche de 21 sans la dépasser tout étant au dessus de celle du Croupier.

Vous commencez avec 2 cartes en main.

Le Croupier tire automatiquement Jusqu’à atteindre au moins 17.

Vous pouvez choisir de tirer une nouvelle carte ou de rester.

- Si vous dépassez 21, vous avez **Perdu**.
- Si le croupier dépasse 21, vous avez **Gagné**.
- Si vous avez une main plus forte que le croupier sans dépasser 21, vous avez **Gagné**.
- Si vos mains sont égales alors... **Match nul** !
- Sinon, vous avez **Perdu**

---

### Valeur des cartes

**2 à 10** : Valeur faciale (2 = 2, 7 = 7)

**Valet, Dame, Roi** : 10 points

**As** : 1 ou 11 selon ce qui est le plus avantageux pour votre main

---

```bash
python3 Jeu_Blackjack.py
