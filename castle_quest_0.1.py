'''

	

'''

def read_matrice(file):
	'''

		Recois en argument le nom du fichier texte concernant 
		le plan à tracer.
		Elle ouvre ce fichier et renvoie en sortie une matrice.

	'''
	with open(file) as f:
		largeur = f.readline()
		hauteur = f.readlines()

	count = 0
	count2 = 1
	for ligne in largeur:
		count += 1
	for ligne in hauteur:
		count2 += 1

	count = int(count/2)

	return (count, count2)
	


def show_plan(matrice):
	'''

		Appelle la fonction trace_case pour chaque colonne du plan,
		par deux boucles imbriquées. Pour chaque élément ligne de la matrice,
		pour chaque élément colonne de cet élément ligne, tracer une case à 
		l'emplacement correspondant, dans une couleur correspondant à ce que 
		dit la matrice.

	'''
	return

def calcul_step(matrice):
	'''

		Calcule la dimention à donner aux cases pour que le plan
		tienne dans la zone de la fenêtre turtle que vous avez définie :
		diviser la largeur et la hauteur de la zone en question par le nombre
		de cases qu'elle doit accueillir, retenir la plus faible de ces deux valeurs

	'''
	return


def coordonnees(case, step):
	'''

		Calcule les données en pixels turtle du coin inférieur 
		gauche d'une case définie par ses coordonnées (numéro de ligne et colonne).
		Souvenez-vous que les lignes sont numérotées de haut en bas, alors que l'axe
		des coordonnées verticales va de bas en haut. 

	'''
	return

def trace_square(dimention):
	'''

		Trace un carré dont la dimension en pixels turtle est donnée en argument.

	'''
	return

def trace_case(case, color, step):
	'''

		Reçoit en arguments un couple de coordonnées en indice dans la matrice 
		contenant le plan, une couleur, et un pas (taille d'un coté) et qui 
		va appeler la fonction trace_square pour tracer un carré d'une certaine 
		couleur et taille à un certain endroit.


	'''
	# trace_square()
	return






