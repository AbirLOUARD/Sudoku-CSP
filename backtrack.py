from heuristiques import select_unassigned_variable, order_domain_values
from fonctions import est_consistant, assigne, desassigne

def recursive_backtrack(assignement, sudoku):
    if len(assignement) == len(sudoku.cases):
        return assignement
    case = select_unassigned_variable(assignement, sudoku)
    for valeur in order_domain_values(sudoku, case):
        if est_consistant(sudoku, assignement, case, valeur):
            assigne(sudoku, case, valeur, assignement)
            resultat = recursive_backtrack(assignement, sudoku)
            if resultat:
                return resultat
            desassigne(sudoku, case, assignement)
    return False
