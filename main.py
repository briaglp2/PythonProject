import os, sys

def menuinteractif():
    liste_menu = {
        "1": "[1] Information sur python",
        "2": "[2] Information sur l'IA",
        "3": "[3] Question sur L'IA",
        "4": "[4] Quitter l'application"
    }
    print(liste_menu["1"] + "\n" + liste_menu["2"] + "\n" + liste_menu["3"] + "\n" + liste_menu["4"])
    choixdelaliste = input("Choisis une option: ")
    if "1" in choixdelaliste:
        informationsurpython()
    elif "2" in choixdelaliste:
        print("Tu a choisis l'option 2")
    elif "3" in choixdelaliste:
        print("Tu a choisis l'option 3")
    elif "4" in choixdelaliste and sys.platform.startswith('win'):
    # Vous êtes sur Windows
        os.system('cls')  # Pour effacer l'écran de la console Windows
    elif "4" in choixdelaliste and sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    # Vous êtes sur Linux ou macOS
        os.system('clear')
    else:
        print("Tu n'a choisis aucune des 4 options")

def informationsurpython():
    liste_menu = {
        "1": "[1] Facilité d'apprentissage : Python est réputé pour sa syntaxe simple et sa lisibilité. Il ressemble presque à du pseudocode, ce qui le rend accessible aux débutants en programmation.",
        "2": "[2] Polyvalence : Python peut être utilisé pour une variété de tâches, notamment le développement web, l'automatisation de tâches, la science des données, l'apprentissage automatique, l'intelligence artificielle, le développement de jeux, etc.",
        "3": "[3] Grande communauté : Python bénéficie d'une vaste communauté d'utilisateurs et de développeurs. Il existe une pléthore de ressources en ligne, de modules, de packages et de frameworks disponibles pour aider les programmeurs Python.",
        "4": "[4] Quitter l'application"
    }
    print(liste_menu["1"] + "\n" + liste_menu["2"] + "\n" + liste_menu["3"] + "\n" + liste_menu["4"])


if __name__ == "__main__":
    menuinteractif()