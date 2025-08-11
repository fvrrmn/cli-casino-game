<div align="center">

## 🎰 Machine à sous

</div>

```bash
python3 cli-machine-a-sous.py
```

- [x] Définir un solde de départ : 1000 €
- [x] Définir des symboles : 🍒, 🍋, 🔔, 💎, 7️⃣
- [x] Assigner un multiple : Pour chaque symbole
- [x] Mise d'un montant : Joueur
- [x] Évaluer : Combinaisons gagnantes
- [x] Calcul : Gain selon le multiplicateur associé
- [x] Actualiser : Solde
- [x] Choix du Joueur : Continuer de miser ou Arrêter de Jouer
 
---

### 📜 Règles 

*Le but est d’aligner des symboles identiques pour remporter le plus de gains possibles.*

- Vous misez un montant dans la limite de votre solde.
- La machine tire 3 symboles au hasard parmi la liste disponible.
- Les gains dépendent de la combinaison obtenue.
- La partie continue tant que vous avez de l'argent disponible ou Jusqu'à ce que vous quittez la partie.

---

### 🂠 Valeur des gains

<div align="center">

| Combinaison           | Multiplicateur |
| --------------------- | -------------- |
| 3 × 7️⃣                | ×7             |
| 3 × 💎                | ×3             |
| 3 × 🔔                | ×2             |
| 3 × 🍋                | ×2             |
| 3 × 🍒                | ×2             |
| 2 symboles identiques | ×1.5           |
| Aucune combinaison    | 0 €            |

</div>

