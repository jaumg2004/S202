from GameDatabase import GameDatabase

# Configurar a conexão com o Neo4j
db = GameDatabase(uri="bolt://localhost:7687", user="neo4j", password="password")

# Criar jogadores
db.create_player("1", "Alice")
db.create_player("2", "Bob")

# Atualizar um jogador
db.update_player("2", "Bobby")

# Criar uma partida
db.create_match("101", ["1", "2"], "Alice venceu")

# Obter detalhes de um jogador
player = db.get_player("1")
print(player)

# Obter todos os jogadores
players = db.get_all_players()
print(players)

# Obter o histórico de partidas de um jogador
history = db.get_player_match_history("1")
print(history)

# Obter os detalhes de uma partida
match = db.get_match("101")
print(match)

# Deletar um jogador
db.delete_player("2")

# Deletar uma partida
db.delete_match("101")

# Fechar a conexão com o banco de dados
db.close()
