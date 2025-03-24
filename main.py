# pip install nuitka

import os, subprocess, sys

print("Programme fait par NatCode (@NatCode sur youtube)")
print()
print("Mes sites :")
print("   - https://natcode.fr.to/")
print("   - https://project-sharing.fr.to/")
print()
print("Mon discord :")
print("   - https://discord.com/invite/CxjqJ6Ufk8")
print()
print("**************************************************************************")
print("*  Si le programme ne marche pas, ouvrez le cmd et faites :              *")
print("*  pip install nuitka                                                    *")
print("*  Si le programme ne marche toujours pas, ouvrez le cmd et faites :     *")
print("*  py -m pip install nuitka                                              *")
print("**************************************************************************")
print()
print("Exemple d'utilisation :")
print()
print("****************************************************************************************")
print("*  Entrez l'emplacement complet du fichier (avec l'extension) : D:\Programmes\main.py  *")
print("*  Entrez le Voulez-vous que le cmd sois masqué ? [yes/no] : yes                       *")
print("*  -- Le programme devrai s'éxécuter :) --                                             *")
print("****************************************************************************************\n")

def main():
    # Demander à l'utilisateur d'entrer l'emplacement complet du fichier
    emplacement_complet = input("Entrez l'emplacement complet du fichier (avec l'extension) : ")

    # Extraire le nom du fichier (avec l'extension) et son emplacement
    emplacement, nom = os.path.split(emplacement_complet)

    # Vérifier si le fichier existe
    if not os.path.exists(emplacement_complet):
        print("Erreur: Le fichier spécifié n'existe pas.")
        exit(1)

    # Changer de répertoire vers l'emplacement spécifié
    os.chdir(emplacement)

    # Exécuter nuitka pour compiler le fichier spécifié en un seul fichier exécutable
    choix_cmd = input("Voulez-vous que le cmd sois masqué ? yes/[no] : ").lower()
    if choix_cmd == "yes" or choix_cmd == "y":
        commande = f'"{sys.executable}" -m nuitka --onefile --standalone --windows-disable-console {nom}'
    else:
        commande = f'"{sys.executable}" -m nuitka --onefile --standalone {nom}'

    # On exécute la commande et traite les erreurs ;)
    try:
        subprocess.run(commande, shell=True)
    except Exception as e:
        print(f"Une erreur est survenue :\n{e}")
        print(f'Voici la commande qui a échoué : {commande}')
        retry = input("Voulez-vous modifier la commande ? yes/[no] : ").lower()
        if retry == "yes" or retry == "y":
            commande2 = input("Votre commande : ")
            try:
                subprocess.run(commande2, shell=True)
            except Exception as e:
                print(f"Une erreur est survenue, annulation...\nErreur :\n{e}\n")
        else:
            print("Anulation de la commande...\n")

main()
