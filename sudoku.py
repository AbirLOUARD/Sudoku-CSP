import itertools

lignes = "123456789"
colonnes = "ABCDEFGHI"

class Sudoku:
    def __init__(self, grille):
        game = list(grille)
        self.cases = list()
        self.cases = self.generer_coordonnees()
        self.valeurs_possibles = dict()
        self.valeurs_possibles = self.generer_valeurs_possibles(grille)
        contraintes = self.generer_contraintes()
        self.contraintes_binaires = list()
        self.contraintes_binaires = self.generer_contraintes_binaires(contraintes)
        self.cases_potentielles = dict()
        self.cases_potentielles = self.generer_cases_potentielles()
        self.elaguage = dict()
        self.elaguage = {v: list() if grille[i] == '0' else [int(grille[i])] for i, v in enumerate(self.cases)}


    def generer_coordonnees(self):
        ensemble_coordonnees = []
        for colonne in colonnes:
            for ligne in lignes:
                nouvelles_coordonnees = colonne + ligne
                ensemble_coordonnees.append(nouvelles_coordonnees)
        return ensemble_coordonnees


    def generer_valeurs_possibles(self, grille):
        liste_grille = list(grille)
        valeurs_possibles = dict()
        for i, coordonnees in enumerate(self.cases):
            if liste_grille[i] == "0":
                valeurs_possibles[coordonnees] = list(range(1,10))
            else:
                valeurs_possibles[coordonnees] = [int(liste_grille[i])]
        return valeurs_possibles


    def generer_contraintes(self):
        contraintes_ligne = []
        contraintes_colonne = []
        contraintes_carre = []
        for ligne in lignes:
            contraintes_ligne.append([colonne + ligne for colonne in colonnes])
        for colonne in colonnes:
            contraintes_colonne.append([colonne + ligne for ligne in lignes])
        coordonnees_carre_lignes = (colonnes[i:i+3] for i in range(0, len(lignes), 3))
        coordonnees_carre_lignes = list(coordonnees_carre_lignes)
        coordonnees_carre_colonnes = (lignes[i:i+3] for i in range(0, len(colonnes), 3))
        coordonnees_carre_colonnes = list(coordonnees_carre_colonnes)
        for ligne in coordonnees_carre_lignes:
            for colonne in coordonnees_carre_colonnes:
                contraintes_carre_actuelles = []
                for x in ligne:
                    for y in colonne:
                        contraintes_carre_actuelles.append(x + y)
                contraintes_carre.append(contraintes_carre_actuelles)
        return contraintes_ligne + contraintes_colonne + contraintes_carre


    def generer_contraintes_binaires(self, contraintes):
        liste_contraintes_binaires = list()
        for c in contraintes:
            contraintes_binaires = list()
            for tuple_contraintes in itertools.permutations(c, 2):
                contraintes_binaires.append(tuple_contraintes)
            for contrainte in contraintes_binaires:
                liste_contraintes = list(contrainte)
                if (liste_contraintes not in liste_contraintes_binaires):
                    liste_contraintes_binaires.append([contrainte[0], contrainte[1]])
        return liste_contraintes_binaires


    def generer_cases_potentielles(self):
        cases_potentielles = dict()
        for case in self.cases:
            cases_potentielles[case] = list()
            for contrainte in self.contraintes_binaires:
                if case == contrainte[0]:
                    cases_potentielles[case].append(contrainte[1])
        return cases_potentielles


    def estFini(self):
        for coordonnees, valeurs_possibles in self.valeurs_possibles.items():
            if len(valeurs_possibles) > 1:
                return False
        return True


    def __str__(self):
        sortie = ""
        compteur = 1
        for case in self.cases:
            valeur = str(self.valeurs_possibles[case])
            if type(self.valeurs_possibles[case]) == list:
                valeur = str(self.valeurs_possibles[case][0])
            sortie += "[" + valeur + "]"
            if compteur >= 9:
                compteur = 0
                sortie += "\n"
            compteur +=1
        return sortie
