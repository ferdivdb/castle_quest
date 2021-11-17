'''
Propre en bas et non - achevé
BROUILLON BROUILLON BROUILLON BROUILLON BROUILLON
BROUILLON BROUILLON BROUILLON BROUILLON BROUILLON
BROUILLON BROUILLON BROUILLON BROUILLON BROUILLON
BROUILLON BROUILLON BROUILLON BROUILLON BROUILLON
BROUILLON BROUILLON BROUILLON BROUILLON BROUILLON

	import turtle

#création matrix
def read_matrice(file):
	
	f = open(file, 'r')
	matrice = [[int(n) for n in line.split(' ')] for line in f ]
	return matrice

matrix = read_matrice('plan_chateau.txt')
matrix.reverse()

x = len(matrix[0])
y = len(matrix)
sc1 = x*x
sc2 = y*x
surf_p = sc1*sc2
case = x*y
faible = (surf_p/case)/(y)
TURTLE_SIZE = (sc2/y)


# Initialization objet Turtle  Screen Vitesse
pen = turtle.Turtle()
sc = turtle.Screen()
sc.setup(sc1, sc2)
pen.speed(0)
pen.penup()
# Initialization de la position de départ
pen.goto(TURTLE_SIZE/2 - sc.window_width()/2, -(sc.window_height()/2 - TURTLE_SIZE/2)+faible)
pos = pen.pos()
pos1 = pos[0]
pos2 = pos[1]

pen.pendown()

# Dessin carre
def square(dim, color):
	pen.color('white', color)
	for i in range(4):
		pen.forward(dim)
		pen.left(90)


# Parcours Matrice
for i in range(len(matrix)):
	pos2 += faible
	for j in range(len(matrix[0])):
		if matrix[i][j] == 3:
			pen.begin_fill()
			square(faible, 'orange')
			pen.penup()
			pen.forward(faible)
			pen.pendown()
			pen.end_fill()
		elif matrix[i][j] == 1:
			pen.begin_fill()
			square(faible, 'azure4')
			pen.penup()
			pen.forward(faible)
			pen.pendown()
			pen.end_fill()
		elif matrix[i][j] == 4:
			pen.begin_fill()
			square(faible, 'green')
			pen.penup()
			pen.forward(faible)
			pen.pendown()
			pen.end_fill()
		else:
			square(faible, 'white')
			pen.penup()
			pen.forward(faible)
			pen.pendown()
	pen.penup()
	pen.goto(pos1, pos2)
	pen.pendown()	
	

turtle.done()

'''
import turtle

def read_matrice(file):
	'''

		Recois en argument le nom du fichier texte concernant 
		le plan à tracer.
		Elle ouvre ce fichier et renvoie en sortie une matrice.

	'''
	f = open(file, 'r')
	matrice = [[int(n) for n in line.split(' ')] for line in f ]
	matrice.reverse()
	return matrice



def calcul_step(matrice):
	'''

		Calcule la dimention à donner aux cases pour que le plan
		tienne dans la zone de la fenêtre turtle que vous avez définie :
		diviser la largeur et la hauteur de la zone en question par le nombre
		de cases qu'elle doit accueillir, retenir la plus faible de ces deux valeurs

	'''
	x = len(matrice[0])
	y = len(matrice)
	l = x*10
	h = y*10
	sc.setup(l, h)
	surf_p = l*h
	surf_m = x*y
	step = (surf_p/surf_m)/(x/10)
	return step

def coordonnees(case, step):
	'''

		Calcule les données en pixels turtle du coin inférieur 
		gauche d'une case définie par ses coordonnées (numéro de ligne et colonne).
		Souvenez-vous que les lignes sont numérotées de haut en bas, alors que l'axe
		des coordonnées verticales va de bas en haut. 

	'''
	TURTLE_SIZE = len(read_matrice('plan_chateau.txt'))
	pen.goto(TURTLE_SIZE/2 - sc.window_width()/2, -(sc.window_height()/2 - TURTLE_SIZE/2)+step)
	

def trace_square(dimention):
	'''

		Trace un carré dont la dimension en pixels turtle est donnée en argument.

	'''
	for i in range(4):
		pen.pendown()
		pen.forward(dimention)
		pen.left(90)
		pen.penup()


def trace_case(case, color, step):
	'''

		Reçoit en arguments un couple de coordonnées en indice dans la matrice 
		contenant le plan, une couleur, et un pas (taille d'un coté) et qui 
		va appeler la fonction trace_square pour tracer un carré d'une certaine 
		couleur et taille à un certain endroit.


	'''
	pen.begin_fill()
	square(case, color)
	pen.penup()
	pen.forward(step)
	pen.pendown()
	pen.end_fill()
	return




def show_plan(matrice):
	'''

		Appelle la fonction trace_case pour chaque colonne du plan,
		par deux boucles imbriquées. Pour chaque élément ligne de la matrice,
		pour chaque élément colonne de cet élément ligne, tracer une case à 
		l'emplacement correspondant, dans une couleur correspondant à ce que 
		dit la matrice.

	'''
	


	return




