grille =['*','*','*','*','*','*','*','*','*',]

print("0 1 2")
print("3 4 5")
print("6 7 9")

joueur = "X"
tour = 1
victoire_user = 0

def ajouteSymbole (joueur):
	caseOK= 0
	while(caseOk != 1):
		 numeroCase = int(input("Numero de case ?"))
		 if(grille[numeroCase]=='*'):
		 	caseOk = 1
    grille[numeroCase] = joueur

def afficher_grille():
	for i in range(3):
		print(grille[i*3],grille[i*3+1],grille[i*3+2])
		

def joueur_O_X(joueur_f):
	if(joueur_f == "X"):
		joueur = "O"
	else:
		joueur = "X"
	return joueur

def win(victoire):
	for i in range(3):

		if (grille[i*3] == grille[i*3+1] == grille[i*3+2] != "*"):
			victoire = 1
		if (grille[i] == grille[i+3] == grille[i+6] != "*"):
			victoire = 1

	for i in range(2):
		if(grille[i+i] == grille[i+4-i] == grille[i+8-(i*3)] != "*"):
			victoire = 1
	return victoire