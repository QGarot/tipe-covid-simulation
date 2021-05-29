import mysql.connector
from mysql.connector import MySQLConnection, errorcode


def connection(host: str, user: str, password: str, dbname: str) -> MySQLConnection:
    try:
        return mysql.connector.connect(user=user, password=password, host=host, database=dbname)
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Mauvais utilisateur ou mauvais mot de passe")
        elif error.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de données indiquées n'existe pas.")
        else:
            print(error)
