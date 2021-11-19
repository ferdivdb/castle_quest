'''
Propre en bas et non - achevé
BROUILLON BROUILLON BROUILLON BROUILLON BROUILLON
BROUILLON BROUILLON BROUILLON BROUILLON BROUILLON
BROUILLON BROUILLON BROUILLON BROUILLON BROUILLON
BROUILLON BROUILLON BROUILLON BROUILLON BROUILLON
BROUILLON BROUILLON BROUILLON BROUILLON BROUILLON

import turtle

### couleurs
def color(matrice):
	if matrice[i][j] == 3: color = 'orange'
	elif matrice[i][j] == 1: color = 'azure4'
	elif matrice[i][j] == 4: color = 'green'
	else: color = 'white'
	return color

###lire matrice
def read_matrice(file):
	f = open(file, 'r')
	matrice = [[int(n) for n in line.split(' ')] for line in f]
	return matrice

### Dessin carre
def tracer_carre(dimention):
	for i in range(4):
		pen.forward(dimention)
		pen.left(90)


### Calcul step
def calcul_step(matrice):
	#matrice = read_matrice('plan_chateau.txt')
	matrice.reverse()
	step = len(matrice[0]) ** 2 / len(matrice)
	return step


#def tracer_case(case, color, step):


#def coordonnees(case, step):

#return case(case1,case2)

#def show_plan(matrice):

### Show plan
matrice = read_matrice('plan_chateau.txt')
step = calcul_step(matrice)
# Initialization Ecran
sc = turtle.Screen()
sc.setup((len(matrice[0]) * len(matrice)), (len(matrice[0]) * len(matrice)))
sc.tracer(0, 0)
# Initialization turtle (vitesse, non visible et levé)
pen = turtle.Turtle(visible = False)
pen.speed(0)
pen.penup()
# envoyer turtle a la position initiale (en bas a gauche )
pen.goto(len(matrice[0]) - sc.window_width() / 2, - (sc.window_height() / 2 - len(matrice[0]) / 2) + step)


# case = position initiale
case = pen.pos()
case1 = case[0]
case2 = case[1]

for i in range(len(matrice)):         # coordonnées
	case2 += step # pas
	for j in range(len(matrice[0])):

### TRACE CASE case, color, step
		pen.pendown()
		pen.begin_fill()
		pen.color('white', color(matrice)) 
		tracer_carre(step)
		pen.penup()
		pen.forward(step)
		pen.pendown()
		pen.end_fill()
###
	pen.penup()
	pen.goto(case1, case2) # coordonnées
	pen.pendown()


sc.mainloop()
sc.update()
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
	l = x*x
	h = y*x
	surface_pixel = l*h
	case = x*y
	step = (surface_pixel/case)/x
	return case, step

def coordonnees(case, step):
	'''

		Calcule les données en pixels turtle du coin inférieur 
		gauche d'une case définie par ses coordonnées (numéro de ligne et colonne).
		Souvenez-vous que les lignes sont numérotées de haut en bas, alors que l'axe
		des coordonnées verticales va de bas en haut. 

	'''
	matrice = read_matrice('plan_chateau.txt')
	pen = turtle.Turtle()
	sc = turtle.Screen()
	sc.setup(len(matrice[0])*len(matrice[0]), len(matrice)*len(matrice[0]))
	TURTLE_SIZE = len(matrice[0])
	pen.goto(TURTLE_SIZE/2 - sc.window_width()/2, -(sc.window_height()/2 - TURTLE_SIZE/2)+step[1])
	case = pen.pos()
	return case
	

def trace_carre(dimention):
	'''

		Trace un carré dont la dimension en pixels turtle est donnée en argument.

	'''
	pen.color="white"
	for i in range(4):
		pen.pendown()
		pen.forward(dimention)
		pen.left(90)
		pen.penup()


def tracer_case(case, color, step):
	'''

		Reçoit en arguments un couple de coordonnées en indice dans la matrice 
		contenant le plan, une couleur, et un pas (taille d'un coté) et qui 
		va appeler la fonction trace_square pour tracer un carré d'une certaine 
		couleur et taille à un certain endroit.


	'''
	pen.begin_fill()
	trace_square(case)
	pen.penup()
	pen.forward(step)
	pen.pendown()
	pen.end_fill()
	




def show_plan(matrice):
	'''

		Appelle la fonction trace_case pour chaque colonne du plan,
		par deux boucles imbriquées. Pour chaque élément ligne de la matrice,
		pour chaque élément colonne de cet élément ligne, tracer une case à 
		l'emplacement correspondant, dans une couleur correspondant à ce que 
		dit la matrice.

	'''
	step = calcul_step(matrice)
	pos = coordonnees(calcul_step(matrice), step)
	pos1 = pos[0]
	pos2 = pos[1]
	color = 'white'
	for i in range(len(matrice)):
		pos2 += step[1]
		for j in range(len(matrice[0])):
			if matrice[i][j] == 3:
				color = 'orange'
			elif matrice[i][j] == 1:
				color = 'azure4'
			elif matrice[i][j] == 4:
				color = 'green'
			else:
				color = 'white'
			trace_case(coordonnees(step[0], step[1]), color, step[1])
		pen.penup()
		pen.goto(pos1, pos2)
		pen.pendown()	
	turtle.done()


show_plan(read_matrice('plan_chateau.txt'))

	
	


	




