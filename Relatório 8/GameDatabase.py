from neo4j import GraphDatabase

class GameDatabase:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    # Método para criar um jogador
    def create_player(self, player_id, name):
        query = """
        MERGE (p:Player {id: $player_id})
        SET p.name = $name
        """
        with self.driver.session() as session:
            session.run(query, player_id=player_id, name=name)

    # Método para atualizar um jogador
    def update_player(self, player_id, name):
        query = """
        MATCH (p:Player {id: $player_id})
        SET p.name = $name
        """
        with self.driver.session() as session:
            session.run(query, player_id=player_id, name=name)

    # Método para deletar um jogador
    def delete_player(self, player_id):
        query = """
        MATCH (p:Player {id: $player_id})
        DETACH DELETE p
        """
        with self.driver.session() as session:
            session.run(query, player_id=player_id)

    # Método para criar uma partida
    def create_match(self, match_id, players, result):
        query = """
        MERGE (m:Match {id: $match_id, result: $result})
        WITH m
        MATCH (p:Player)
        WHERE p.id IN $players
        MERGE (p)-[:PARTICIPATED_IN]->(m)
        """
        with self.driver.session() as session:
            session.run(query, match_id=match_id, players=players, result=result)

    # Método para recuperar um jogador pelo ID
    def get_player(self, player_id):
        query = """
        MATCH (p:Player {id: $player_id})
        RETURN p.id AS id, p.name AS name
        """
        with self.driver.session() as session:
            result = session.run(query, player_id=player_id)
            return result.single()

    # Método para listar todos os jogadores
    def get_all_players(self):
        query = """
        MATCH (p:Player)
        RETURN p.id AS id, p.name AS name
        """
        with self.driver.session() as session:
            result = session.run(query)
            return [record for record in result]

    # Método para obter os detalhes de uma partida
    def get_match(self, match_id):
        query = """
        MATCH (m:Match {id: $match_id})
        OPTIONAL MATCH (p:Player)-[:PARTICIPATED_IN]->(m)
        RETURN m.id AS match_id, m.result AS result, collect(p.name) AS players
        """
        with self.driver.session() as session:
            result = session.run(query, match_id=match_id)
            return result.single()

    # Método para obter o histórico de partidas de um jogador
    def get_player_match_history(self, player_id):
        query = """
        MATCH (p:Player {id: $player_id})-[:PARTICIPATED_IN]->(m:Match)
        RETURN m.id AS match_id, m.result AS result
        """
        with self.driver.session() as session:
            result = session.run(query, player_id=player_id)
            return [record for record in result]

    # Método para deletar uma partida
    def delete_match(self, match_id):
        query = """
        MATCH (m:Match {id: $match_id})
        DETACH DELETE m
        """
        with self.driver.session() as session:
            session.run(query, match_id=match_id)
