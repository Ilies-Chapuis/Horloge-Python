import threading
import winsound
import os
import msvcrt

dictionnaire = {"heure" : 0, "minute" : 0, "seconde" : 0}
alarme = {"heure_alarme" : dictionnaire["heure"]+1, "minute_alarme" : dictionnaire["minute"]+1, "seconde_alarme" : dictionnaire["seconde"]+1}

DOSSIER_SCRIPT = os.path.dirname(os.path.abspath(__file__)) #Compliqué mais ça sert à dire ou se trouve le fichier son pour python.
CHEMIN_SON = os.path.join(DOSSIER_SCRIPT, "alarme.wav")

def horloge(dictionnaire,alarme):

    while True:
        threading.Event().wait(1) #Sert à attendre 1 seconde à chaque répétition.

        ## ALARME ##
        if alarme["heure_alarme"] == dictionnaire["heure"] and alarme["minute_alarme"] == dictionnaire["minute"] and alarme["seconde_alarme"] == dictionnaire["seconde"]:
            winsound.PlaySound(CHEMIN_SON, winsound.SND_FILENAME) #+ " | winsound.SND_ASYNC" si non bloquant.
        ## ALARME ##

        ## FONCTIONNEMENT ##
        if dictionnaire["seconde"] == 59: #Vérification des secondes.
            dictionnaire["seconde"] = -1
            dictionnaire["minute"] += 1
        
        if dictionnaire["minute"] == 60: #Vérification des minutes + Des heures.
            dictionnaire["minute"] = 0
            if dictionnaire["heure"] == 12:
                dictionnaire["heure"] = 1
            else:
                dictionnaire["heure"] += 1

        dictionnaire["seconde"] += 1 #Ajout des secondes.
        print(f"{dictionnaire["heure"]:02d}:{dictionnaire["minute"]:02d}:{dictionnaire["seconde"]:02d}", end="\r")
        ## FONCTIONNEMENT ##

        ## MODIFICATION ##
        if msvcrt.kbhit():
            touche = msvcrt.getch()
            if touche == b' ':
                demander_valeur()
            if touche == b'a':
                demander_alarme()
        ## MODIFICATION ##


def demander_valeur():
    heure = int(input("Entrez une valeur (heure) : ") or dictionnaire["heure"])
    minute = int(input("Entrez une valeur (minute) : ") or dictionnaire["minute"])
    seconde = int(input("Entrez une valeur (seconde) : ") or dictionnaire["seconde"])

    dictionnaire["heure"] = heure
    dictionnaire["minute"] = minute
    dictionnaire["seconde"] = seconde

def demander_alarme():

    heure = int(input(f"Entrez l'heure de votre Alarme : ") or dictionnaire["heure"]+1)
    minute = int(input(f"Entrez les minutes de votre Alarme : ") or dictionnaire["minute"]+1)
    seconde =  int(input(f"Entrez les secondes de votre Alarme : ") or dictionnaire["seconde"]+1)

    alarme["heure_alarme"] = heure
    alarme["minute_alarme"] = minute
    alarme["seconde_alarme"] = seconde

horloge(dictionnaire,alarme)