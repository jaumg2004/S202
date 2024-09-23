class Motorista:
    def __init__(self, corridas, nota):
        self.corridas = corridas
        self.nota = nota

    def to_dict(self):
        return {
            "corridas": [corrida.to_dict() for corrida in self.corridas],
            "nota": self.nota
        }