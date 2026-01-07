import time
import os
from datetime import datetime

# Permet d'afficher l'heure (heure est un tuple)
# :02d sert à forcer l'affichage sur deux chiffres
# end="\r" permet de réécrire sur la même ligne

def afficher_heure(heure):
    h, m, s = heure
    print(f"{h:02d}:{m:02d}:{s:02d}", end="\r")

# Permet de définir l’heure de l’alarme sous forme de tuple
def regler_alarme():
    h = int(input("Heure de l'alarme (0-23) : "))
    m = int(input("Minutes de l'alarme (0-59) : "))
    s = int(input("Secondes de l'alarme (0-59) : "))

    if not (0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59):
        print("Heure invalide")
        return None

    return (h, m, s)

# Heure actuelle de l'ordinateur
maintenant = datetime.now()
heure_actuelle = (maintenant.hour, maintenant.minute, maintenant.second)

# Réglage de l’alarme par l’utilisateur
alarme = regler_alarme()

if alarme is None:
    print("Programme arrêté.")
    exit()

while True:
    h, m, s = heure_actuelle
    afficher_heure(heure_actuelle)

    if heure_actuelle == alarme:
        print("\n⏰ ALARME !!! Réveille-toi Mamie ! ⏰")
        break

    time.sleep(1)

    s += 1
    if s == 60:
        s = 0
        m += 1
    if m == 60:
        m = 0
        h += 1
    if h == 24:
        h = 0

    heure_actuelle = (h, m, s)
