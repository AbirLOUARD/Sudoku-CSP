def sont_different(caseA, caseB):
    v = caseA != caseB
    return v


def nombre_conflits(sudoku, case, valeur):
    compteur = 0
    for case_potentielle in sudoku.cases_potentielles[case]:
        if len(sudoku.valeurs_possibles[case_potentielle]) > 1 and valeur in sudoku.valeurs_possibles[case_potentielle]:
            compteur += 1
    return compteur


def est_consistant(sudoku, assignement, case, valeur):
    consistance = True
    for case_actuelle, valeur_actuelle in assignement.items():
        if valeur_actuelle == valeur and case_actuelle in sudoku.cases_potentielles[case]:
            consistance = False
    return consistance


def assigne(sudoku, case, valeur, assignement):
    assignement[case] = valeur
    if sudoku.valeurs_possibles:
        forward_check(sudoku, case, valeur, assignement)


def desassigne(sudoku, case, assignement):
    if case in assignement:
        for (coordonnees, valeur) in sudoku.elaguage[case]:
            sudoku.valeurs_possibles[coordonnees].append(valeur)
        sudoku.elaguage[case] = []
        del assignement[case]


def forward_check(sudoku, case, valeur, assignement):
    for case_potentielle in sudoku.cases_potentielles[case]:
        if case_potentielle not in assignement:
            if valeur in sudoku.valeurs_possibles[case_potentielle]:
                sudoku.valeurs_possibles[case_potentielle].remove(value)
                sudoku.elaguage[case].append((case_potentielle, valeur))


def dessiner_grille(grille):
    sortie = ""
    compteur = 1
    for case in grille:
        valeur = case
        sortie += "[" + valeur + "]"
        if compteur >= 9:
            compteur = 0
            sortie += "\n"
        compteur += 1
    return sortie
