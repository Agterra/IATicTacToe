import pygame,random,time

def _initMatrice_():
	plateau = [[0,0,0],[0,0,0],[0,0,0]]
	return plateau

def estPlein(plateau):
	for i in plateau:
		for j in i:
			if j == 0:
				return False
	return True
	
def checkVictoire(plateau):
	for i in range(3):
		for j in range(3):
			if i==j:
				if i==1:
					if checkLigne(plateau,i)!=0:
						return checkLigne(plateau,i)
					if checkColonne(plateau,j)!=0:
						return checkColonne(plateau,j)
					if checkDiagonaleGauche(plateau)!=0:
						return checkDiagonaleGauche(plateau)
					if checkDiagonaleDroite(plateau)!=0:
						return checkDiagonaleDroite(plateau)
				else:		
					if checkLigne(plateau,i)!=0:
						return checkLigne(plateau,i)
					if checkColonne(plateau,j)!=0:
						return checkColonne(plateau,j)
					if checkDiagonaleGauche(plateau)!=0:
						return checkDiagonaleGauche(plateau)
			elif i+j==2:
				if i==j:
					if checkLigne(plateau,i)!=0:
						return checkLigne(plateau,i)
					if checkColonne(plateau,j)!=0:
						return checkColonne(plateau,j)
					if checkDiagonaleGauche(plateau)!=0:
						return checkDiagonaleGauche(plateau)
					if checkDiagonaleDroite(plateau)!=0:
						return checkDiagonaleDroite(plateau)
				else:		
					if checkLigne(plateau,i)!=0:
						return checkLigne(plateau,i)
					if checkColonne(plateau,j)!=0:
						return checkColonne(plateau,j)
					if checkDiagonaleDroite(plateau)!=0:
						return checkDiagonaleDroite(plateau)
					
			else :
				if checkLigne(plateau,i)!=0:
						return checkLigne(plateau,i)
				if checkColonne(plateau,j)!=0:
						return checkColonne(plateau,j)
	return 0
						
def checkLigne(plateau,ligne):
	cptJ1=0;cptJ2=0
	for j in range(3):
		if plateau[ligne][j]==-1:
			cptJ1+=1
		elif plateau[ligne][j]==1:
			cptJ2+=1
	if cptJ1==3:
		return -1
	elif cptJ2==3:
		return 1
	else :
		return 0
		         
def checkColonne(plateau,colonne):
	cptJ1=0;cptJ2=0
	for i in range(3):
		if plateau[i][colonne]==-1:
			cptJ1+=1
		elif plateau[i][colonne]==1:
			cptJ2+=1
	if cptJ1==3:
		return -1
	elif cptJ2==3:
		return 1
	else :
		return 0
	
def checkDiagonaleGauche(plateau):
	cptJ1=0;cptJ2=0
	for i in range(3):
		for j in range(3):
			if i==j:
				if plateau[i][j]==-1:
					cptJ1+=1
				elif plateau[i][j]==1:
					cptJ2+=1
	if cptJ1==3:
		return -1
	elif cptJ2==3:
		return 1
	else :
		return 0

def checkDiagonaleDroite(plateau):
	cptJ1=0;cptJ2=0
	for i in range(3):
		for j in range(3):
			if i+j==2:
				if plateau[i][j]==-1:
					cptJ1+=1
				elif plateau[i][j]==1:
					cptJ2+=1
	if cptJ1==3:
		return -1
	elif cptJ2==3:
		return 1
	else :
		return 0		
		          
def jouerTour(tour,plateau,posX,posY):
	signe = 0
	if (tour%2)==0:
		signe = 1
	else :
		signe = -1
	if plateau[posY][posX]== 0:
		plateau[posY][posX]=signe
	else :
		
		return -42

	
def _affichage_(plateau):	
	for i in plateau:
		for j in i:
			if j == -1:
				print ('O'),
			elif j == 1:
				print ('X'),
			else:
				print (' '),
			print ('|'),
		print('')
	
def randBot(plateau):
	copie = plateau
	i = random.randint(0,2)
	j = random.randint(0,2)
	while copie[i][j]!=0:
		i = random.randint(0,2)
		j = random.randint(0,2)
	if i==0 and j == 0:
		return 7
	elif i==0 and j == 1:
		return 8
	elif i==0 and j == 2:
		return 9
	elif i==1 and j == 0:
		return 4
	elif i==1 and j == 1:
		return 5
	elif i==1 and j == 2:
		return 6
	elif i==2 and j == 0:
		return 1
	elif i==2 and j == 1:
		return 2
	elif i==2 and j == 2:
		return 3
	
def iaPeuMaligneJ2(plateau,tour):
	print"L'IA reflechie..."
	copie = _initMatrice_()
	for i in range(3):
		for j in range(3):
			copie[i][j]=plateau[i][j]			
	for i in range(3):
		for j in range(3):
			if copie[i][j]==0:
				
				copie[i][j]=1
				result = checkVictoire(copie)
				if result == 1:
					plateau[i][j]=1
					return 1;
				else:
					copie[i][j]=0
					
	if tour==2:
		if plateau[1][1]==-1:
			plateau[0][0]=1
		elif plateau[0][0]==-1:
			plateau[0][2]=1
		else:
			i = random.randint(0,2)
			j = random.randint(0,2)
			while copie[i][j]!=0:
				i = random.randint(0,2)
				j = random.randint(0,2)
			plateau[i][j]=1
			return 1
	else:
		i = random.randint(0,2)
		j = random.randint(0,2)
		while copie[i][j]!=0:
			i = random.randint(0,2)
			j = random.randint(0,2)
		plateau[i][j]=1
		return 1
					
def iaPeuMaligneJ1(plateau,tour):
	print"L'IA reflechie..."
	copie = _initMatrice_()
	for i in range(3):
		for j in range(3):
			copie[i][j]=plateau[i][j]			
	for i in range(3):
		for j in range(3):
			if copie[i][j]==0:
					
				copie[i][j]=1
				result = checkVictoire(copie)
				if result == 1:
					plateau[i][j]=-1
					return 1;
				else:
					copie[i][j]=0
	if tour==2:
		if plateau[1][1]==1:
			plateau[0][0]=-1
		elif plateau[0][0]==1:
			plateau[0][2]=-1
		else:
			i = random.randint(0,2)
			j = random.randint(0,2)
			while copie[i][j]!=0:
				i = random.randint(0,2)
				j = random.randint(0,2)
			plateau[i][j]=-1
			return 1
	else:
		i = random.randint(0,2)
		j = random.randint(0,2)
		while copie[i][j]!=0:
			i = random.randint(0,2)
			j = random.randint(0,2)
		plateau[i][j]=-1
		return 1
					
def iaIntelligente(plateau,Jx,Jy,Bx,By,tour):
	
	copie = _initMatrice_()
	for i in range(3):
		for j in range(3):
			copie[i][j]=plateau[i][j]
	if Jx>-1 and Jy>-1 and Bx>-1 and By>-1:
		copie[Jy][Jx]=-1
		copie[By][Bx]=1
	else:
		i = random.randint(0,2)
		j = random.randint(0,2)
		a = random.randint(0,2)
		b = random.randint(0,2)
		while copie[i][j]!=0 and copie[a][b]!=0 and i!=a and j!=b:
			i = random.randint(0,2)
			j = random.randint(0,2)
			a = random.randint(0,2)
			b = random.randint(0,2)
		copie[i][j]=-1
		copie[a][b]=1
		
	if estPlein(copie):
		return copie
	if checkVictoire(copie)==1:
		return copie
			
	i = random.randint(0,2)
	j = random.randint(0,2)
	a = random.randint(0,2)
	b = random.randint(0,2)
	while copie[i][j]!=0 and copie[a][b]!=0 and i!=a and j!=b:
		i = random.randint(0,2)
		j = random.randint(0,2)
		a = random.randint(0,2)
		b = random.randint(0,2)
	
	return iaIntelligente(copie,j,i,b,a,tour+1)
	
def simulation(plateau,tour):
				
	copie = _initMatrice_()
	for i in range(3):
		for j in range(3):
			copie[i][j]=plateau[i][j]
	_affichage_(copie)
	print""
	time.sleep(1)			
	if estPlein(copie):
		return copie
	if checkVictoire(copie)==-1:
		print"Victoire Joueur 1"
		return copie
	elif checkVictoire(copie)==1:
		print"Victoire Joueur 2"
		return copie
		
	if(tour%2==0):
		iaPeuMaligneJ2(copie,tour)
	else:
		iaPeuMaligneJ1(copie,tour)
	
	return simulation(copie,tour+1)
				
def main():
	print ("Comment jouer:\n")
	print ("7|8|9\n4|5|6\n1|2|3\n")
	plateau = _initMatrice_()
	tour = 1
	_affichage_(plateau)
	
	while checkVictoire(plateau)==0 and estPlein(plateau)==False:
		
		if (tour%2)==0:
			print("Tour joueur 2:");case =-1; iaPeuMaligne(plateau,tour);time.sleep(1)
			#print("Tour joueur 2:");case = randBot(plateau);time.sleep(1)
			#case = int(input("Tour joueur 2:"))
		else:
			case = int(input("Tour joueur 1:"))
			
		if case == 1:
			check = jouerTour(tour,plateau,0,2)
		elif case == 2:
			check = jouerTour(tour,plateau,1,2)
		elif case == 3:
			check = jouerTour(tour,plateau,2,2)
		elif case == 4:
			check = jouerTour(tour,plateau,0,1)
		elif case == 5:
			check = jouerTour(tour,plateau,1,1)
		elif case == 6:
			check = jouerTour(tour,plateau,2,1)
		elif case == 7:
			check = jouerTour(tour,plateau,0,0)
		elif case == 8:
			check = jouerTour(tour,plateau,1,0)
		elif case == 9:
			check = jouerTour(tour,plateau,2,0)
		elif case == -1:
			print "L'IA dit: A TOI HUMAIN."
		if check == -42:
			print ("Vous ne pouvez pas jouer ici!")
		else:
			_affichage_(plateau)
			tour+=1
			
	
	if checkVictoire(plateau)==-1:
		print ("Victoire Joueur 1!")
	elif checkVictoire(plateau)==1:
		print ("Victoire Joueur 2!")
	else :
		print ("Egalite!")
	
		
						
plateau=_initMatrice_()
#_affichage_(iaIntelligente(plateau,-1,-1,-1,-1,0))
simulation(plateau,0)
#A faire: ia maligne
