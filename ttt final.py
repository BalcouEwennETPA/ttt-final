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
		