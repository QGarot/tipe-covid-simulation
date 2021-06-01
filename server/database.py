import mysql.connector
from mysql.connector.cursor import MySQLCursor


class Database:
    def __init__(self, host: str, user: str, password: str, database_name: str) -> None:
        """
        Cette classe permet de gèrer les actions effectuées sur la base de données sélectionnée.

        :param host: Hôte du server MySQL
        :param user: Nom d'utilisateur
        :param password: Mot de passe
        :param database_name: Nom de la base de données
        """
        self.connection = mysql.connector.connect(
            host=host,
            port=3306,
            user=user,
            database=database_name,
            password=password
        )

        self.cursor = self.connection.cursor()

    def get_cursor(self) -> MySQLCursor:
        """
        Le curseur est un objet permettant d'éxécuter des requêtes SQL.

        :return: Le curseur de la BDD sur laquelle on est connecté.
        """
        return self.cursor

    def insert(self, sql: str) -> None:
        """
        Permet d'éxécuter une requête SQL pour insérer une ligne dans une table.

        :param sql: Requête SQL
        :return: None
        """
        self.get_cursor().execute(sql)
        self.connection.commit()
        return None

    def query(self, sql: str) -> list:
        """
        Retourne une liste correspondant aux enregistrements retournés par la requête.
        Cette liste contient des n-uplets si n attributs sont sélectionnés dans la requête.

        :param sql: Requête SQL
        :return: list
        """
        self.get_cursor().execute(sql)
        result = self.get_cursor().fetchall()
        return result
