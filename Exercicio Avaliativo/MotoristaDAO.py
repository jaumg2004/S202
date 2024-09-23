from bson.objectid import ObjectId
from writeAJson import writeAJson

class MotoristaDAO:
    def __init__(self, db):
        self.collection = db.get_motoristas_collection()

    def create_motorista(self, motorista):
        result = self.collection.insert_one(motorista)
        print(f"Motorista inserido com ID: {result.inserted_id}")
        writeAJson(motorista, f"motorista_{result.inserted_id}")  # Salva o motorista como JSON

    def read_motorista(self, motorista_id):
        motorista = self.collection.find_one({"_id": ObjectId(motorista_id)})
        writeAJson(motorista, f"motorista_{motorista_id}")  # Salva o motorista lido como JSON
        return motorista

    def update_motorista(self, motorista_id, updated_data):
        self.collection.update_one({"_id": ObjectId(motorista_id)}, {"$set": updated_data})
        motorista = self.read_motorista(motorista_id)  # Lê os dados atualizados
        writeAJson(motorista, f"motorista_atualizado_{motorista_id}")  # Salva o motorista atualizado como JSON

    def delete_motorista(self, motorista_id):
        self.collection.delete_one({"_id": ObjectId(motorista_id)})
        print(f"Motorista com ID {motorista_id} deletado.")
