from Database import Database
from MotoristaDAO import MotoristaDAO
from MotoristaCLI import MotoristaCLI

def main():
    # Conecta ao MongoDB Atlas
    uri = "mongodb://localhost:27017/"  # Substitua com sua URI do MongoDB Atlas
    database = Database(uri)

    # Inicializa o DAO para Motoristas
    motorista_dao = MotoristaDAO(database)

    # Inicializa a CLI
    motorista_cli = MotoristaCLI(motorista_dao)

    # Executa o menu CLI
    motorista_cli.menu()

if __name__ == "__main__":
    main()
