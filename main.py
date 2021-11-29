from fonctions import dessiner_grille
from sudoku import Sudoku
from backtrack import recursive_backtrack
from ac3 import AC3

def resoudre(grille):
    print(dessiner_grille(grille))
    print("\n Resolution par AC3 \n")
    sudoku = Sudoku(grille)
    solution_AC3 = AC3(sudoku)

    if not solution_AC3:
        print("\n Aucune solution possible \n")
    else:
        if (sudoku.estFini()):
            print("\n La solution par AC3 est : \n")
            print(sudoku)
        else:
            print("\n Recherche par AC3 fini \n Debut du Backtracking \n")

            assignement = {}

            for case in sudoku.cases:
                if (len(sudoku.valeurs_possibles[case]) == 1):
                    assignement[case] = sudoku.valeurs_possibles[case][0]

            assignement = recursive_backtrack(assignement, sudoku)

            for case in sudoku.valeurs_possibles:
                sudoku.valeurs_possibles[case] = assignement[case] if len(case) > 1 else sudoku.valeurs_possibles[case]

            if assignement:
                print("\ La solution par Backtracking est : \n")
                print(sudoku)
            else:
                print("\n Aucune solution possible \n")


if __name__ == "__main__":
    numeros_grille = ""
    mylines = []
    with open ('Sudoku.txt', 'rt') as myfile:
        for lines in myfile:
            mylines.append(lines.rstrip('\n').split(" "))
    for i in range(9):
        for j in range(9):
            numeros_grille += mylines[i][j]

    resoudre(numeros_grille)
