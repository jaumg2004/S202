from Aluno import Aluno

class Aula(Aluno):
    alunos = []

    def __init__(self, professor, assunto):
        self.professor = professor
        self.assunto = assunto
        self.aluno = self.alunos

    def adicionar_aluno(self, aluno):
        self.aluno.append(aluno)

    def listar_presenca(self):
        print(f'Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:')
        for aluno in self.aluno:
            aluno.presenca()