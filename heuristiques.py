from fonctions import nombre_conflits

#MRV
def select_unassigned_variable(assignement, sudoku):
    non_assigne = []
    for case in sudoku.cases:
        if case not in assignement:
            non_assigne.append(case)
    choix = lambda case: len(sudoku.valeurs_possibles[case])
    return min(non_assigne, key=choix)


#LCV
def order_domain_values(sudoku, case):
    if len(sudoku.valeurs_possibles[case]) == 1:
        return sudoku.valeurs_possibles[case]
    choix = lambda valeur: nombre_conflits(sudoku, case, valeur)
    return sorted(sudoku.valeurs_possibles[case], key=choix)
