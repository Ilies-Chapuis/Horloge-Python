import threading
import time
from datetime import datetime, timedelta


current_time = datetime.now()
lock = threading.Lock()
running = True


def afficher_heure():

    global current_time
    while True:

        time.sleep(1)
        with lock:

            current_time += timedelta(seconds=1)
            print(f"Heure actuelle : {datetime.now().strftime('%H:%M:%S')}")
            continue


def alarme_check(alarm_time):

    global running
    while running:
 
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
               
thread = threading.Thread(target=afficher_heure, daemon=True)
thread.start()               



while True:

    commande = input(
        "Commande :\n"
        " - set HH:MM:SS → changer l'heure\n"
        " - alarme → définir une alarme\n"
        " - quit → quitter\n"
    )

    if commande.lower() == "quit": 

        running = False
        break

    if commande.startswith("alarme"):

        alarm_time = alarme_check()
        if alarm_time is None:
            continue

        alarm_thread = threading.Thread(
            target=alarme_check, args=(alarm_time,), daemon=True
        )
        alarm_thread.start()

    if commande.startswith("set"):

        if input("set") == "set":

            heures = int(input("Choisissez l'heure :"))
            if heures < 0 or heures > 23:
                print("Heure invalide")
                continue

            minutes = int(input("Choisissez les minutes :"))
            if minutes < 0 or minutes > 59:
                print("Minutes invalides")
                continue

            secondes = int(input("Choisissez les secondes :"))
            if secondes < 0 or secondes > 59:
                print("Secondes invalides")
                continue

        try:

            _, heure = commande.split()
            h, m, s = map(int, heure.split(":"))

            with lock:
                current_time = current_time.replace(
                    hour=h, minute=m, second=s
                )
            print("Heure modifiée avec succès.")

        except ValueError:
            print("Format invalide. Exemple : set 14:30:00")


print("Programme arrêté.")