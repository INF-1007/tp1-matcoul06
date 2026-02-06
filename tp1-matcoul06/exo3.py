# -*- coding: utf-8 -*-
# Exercice 03 - Choisir le meilleur trajet vers le CEPSUM (gabarit)
"""
Objectif :
- DEMANDER : distance (km, float), attente_navette (min, float), temps_metro (min, float), controle (min, float)
- Valider : toutes les valeurs >= 0
- Calculer les temps bruts (minutes) :
    marche  = distance * 60 / 5 + controle
    navette = attente_navette + distance * 60 / 18 + controle
    metro   = temps_metro + controle
- Arrondir chaque temps a la minute superieure (ceil)
- Determiner la/les option(s) minimale(s)

Sortie :
- 1 option gagnante : "Option la plus rapide : marcher." ou "navette." ou "metro."
- 2 options ex-aequo (ordre : marcher, navette, metro) : "Egalite : X et Y."
- 3 options ex-aequo : "Egalite : marcher, navette et metro."

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Prompts EXACTS :
1) "Entrez la distance jusqu'au CEPSUM (en kilometres) : "
2) "Entrez le temps d'attente de la navette (en minutes) : "
3) "Entrez le temps du trajet en metro (en minutes) : "
4) "Entrez le temps de controle a l'entree (en minutes) : "
"""

# TODO: Importer math
import math
# TODO: Lire les 4 valeurs
try:
    distance=float(input("Entrez la distance jusqu'au CEPSUM (en kilometres) : "))
    attente=float(input("Entrez le temps d'attente de la navette (en minutes) : "))
    metro=float(input("Entrez le temps du trajet en metro (en minutes) : "))
    controle=float(input("Entrez le temps de controle a l'entree (en minutes) : "))
except ValueError:
    print("Erreur - donnees invalides.")
# TODO: Validation


# TODO: Calculer, arrondir (ceil) et determiner le(s) meilleur(s)
marche =(round( distance * 60 / 5 + controle),2)
navette =(round( attente + distance * 60 / 18 + controle),2)
metro = round(metro + controle),2
print(metro)
# TODO: Afficher la phrase exacte
