from neo4j import GraphDatabase

class Database:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def query(self, query):
        with self.driver.session() as session:
            result = session.run(query)
            return [record for record in result]

# Instanciar a classe Database
db = Database("bolt://44.207.0.158", "neo4j", "stones-jurisdiction-storm")

# Consultas da Questão 01
query1 = 'MATCH (t:Teacher {name: "Renzo"}) RETURN t.ano_nasc, t.cpf'
query2 = 'MATCH (t:Teacher) WHERE t.name STARTS WITH "M" RETURN t.name, t.cpf'
query3 = 'MATCH (c:City) RETURN c.name'
query4 = 'MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name, s.address, s.number'

# Executar e imprimir resultados
print(db.query(query1))
print(db.query(query2))
print(db.query(query3))
print(db.query(query4))

# Consultas da Questão 02
query5 = 'MATCH (t:Teacher) RETURN min(t.ano_nasc) AS mais_velho, max(t.ano_nasc) AS mais_jovem'
query6 = 'MATCH (c:City) RETURN avg(c.population) AS media_habitantes'
query7 = 'MATCH (c:City {cep: "37540-000"}) RETURN replace(c.name, "a", "A") AS nome_alterado'
query8 = 'MATCH (t:Teacher) RETURN substring(t.name, 2, 1) AS caractere_terceiro'

print(db.query(query5))
print(db.query(query6))
print(db.query(query7))
print(db.query(query8))

# Fechar a conexão após todas as consultas
db.close()
