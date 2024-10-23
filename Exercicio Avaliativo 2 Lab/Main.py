from teacher_crud import TeacherCRUD
from query import Database

db = Database("bolt://44.207.0.158", "neo4j", "stones-jurisdiction-storm")
teacher_crud = TeacherCRUD(db)

# 1. Criar um Professor
teacher_crud.create('Chris Lima', 1956, '189.052.396-66')

# 2. Ler (consultar) o Professor
print(teacher_crud.read('Chris Lima'))

# 3. Atualizar o CPF do Professor
teacher_crud.update('Chris Lima', '162.052.777-77')

# 4. Deletar o Professor
teacher_crud.delete('Chris Lima')

# Fechar a conexão com o banco de dados
db.close()
