from MotoristaDAO import MotoristaDAO
from Motorista import Motorista
from Passageiro import Passageiro
from Corrida import Corrida

class MotoristaCLI:
    def __init__(self, motorista_dao):
        self.motorista_dao = motorista_dao

    def menu(self):
        while True:
            choice = input("1. Criar Motorista\n2. Ler Motorista\n3. Atualizar Motorista\n4. Deletar Motorista\n5. Sair\nEscolha uma opção: ")
            if choice == "1":
                self.create_motorista()
            elif choice == "2":
                self.read_motorista()
            elif choice == "3":
                self.update_motorista()
            elif choice == "4":
                self.delete_motorista()
            elif choice == "5":
                break

    def create_motorista(self):
        # Entrada de dados para Passageiro
        nome_passageiro = input("Nome do Passageiro: ")
        documento_passageiro = input("Documento do Passageiro: ")
        passageiro = Passageiro(nome_passageiro, documento_passageiro)

        # Entrada de dados para Corrida
        nota_corrida = int(input("Nota da Corrida: "))
        distancia = float(input("Distância percorrida (km): "))
        valor = float(input("Valor da Corrida (R$): "))
        corrida = Corrida(nota_corrida, distancia, valor, passageiro)

        # Criando o Motorista
        nota_motorista = int(input("Nota do Motorista: "))
        motorista = Motorista([corrida], nota_motorista)

        # Salvando no MongoDB e em JSON
        self.motorista_dao.create_motorista(motorista.to_dict())

    def read_motorista(self):
        motorista_id = input("ID do Motorista: ")
        motorista = self.motorista_dao.read_motorista(motorista_id)
        print(motorista)

    def update_motorista(self):
        motorista_id = input("ID do Motorista: ")
        nova_nota = int(input("Nova Nota do Motorista: "))
        self.motorista_dao.update_motorista(motorista_id, {"nota": nova_nota})

    def delete_motorista(self):
        motorista_id = input("ID do Motorista: ")
        self.motorista_dao.delete_motorista(motorista_id)
