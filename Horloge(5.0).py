import time
import os
from datetime import datetime
import threading

# ================= VARIABLES GLOBALES =================

pause = False
alarme_declenchee = False

# ================= FONCTIONS =================

# Permet d'afficher l'heure (heure est un tuple)
# :02d sert à forcer l'affichage sur deux chiffres
# end="\r" permet de réécrire sur la même ligne

def afficher_heure(heure, mode):
    h, m, s = heure

    if mode == "12":
        if h == 0:
            h_affiche = 12
            periode = "AM"

        elif h < 12:
            h_affiche = h
            periode = "AM"

        elif h == 12:
            h_affiche = 12
            periode = "PM"

        else:
            h_affiche = h - 12
            periode = "PM"

        print(f"{h_affiche:02d}:{m:02d}:{s:02d} {periode}", end="\r")

    else:
        print(f"{h:02d}:{m:02d}:{s:02d}", end="\r")

# Permet de définir l’heure de l’alarme sous forme de tuple

def regler_alarme():
    h = int(input("Heure de l'alarme (0-23) : "))
    print()

    m = int(input("Minutes de l'alarme (0-59) : "))
    print()

    s = int(input("Secondes de l'alarme (0-59) : "))
    print()

    if not (0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59):
        print("Heure invalide")
        return None

    return (h, m, s)

# Permet d'ajouter une seconde à l'heure

def Temps_hologes(heure_actuelle):
    h, m, s = heure_actuelle

    s += 1
    if s == 60:
        s = 0
        m += 1

    if m == 60:
        m = 0
        h += 1

    if h == 24:
        h = 0

    return (h, m, s)

# ================= THREAD HORLOGE =================

# Threading permet de faire plusieurs choses “en même temps” dans un même programme.
# (exemple pour ce code ci: Une partie du programme affiche l’horloge (def horloge)\
# l'autre partie écoute le clavier (def clavier))


def thread_horloge():
    global heure_actuelle, alarme_declenchee, pause

    while True:
        if not pause:
            afficher_heure(heure_actuelle, mode)

            if heure_actuelle == alarme and not alarme_declenchee:
                alarme_declenchee = True
                print()
                print()
                print(" ALARME !!! Réveille-toi Mamie ! ")
                print()

            heure_actuelle = Temps_hologes(heure_actuelle)

        time.sleep(1)

# ================= THREAD CLAVIER =================

def thread_clavier():
    global pause

    while True:
        print()
        commande = input("Appuyer sur 'p' pour pause ou 'r' pour reprendre : ")

        if commande == "p":
            pause = True
            print("Horloge en pause")

        elif commande == "r":
            pause = False
            print("Horloge reprise")

# ================= PROGRAMME PRINCIPAL =================

print()
print("=== Horloge de Mamie ===")
print()

# Choix du mode d'affichage
mode = input("Veuillez choisir le mode d'affichage (12 ou 24) : ")
print()

# Réglage de l’alarme
alarme = regler_alarme()

if alarme is None:
    print("Programme arrêté.")
    exit()

# Heure actuelle de l'ordinateur
maintenant = datetime.now()
heure_actuelle = (maintenant.hour, maintenant.minute, maintenant.second)

# Lancement des threads
thread1 = threading.Thread(target=thread_horloge)
thread2 = threading.Thread(target=thread_clavier)

thread1.start()
thread2.start()

#(Important ne pas utiliser d'input cela bloque le programme lorsqu'il y a une interaction pause pour l'horloge)