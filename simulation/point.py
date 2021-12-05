class Point:
    """
    Cette classe modélise un individu par un cercle coloré.
    """
    def __init__(self, x, y, color, canvas):
        self.x = x
        self.y = y
        self.color = color
        self.canvas = canvas
        self.diameter = 20
        self.id = None

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
        Dessine le cercle représentant l'individu dans le canvas sélectionné
        :return:
        """
        x0 = self.get_x() - self.get_diameter()/2
        y0 = self.get_y() - self.get_diameter()/2
        x1 = self.get_x() + self.get_diameter()/2
        y1 = self.get_y() + self.get_diameter()/2
        self.id = self.canvas.create_oval(x0, y0, x1, y1, fill=self.get_color())




