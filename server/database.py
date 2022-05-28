import mysql.connector


class Database:
    def __init__(self, host, user, password, database_name):
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

    def get_cursor(self):
        """
        Le curseur est un objet permettant d'éxécuter des requêtes SQL.

        :return: Le curseur de la BDD sur laquelle on est connecté.
        """
        return self.cursor

    def update(self, table_name, attribute, new_value, condition):
        """
        Permet de mettre à jour des données.
        :param table_name:
        :param attribute:
        :param new_value:
        :param condition:
        :return:
        """
        sql = "UPDATE " + table_name + " SET " + attribute + " = '" + new_value + "' WHERE " + condition
        self.get_cursor().execute(sql)
        self.connection.commit()

    def insert(self, table_name, structure, values):
        """
        Permet d'enregistrer des valeurs dans la table table_name.

        :param table_name: Nom de la table
        :param structure: Structure de la table
        :param values: Les attributs sous forme de liste ou de tuple
        :return: None
        """
        sql = "INSERT INTO " + table_name + " " + structure + " VALUES " + str(values)
        self.get_cursor().execute(sql)
        self.connection.commit()

    def select(self, attributes, table_name, condition=None):
        """
        Retourne une liste correspondant aux enregistrements retournés par la requête.
        Cette liste contient des n-uplets si n attributs sont sélectionnés dans la requête.

        :param condition:
        :param table_name:
        :param attributes:
        :return: list
        """
        if condition is not None:
            sql = "SELECT " + attributes + " FROM " + table_name + " WHERE " + condition
        else:
            sql = "SELECT " + attributes + " FROM " + table_name

        self.get_cursor().execute(sql)
        result = self.get_cursor().fetchall()
        return result
