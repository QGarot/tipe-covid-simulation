import datetime
from server.database import Database
from server.health_data import HealthData


class User:
    def __init__(self, id, contaminated):
        self.id = id
        self.contaminated = contaminated
        self.health_data = HealthData()

    @staticmethod
    def get_db_attributes() -> str:
        """
        Retourne la chaîne de caractère correspondant aux attributs de la table 'users'.

        :return: str
        """
        return "(contamine)"

    def initialize_health_data(self, type1=None, type2=None, type3=None):
        """
        On suppose que les clés de type1/2/3 sont conformes.
        :param type1:
        :param type2:
        :param type3:
        :return:
        """
        if type1 is None and type2 is None and type3 is None:
            self.health_data.generate()
        else:
            for key in type1.keys():
                self.health_data.type1[key] = type1[key]
            for key in type2.keys():
                self.health_data.type2[key] = type2[key]
            for key in type3.keys():
                self.health_data.type3[key] = type3[key]

    def get_values(self) -> tuple:
        """
        Retourne les valeurs des attributs correspondant à cet objet.

        :return: tuple
        """
        return self.get_contamination(),

    def get_contamination(self) -> int:
        """
        Retourne " l'état " de l'invividu :
        0 pour un individu sain, 1 pour un individu infecté et 3 pour un individ rétabli.

        :return: int
        """
        return self.contaminated

    def insert_db(self, db: Database) -> None:
        """
        Permet d'insérer les données de cet utilisateur dans la base de données indiquée en paramètre.

        :param db: Base de données
        :return:
        """
        request = "INSERT INTO users " + self.get_db_attributes() + " VALUES (%s)"
        db.set(request, self.get_values())
        print("OK!")
