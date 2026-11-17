"""Fonction pour ajouter une équipe à la liste des équipes"""
def ajouter_equipe(equipes, nom):
    nom = nom.strip() 
   # Vérifier si le nom de l'équipe est vide ou non 
    if nom == "":
       return False
    # Vérifier si l'équipe existe déjà dans la liste
    for equipe in equipes:
        if equipe["nom"].lower() == nom.lower():
            return False
    #Créer un dictionnaire pour la nouvelle équipe avec les statistiques initiales
    nouvelle_equipe = {"nom": nom,
             "victoires": 0,
             "nuls": 0,
             "defaites": 0,
             "buts_marques": 0,
             "buts_encaisses": 0,
             "points": 0}
    equipes.append(nouvelle_equipe)
    return True


"""Fonction pour afficher les équipes"""
def afficher_equipes(equipes):
    # Vérifier si la liste des équipes est vide
    if not equipes:
        return False
    else:
        for i, equipe in enumerate(equipes, start=1):# Afficher les informations de chaque équipe avec son index
            print(f"{i}. {equipe['nom']} - Points: {equipe['points']} | V: {equipe['victoires']} | N: {equipe['nuls']} | D: {equipe['defaites']} | Buts: {equipe['buts_marques']}-{equipe['buts_encaisses']}")
        return True


"""Fonction pour la recherche linéaire d'une équipe par son nom"""
def recherche_lineaire(equipes, nom_recherche):
    nom = nom_recherche.strip().lower()
    for equipe in equipes:
        if equipe["nom"].lower() == nom:
            return equipe
    return None

"""Fonction pour saisir le résultat d'un match"""
def saisir_resultat(equipes, nom1, nom2, but_equipe1, but_equipe2):
    #interdire les scores négatifs
    if but_equipe1 < 0 or but_equipe2 < 0:
        return False, "les scores ne peuvent pas être négatifs"
    
    #empêcher la saisie de deux équipes identiques
    if nom1.strip().lower() == nom2.strip().lower():
        return False, "les deux équipes doivent être différentes"
    #rechercher les équipes dans la liste des équipes
    equipe1 = recherche_lineaire(equipes, nom1)
    equipe2 = recherche_lineaire(equipes, nom2)

    # Vérifier si les deux équipes existent dans la liste des équipes
    if equipe1 is None or equipe2 is None:
        return False, "l'une des équipes n'existe pas"
     # Buts marqués / encaissés
    equipe1["buts_marques"] += but_equipe1
    equipe1["buts_encaisses"] += but_equipe2
    equipe2["buts_marques"] += but_equipe2
    equipe2["buts_encaisses"] += but_equipe1
    # Mettre à jour les statistiques des équipes en fonction du résultat du match
    if but_equipe1 > but_equipe2:
        equipe1["victoires"] += 1
        equipe2["defaites"] += 1
        equipe1["points"] += 3
    elif but_equipe1 < but_equipe2:
        equipe2["victoires"] += 1
        equipe1["defaites"] += 1
        equipe2["points"] += 3
    else:
        equipe1["nuls"] += 1
        equipe2["nuls"] += 1
        equipe1["points"] += 1
        equipe2["points"] += 1
    return True, "Résultat du match enregistré avec succès"


""" Fonction pour trier les équipes par points(ordre décroissant), puis par différence de buts en cas d'égalité"""
def trier_equipes(equipes):
    equipes = sorted(equipes, key=lambda e: (e["points"], e["buts_marques"] - e["buts_encaisses"]), reverse=True)
    return equipes


"""Fonction d'algorithme de tri manuel"""
def tri_bubble(equipes):
    n = len(equipes)
    for i in range (n):
        for j in range(0, n-i-1):
            if (equipes[j]["points"] < equipes[j+1]["points"]):
                equipes[j], equipes[j+1] = equipes[j+1], equipes[j]
    return equipes

def afficher_statistiques(equipes):
    """Affiche les 5 statistiques demandées."""
    if not equipes:
        print("Aucune équipe.")
        return
    meilleur_points = max(equipes, key=lambda e: e["points"])
    meilleure_attaque = max(equipes, key=lambda e: e["buts_marques"])
    meilleure_defense = min(equipes, key=lambda e: e["buts_encaisses"])
    moyenne_buts = sum(e["buts_marques"] for e in equipes) / len(equipes)
    total_matchs = sum(e["victoires"] + e["nuls"] + e["defaites"] for e in equipes) // 2

    print(f"Plus de points : {meilleur_points['nom']} ({meilleur_points['points']} pts)")
    print(f"Plus de buts marqués : {meilleure_attaque['nom']} ({meilleure_attaque['buts_marques']})")
    print(f"Meilleure défense : {meilleure_defense['nom']} ({meilleure_defense['buts_encaisses']} encaissés)")
    print(f"Moyenne de buts par équipe : {moyenne_buts:.2f}")
    print(f"Matchs joués : {total_matchs}")

"""Fonction de recherche dichotomique"""
def recherche_dichotomique(equipes_triees, nom_recherche):
    nom_recherche = nom_recherche.strip().lower()
    debut = 0
    fin = len(equipes_triees) - 1

    while debut <= fin:
        milieu = (debut + fin) // 2
        nom_milieu = equipes_triees[milieu]["nom"].lower()

        if nom_milieu == nom_recherche:
            return equipes_triees[milieu]
        elif nom_milieu < nom_recherche:
            debut = milieu + 1
        else:
            fin = milieu - 1

    return None

"""Fonction pour générer automatiquement les matchs"""
def generer_matchs(equipes):
    if len(equipes) < 2:
        print("Il n'y a pas assez d'équipes pour générer des matchs.")
        return

    matchs = []
    for i in range(len(equipes)):
        for j in range(i + 1, len(equipes)):
            matchs.append((equipes[i]["nom"], equipes[j]["nom"]))

    print("\nMatchs générés :")
    for match in matchs:
        print(f"{match[0]} vs {match[1]}")
    return matchs


"""Fonction pour  compter récursivement le nombre d’équipes ayant plus de 10 points"""
def compter_equipes_recursif(equipes, seuil_points=10, index=0):
    if index >= len(equipes):
        return 0
    if equipes[index]["points"] > seuil_points:
        return 1 + compter_equipes_recursif(equipes, seuil_points, index + 1)
    else:
        return compter_equipes_recursif(equipes, seuil_points, index + 1)
