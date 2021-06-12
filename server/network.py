from socket import socket, AF_INET, SOCK_STREAM
from server.database import Database
from server.logger import info, error, line


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.db = None

        self.initialize()

    def init_database(self) -> None:
        """
        Se connecte à la base de données.

        :return:
        """
        try:
            self.db = Database("127.0.0.1", "root", "", "tipe")
            info("Connecté à la base de données")
        except:
            error("Une erreur est survenue lors de la connexion à la base de données")

    def initialize(self) -> None:
        """
        Initialise le serveur (se connecte à la base de données, charge les tables, etc...)

        :return: None
        """

        self.init_database()

    def __create_socket(self) -> socket:
        """
        Définit l'attribut socket du serveur et le met à l'écoute.
        Méthodes de l'objet socket :
        -> listen()
        -> accept()
        -> connect()
        -> send()
        -> recv()

        :return: socket
        """
        s = socket(AF_INET, SOCK_STREAM)

        # Liaison du socket à l'host et au port indiqué en paramètre
        s.bind((self.host, self.port))

        return s

    def run(self):
        sock = self.__create_socket()
        info("Serveur lancé !")
        sock.listen()
        while True:
            conn, address = sock.accept()
            info("Nouvelle connexion" + str(conn) + " / " + str(address))
