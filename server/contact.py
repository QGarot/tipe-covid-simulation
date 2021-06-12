import datetime
from server.database import Database


class Contact:
    def __init__(self, users: tuple, region: str):
        self.users = users
        self.region = region
        self.date = datetime.date.today()

    @staticmethod
    def get_db_attributes() -> str:
        """
        Retourne la chaîne de caractère correspondant aux attributs de la table 'users'.

        :return: str
        """
        return "(userid1, userid2, region, date)"
        
    def get_values(self):
        return self.get_users()[0], self.get_users()[1], self.get_region(), self.get_date()

    def get_users(self) -> tuple:
        return self.users

    def get_region(self) -> str:
        return self.region

    def get_date(self) -> datetime.date:
        return self.date
        
    def insert_db(self, db: Database) -> None:
        """
        """
        
        request = "INSERT INTO contacts " + self.get_db_attributes() + " VALUES (%s, %s, %s, %s)"
        db.set(request, self.get_values())
        print("OK!")
