class TeacherCRUD:
    def __init__(self, database):
        self.db = database

    def create(self, name, ano_nasc, cpf):
        query = f'CREATE (t:Teacher {{name: "{name}", ano_nasc: {ano_nasc}, cpf: "{cpf}"}})'
        self.db.query(query)

    def read(self, name):
        query = f'MATCH (t:Teacher {{name: "{name}"}}) RETURN t.name, t.ano_nasc, t.cpf'
        return self.db.query(query)

    def update(self, name, newCpf):
        query = f'MATCH (t:Teacher {{name: "{name}"}}) SET t.cpf = "{newCpf}" RETURN t'
        self.db.query(query)

    def delete(self, name):
        query = f'MATCH (t:Teacher {{name: "{name}"}}) DELETE t'
        self.db.query(query)
