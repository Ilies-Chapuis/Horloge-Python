import time
from datetime import datetime

# affiche l'heure
heures = 0
minutes = 0
secondes = 0

def afficher_heure(heures, minutes, secondes):
    heures = int(input("Choisissez l'heure :"))
    if heures < 0 or heures > 23:
        return "Heure invalide"
    
    minutes = int(input("Choisissez les minutes :"))
    if minutes < 0 or minutes > 59:
        return "Minutes invalides"
    
    secondes = int(input("Choisissez les secondes :"))
    if secondes < 0 or secondes > 59:
        return "Secondes invalides"
    
    affichage = f"{heures:02}:{minutes:02}:{secondes:02}"
    return affichage


print(afficher_heure(heures, minutes, secondes))
time.sleep(1)