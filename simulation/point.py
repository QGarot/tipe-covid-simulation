import math
from random import random


class Point:
    """
    Cette classe modélise un individu par un cercle coloré.
    """
    def __init__(self, x, y, diameter, color, canvas):
        self.x = x
        self.y = y
        self.color = color
        self.canvas = canvas
        self.diameter = diameter
        self.id = None
        self.contacts = []
        self.neighbors = []

    def add_neighbor(self, point):
        """
        Pour simplifier, on considère que si un point devient voisin d'un autre, alors il le reste jusqu'à la fin de
        la simulation (supposition cohérente puisque les points bougent à la même vitesse vers la même destination).
        :param point:
        :return:
        """
        if point not in self.neighbors:
            self.neighbors.append(point)

    def is_contaminated(self):
        return self.color == "red"

    def is_healthy(self):
        return self.color == "green"

    def is_recovered(self):
        return self.color == "orange"

    def get_vector(self, point):
        """
        Retourne le vecteur directeur : il indique la direction et le sens de déplacement vers le point indiqué
        en paramètre.
        C'est un vecteur unitaire.
        :return:
        """
        dx = point.x - self.x
        dy = point.y - self.y
        norm = self.distance(point)

        return dx/norm, dy/norm

    def distance(self, point):
        """
        Retourne la distance séparant le point indiqué en paramètre et CE point (désigné par l'objet self)
        """
        dx = point.x - self.x
        dy = point.y - self.y
        dist = math.sqrt(dx ** 2 + dy ** 2)
        return dist

    def is_in_ball(self, center, radius):
        """
        Vérifie si le point self est dans la boule définie par son centre et son rayon.
        :param center:
        :param radius:
        :return:
        """
        return center.distance(self) <= radius

    def is_on_point(self, point):
        """
        Vérifie si le point self est sur le point indiqué en paramètre.
        :param point:
        :return:
        """
        radius = point.get_diameter() / 2
        return self.is_in_ball(point, radius)

    def move(self, vector):
        """
        Translation du point selon le vecteur entré en paramètre
        :param vector:
        :return:
        """
        # On met à jour ses nouvelles coordonnées
        self.x = self.x + vector[0]
        self.y = self.y + vector[1]

        # On déplace le point (dx <- vector[0] ; dy <- vector[1])
        self.canvas.move(self.id, vector[0], vector[1])

    def get_diameter(self):
        """
        Retourne le diamètre du cercle
        :return:
        """
        return self.diameter

    def get_color(self):
        """
        Retourne la couleur du point
        :return:
        """
        return self.color

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def draw(self):
        """
        Dessine le disque représentant l'individu dans le canvas sélectionné
        :return:
        """
        x0 = self.get_x() - self.get_diameter()/2
        y0 = self.get_y() - self.get_diameter()/2
        x1 = self.get_x() + self.get_diameter()/2
        y1 = self.get_y() + self.get_diameter()/2

        self.id = self.canvas.create_oval(x0, y0, x1, y1, fill=self.get_color())
        # self.canvas.create_text(x0, y0, text=self.id)

    def change_color(self, color):
        self.color = color
        self.canvas.itemconfig(self.id, fill=color)

    def contaminate(self, beta):
        """
        Cette fonction modélise la contamination du point.
        :return:
        """
        # On ne contamine que les individus sains...
        if self.is_healthy():
            k = random()
            # ... avec une probabilité beta
            if k <= beta:
                self.change_color("red")
                print(str(self.id) + " a été contaminé !")
            else:
                print(str(self.id) + " n'a pas été contaminé !")
