import random

cadrillage = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


#le joueur a t-il gagné ?
def resultat(symbolejoueur):
    indexrow = [0, 3, 6]
    indexcolumn = [0, 1, 2]
    for el in indexrow:
        if cadrillage[el] == symbolejoueur:
            if cadrillage[el + 1] == symbolejoueur:
                if cadrillage[el + 2] == symbolejoueur:
                    return 1
    for el in indexcolumn:
        if cadrillage[el] == symbolejoueur:
            if cadrillage[el + 3] == symbolejoueur:
                if cadrillage[el + 6] == symbolejoueur:
                    return 1
    if cadrillage[0] == symbolejoueur:
        if cadrillage[4] == symbolejoueur:
            if cadrillage[8] == symbolejoueur:
                return 1
    if cadrillage[2] == symbolejoueur:
        if cadrillage[4] == symbolejoueur:
            if cadrillage[6] == symbolejoueur:
                return 1
    return 0

def affichercadrillage():
    print("\n " + cadrillage[0] + " | " + cadrillage[1] + " | " + cadrillage[2] + " ")
    print("---+---+---")
    print(" " + cadrillage[3] + " | " + cadrillage[4] + " | " + cadrillage[5] + " ")
    print("---+---+---")
    print(" " + cadrillage[6] + " | " + cadrillage[7] + " | " + cadrillage[8] + " ")

def restecase ():
    caserestante = 0
    for el in cadrillage:
        if el == ' ':
            caserestante = 1
    if caserestante == 0:
        affichercadrillage()
        print('***** Il y a égalité *****')
    return caserestante

print('\nTon symbole est : X\n')
while True:
    statutjeu = -1
    while statutjeu != 0:
        caserestante = restecase()
        if caserestante == 0:
            break
        affichercadrillage()

        print('Ou jouez-vous ? (Entrez une position de 1 à 9')
        position = input()
        position = int(position) - 1

        if cadrillage[position] == ' ':
            cadrillage[position] = 'X'
            statutjeu = 0
        else:
            statutjeu = 1
            print('Position déjà joué !')

    response = resultat('X')
    if response == 1:
        affichercadrillage()
        print('***** Tu as gagné !!! *****')
        break

    caserestante = restecase()
    if caserestante == 0:
        break

    while True:
        positionpc = random.randint(0,8)
        if cadrillage[positionpc] == ' ':
            cadrillage[positionpc] = '0'
            print('Le pc a joué en position',positionpc+1)
            break

    responsepc = resultat('0')
    if responsepc == 1:
        affichercadrillage()
        print('***** Tu as perdu !!! *****')
        break