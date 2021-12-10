import math


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

    def distance(self, point):
        """
        Retourne la distance séparant le point indiqué en paramètre et CE point (désigné par l'objet self)
        :param point:
        :return:
        """
        dx = point.x - self.x
        dy = point.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def get_h(self, attractor_point):
        """
        Retourne l'insatisfaction. L'insatisfaction d'un individu correspond à la distance qu'il lui reste à
        parcourir pour atteindre le point attracteur.
        :return:
        """

        return self.distance(attractor_point)

    def move(self, dx, dy):
        """
        Déplace le point de dx (en x) et de dy en y
        :param dx:
        :param dy:
        :return:
        """

        self.canvas.move(self.id, dx, dy)

    def get_diameter(self):
        """
        Retourne le diamètre du cercle
        :return:
        """
        return self.diameter

    def get_color(self):
        """
        Retourne la couleur du cercle
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




