# pip install nuitka

import os
import subprocess

# Vous pourrez enlever ces print() ;)
print()
print("Programme fait par NatCode (@NatCode171 sur youtube)")
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
print("**************************************************************************")
print("*  Entrez l'emplacement du fichier : D:\Programmes\Virus_Firefox         *")
print("*  Entrez le nom du fichier (avec l'extension) : main.py                 *")
print("*  Le programme devrai s'éxécuter :)                                     *")
print("**************************************************************************")
print()

# Demander à l'utilisateur d'entrer l'emplacement du fichier
emplacement = input(" Entrez l'emplacement du fichier : ")

# Demander à l'utilisateur d'entrer le nom du fichier avec l'extension
nom = input(" Entrez le nom du fichier (avec l'extension) : ")

# Vérifier si le fichier existe
chemin_complet = os.path.join(emplacement, nom)
if not os.path.exists(chemin_complet):
    print("Erreur: Le fichier spécifié n'existe pas.")
    exit(1)

# Changer de répertoire vers l'emplacement spécifié
os.chdir(emplacement)

# Exécuter nuitka pour compiler le fichier spécifié en un seul fichier exécutable
subprocess.run(f'py -m nuitka --onefile --standalone {nom}', shell=True)
