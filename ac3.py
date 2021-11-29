from fonctions import sont_different

def AC3(csp, queue=None):
    if queue == None:
        queue = list(csp.contraintes_binaires)
    while queue:
        (posX, posY) = queue.pop(0)
        if enlever_valeur_inconsistantes(csp, posX, posY):
            if len(csp.valeurs_possibles[posX]) == 0:
                return False
            for v in csp.cases_potentielles[posX]:
                if v != posX:
                    queue.append((v, posX))
    return True


def enlever_valeur_inconsistantes(csp, caseA, caseB):
    enleve = False
    for valeur in csp.valeurs_possibles[caseA]:
        if not any([sont_different(valeur, valeur_possible) for valeur_possible in csp.valeurs_possibles[caseB]]):
            csp.valeurs_possibles[caseA].remove(valeur)
            enleve = True
    return enleve
