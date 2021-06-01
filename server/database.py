import mysql.connector
from mysql.connector.cursor import MySQLCursor


class Database:
    def __init__(self, host: str, user: str, password: str, database_name: str) -> None:
        self.connection = mysql.connector.connect(
            host=host,
            port=3306,
            user=user,
            database=database_name,
            password=password
        )

    def get_cursor(self) -> MySQLCursor:
        return self.connection.cursor()

    def insert(self, sql: str) -> None:
        self.get_cursor().execute(sql)
        self.connection.commit()
        return None

    def query(self, sql: str) -> list:
        self.get_cursor().execute(sql)
        result = self.get_cursor().fetchall()
        return result
