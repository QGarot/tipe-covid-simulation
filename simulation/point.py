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
        self.on_attractor = False

    def get_vector(self, point):
        """
        Retourne le vecteur directeur : il indique la direction et le sens de déplacement vers le point indiqué
        en paramètre.
        C'est un vecteur unitaire.
        :return:
        """
        dx = point.x - self.x
        dy = point.y - self.y
        norm = self.distance(point, distance_type="a")

        return dx/norm, dy/norm

    def draw_vector(self, vector):
        self.canvas.create_line(self.x, self.y, self.x + vector[0], self.y + vector[1], width=2, fill="black", arrow="last")

    def distance(self, point, distance_type="b"):
        """
        Retourne la distance séparant le point indiqué en paramètre et CE point (désigné par l'objet self)
        ATTENTION :
            Si distance_type = "a", ce n'est pas la distance séparant les centres des deux disques qui est
            calculée, mais la plus petite distance séparant leurs extrémités.
        """
        dx = point.x - self.x
        dy = point.y - self.y
        dist = math.sqrt(dx ** 2 + dy ** 2)
        if distance_type == "a":
            return dist - self.diameter
        else:
            return dist

    def get_h(self, point0):
        """
        Retourne l'insatisfaction. L'insatisfaction d'un individu correspond à la distance qu'il lui reste à
        parcourir pour atteindre le point attracteur, indiqué en paramètre.
        :return:
        """

        return self.distance(point0)

    def move_to(self, vector, attractor_point):
        """
        Translation du point selon le vecteur entré en paramètre
        :param point:
        :return:
        """

        x0 = attractor_point.get_x() - attractor_point.get_diameter()/2
        y0 = attractor_point.get_y() - attractor_point.get_diameter()/2
        x1 = attractor_point.get_x() + attractor_point.get_diameter()/2
        y1 = attractor_point.get_y() + attractor_point.get_diameter()/2

        if self.id in self.canvas.find_overlapping(x0, y0, x1, y1):
            self.on_attractor = True
        else:
            # On supprime le point ...
            self.canvas.delete(self.id)

            # ... on calcule les nouvelles coordonnées ...
            self.x = self.x + vector[0]
            self.y = self.y + vector[1]

            # ... pour ensuite le redessiner avec les nouvelles coordonnées
            self.draw()

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
