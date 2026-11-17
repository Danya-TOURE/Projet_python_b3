from functions import ajouter_equipe, afficher_equipes, recherche_lineaire, saisir_resultat,trier_equipes
from functions import tri_bubble, afficher_statistiques, recherche_dichotomique, generer_matchs, compter_equipes_recursif

def menu_principal(equipes):
    while True:
        print("\nMenu principal :")
        print("1. Ajouter une équipe")
        print("2. Afficher les équipes")
        print("3. Saisir le résultat d'un match")
        print("4. Rechercher une équipe")
        print("5. Afficher le classement")
        print("6. Quitter")

        choix = input("Entrez votre choix (1-6) : ")
        if choix == "1":
            nom = input("Entrez le nom de l'équipe : ")
            if ajouter_equipe(equipes, nom):
                print(f"L'équipe '{nom}' a été ajoutée avec succès.")
            else:
                print(f"Impossible d'ajouter l'équipe '{nom}'. Elle existe déjà ou le nom est invalide.")
        elif choix == "2":
            if not afficher_equipes(equipes):
                print("Aucune équipe n'a été ajoutée.")
        elif choix == "3":
            nom1 = input("Entrez le nom de la première équipe : ")
            nom2 = input("Entrez le nom de la deuxième équipe : ")
            try:
                but_equipe1 = int(input(f"Entrez le nombre de buts marqués par {nom1} : "))
                but_equipe2 = int(input(f"Entrez le nombre de buts marqués par {nom2} : "))
            except ValueError:
                print("Veuillez entrer un nombre entier pour les buts.")
                continue

            success, message = saisir_resultat(equipes, nom1, nom2, but_equipe1, but_equipe2)
            if success:
                print("Résultat saisi avec succès.")
            else:
                print(f"Erreur lors de la saisie du résultat : {message}")
        elif choix == "4":
            nom_recherche = input("Entrez le nom de l'équipe à rechercher : ")
            equipe = recherche_lineaire(equipes, nom_recherche)
            if equipe:
                print(f"Équipe trouvée : {equipe['nom']} - Points: {equipe['points']} | V: {equipe['victoires']} | N: {equipe['nuls']} | D: {equipe['defaites']} | Buts: {equipe['buts_marques']}-{equipe['buts_encaisses']}")
            else:
                print(f"Aucune équipe trouvée avec le nom '{nom_recherche}'.")
        elif choix == "5":
            classement = trier_equipes(equipes)
            print("\n=== CLASSEMENT ===")
            if not classement:
                print("Aucune équipe n'a été ajoutée.")
            for i, e in enumerate(classement, start=1):
                diff = e["buts_marques"] - e["buts_encaisses"]
                print(f"{i}. {e['nom']} | {e['points']} pts | V:{e['victoires']} N:{e['nuls']} "
                    f"D:{e['defaites']} | Buts: {e['buts_marques']}-{e['buts_encaisses']} | Diff: {diff:+d}")
        elif choix == "6":
            print("Au revoir !")
            break

