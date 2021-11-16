# Info-F-101 : Projet d’Informatique castle_quest
[![N|Solid](https://fundit.fr/sites/default/files/actors/1456-universite-libre-bruxelles-ulb.jpg)](https://nodesource.com/products/nsolid)

## Présentation générale:
### Le projet en trois phrases
>L’objectif du projet est de réaliser une implémentation en Python 3 du jeu Breakthrough. C’est un jeu à deux joueurs sur un échiquier où chaque joueur contrôle deux rangées de pions, qui se déplacent toujours en avant (tout droit ou en diagonale) et qui prennent en diagonale. Le but est d’être le premier joueur à amener un pion à l’autre bout de l’échiquier.
### Les étapes de développement
Nous sommes conscients que ce projet, si vous voulez le faire dans sa totalité, est ambitieux surtout pour des programmeurs débutants.

Nous vous proposons donc, pour mener à bien votre projet, de le phaser dans sa réalisation ; de créer dans un premier temps (niveau 1) un embryon de projet, qui va grossir petit à petit (niveaux 2, 3) pour finalement englober la totalité de ce qui vous est demandé.

7.2.1. Niveau 1 : construction et affichage du plan du château
Le niveau 1 parle de lecture du plan à partir du fichier chateau.txt, de la construction de la matrice correspondante pour stocker ce plan, et de son affichage grâce au module turtle.

Pour cela différentes fonctions doivent être programmées.

FONCTION DE LECTURE DU FICHIER CONTENANT LE PLAN
Vous devez écrire une première fonction lire_matrice(fichier), qui recevra en argument le nom d’un fichier texte contenant le plan à tracer. Elle ouvrira ce fichier et renverra en sortie une matrice, c’est-à-dire une liste de listes, soit une liste dont chaque élément sera lui-même une liste représentant une ligne horizontale de cases du plan.

Prenons l’exemple de ce plan comprenant 4 lignes et 6 colonnes avec les cases vides blanches, des murs gris, un objet orange et une porte verte :

plan d'un chateau très simple
Plan d’un chateau très simple

Il est représenté par le fichier suivant, composé d’entiers séparés par des espaces et de retours à la ligne :

1 0 1 1 1 1
1 0 0 0 0 1
1 0 4 0 0 1
1 1 1 3 1 1
La fonction de lecture du fichier renverra la liste de listes suivante :

[[1, 0, 1, 1, 1, 1], [1, 0, 0, 0, 0, 1], [1, 0, 4, 0, 0, 1], [1, 1, 1, 3, 1, 1]]
FONCTIONS D’AFFICHAGE DU PLAN
Pour tracer le plan du château à partir de la matrice obtenue, vous écrirez une fonction afficher_plan(matrice) utilisant le module turtle ; cette fonction recevra en entrée la matrice telle que décrite ci-dessus.

Pour réaliser cette fonction, nous vous conseillons de suivre les étapes suivantes :

Commencer par une fonction calculer_pas(matrice) qui calcule la dimension à donner aux cases pour que le plan tienne dans la zone de la fenêtre turtle que vous avez définie : diviser la largeur et la hauteur de la zone en question par le nombre de cases qu’elle doit accueillir, retenir la plus faible de ces deux valeurs.

Par exemple, pour une zone turtle d’affichage pour le plan de 290 (-240 à 50) de large et 440 (-240 à 200) de haut, si le plan fait 20 cases en largeur et 44 cases en hauteur, les carrés auront une taille de 10 pour ne pas sortir de la zone (ici le souci, si la taille est supérieure à 10, sera la hauteur du plan).

Définir une fonction coordonnees(case, pas) qui calcule les coordonnées en pixels turtle du coin inférieur gauche d’une case définie par ses coordonnées (numéros de ligne et de colonne). Souvenez-vous que les lignes sont numérotées de haut en bas, alors que l’axe des coordonnées verticales va de bas en haut. Par exemple : avec un château de 44 lignes (lignes 0 à 43), la case inférieure gauche du château (c’est-à-dire la case (43, 0)) pour une sous-fenêtre turtle allant de (-240, -240) à (50, 200) vaudra (-240, -240).

Définir une fonction tracer_carre(dimension), traçant un carré dont la dimension en pixels turtle est donnée en argument.

Définir une fonction tracer_case(case, couleur, pas), recevant en arguments un couple de coordonnées en indice dans la matrice contenant le plan, une couleur, et un pas (taille d'un côté) et qui va appeler la fonction tracer_carre pour tracer un carré d’une certaine couleur et taille à un certain endroit.

Définir enfin une fonction afficher_plan(matrice), qui va appeler la fonction tracer_case pour chaque ligne et chaque colonne du plan, par deux boucles imbriquées. Le principe est : pour chaque élément ligne de la matrice, pour chaque élément colonne de cet élément ligne, tracer une case à l’emplacement correspondant, dans une couleur correspondant à ce que dit la matrice.

CORPS DU PROGRAMME AU NIVEAU 1
Il restera alors à écrire la suite d’instructions qui va :

fixer les valeurs nécessaires (noms des fichiers de données, couleurs des divers types de cases, points définissant les différentes zones de l’écran),

appeler les différentes fonctions nécessaires pour créer la matrice et tracer le plan,

et à réaliser un premier script complet, contenant l’ensemble des éléments (docstrings, import, définitions des constantes, des fonctions et corps du programme) tel qu’expliqué dans le manuel des bonnes pratiques

![Tux, the Linux mascot](https://studio.fun-mooc.fr/asset-v1:ulb+44013+session04+type@asset+block/video_jeu.gif)