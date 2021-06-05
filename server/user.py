import datetime
from server.database import Database


class User:
    def __init__(self, name: str, first_name: str, age: int, nationality: str):
        self.name = name
        self.first_name = first_name
        self.age = age
        self.nationality = nationality
        self.date_registration = datetime.date.today()

    @staticmethod
    def get_db_attributes() -> str:
        """
        Retourne la chaîne de caractère correspondant aux attributs de la table 'users'.

        :return: str
        """
        return "(nom, prenom, age, nationalite, date_enregistrement)"

    def get_values(self) -> tuple:
        """
        Retourne les valeurs des attributs correspondant à cet objet.

        :return: tuple
        """
        return self.get_name(), self.get_first_name(), self.get_age(), self.get_nationality(), datetime.date.today()

    def get_name(self) -> str:
        """
        Retourne le nom de famille de l'utilisateur.

        :return: str
        """
        return self.name

    def get_first_name(self) -> str:
        """
        Retourne le prénom de l'utilisateur.

        :return: str
        """
        return self.first_name

    def get_age(self) -> int:
        """
        Retourne l'âge de l'utilisateur.

        :return: int
        """
        return self.age

    def get_nationality(self) -> str:
        """
        Retourne la nationalité de l'utilisateur.

        :return: str
        """
        return self.nationality

    def get_date_registration(self) -> datetime.date:
        """
        Retourne la date d'enregistrement de l'utilisateur.

        :return: datetime.date
        """

        return self.date_registration

    def insert_db(self, db: Database) -> None:
        """
        Permet d'insérer les données de cet utilisateur dans la base de données indiquée en paramètre.

        :param db: Base de données
        :return:
        """
        request = "INSERT INTO users " + self.get_db_attributes() + " VALUES (%s, %s, %s, %s, %s)"
        db.set(request, self.get_values())
        print("OK!")
