from neo4j import GraphDatabase

class FamilyGraphClient:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def consultar_engenheiros(self):
        query = "MATCH (p:Pessoa:Engenheiro) RETURN p.nome AS nome"
        with self.driver.session() as session:
            result = session.run(query)
            print("Engenheiros na família:")
            for record in result:
                print(record["nome"])

    def consultar_pai(self, nome):
        query = f"MATCH (p1)-[:PAI_DE]->(p2 {{nome: '{nome}'}}) RETURN p1.nome AS nome"
        with self.driver.session() as session:
            result = session.run(query)
            for record in result:
                print(f"{record['nome']} é pai de {nome}")

    def consultar_relacionamentos(self, nome):
        query = f"MATCH (p1 {{nome: '{nome}'}})-[r]->(p2) RETURN type(r) AS relacao, p2.nome AS nome"
        with self.driver.session() as session:
            result = session.run(query)
            print(f"Relacionamentos de {nome}:")
            for record in result:
                print(f"{record['relacao']} com {record['nome']}")

# Uso do client
client = FamilyGraphClient("bolt://localhost:7687", "neo4j", "senha")

# Consultas
client.consultar_engenheiros()
client.consultar_pai("Ana")
client.consultar_relacionamentos("João")

# Fechar conexão
client.close()
