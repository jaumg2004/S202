class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ministrar_aula(self, assunto):
        print(f'O professor {self.nome} está ministrando uma aula sobre {assunto}.')