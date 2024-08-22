from database import Database
from helper.WriteAJson import writeAJson

class Pokedex():
    def __init__(self, database, collection):
        self.db = Database(database, collection)

    def mostrarPokemons(self):
        pokemons = self.db.collection.find()

    def getPokemonByName(self, name: str):
        return self.db.collection.find({"name": name})

    def getPokemonsByType(self, types: list):
        return self.db.collection.find({"type": {"$in": types}})

    def getPokemonsByTypeOrType(self, types: list):
        return self.db.collection.find({ "type": {"$in": tipos}, "next_evolution": {"$exists": True} })

    def getPokemonsByWeaknesses(self, weaknesses: list):
        return self.db.collection.find({"weaknesses": {"$all": weaknesses}})

    def getPokemonsByFourthWeaknesses(self):
        return self.db.collection.find({"weaknesses": {"$size": 4}})

    def getPokemonsByTypeOrByWeaknesses(self, type: str):
        return self.db.collection.find({"$or": [{"type": type},{"weaknesses": type}]})