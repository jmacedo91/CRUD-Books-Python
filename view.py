import sqlite3 as lite

# CRUD

# Create = Inserir / Criar
# Read = Ler / Acessar
# Update =  Atualizar
# Delete = Deletar

# Criando conexão
con = lite.connect('dados.db')

lista = ['Fragmentos do Horror', 'Junji Ito', 'Darkside Books', 'Terror', '03/03/1991', 'Brasil']

# Inserir Dados (Create)
# lista = ['Fragmentos do Horror', 'Junji Ito', 'Darkside Books', 'Terror', '03/03/1991', 'Brasil']
# with con:
#     cur = con.cursor()
#     query = "INSERT INTO biblioteca (Livro, Autor, Editora, Genero, Data, Pais) VALUES (?, ?, ?, ?, ?, ?)"
#     cur.execute(query, lista)

# Ler Dados (Read)
with con:
    cur = con.cursor()
    query = "SELECT * FROM biblioteca"
    cur.execute(query)
    informacao = cur.fetchall()
    print(informacao)

# Atualizar Dados (Update)
# lista = ['Contos de Terror', 1]
# with con:
#     cur = con.cursor()
#     query = "UPDATE biblioteca SET Livro=? WHERE id=?"
#     cur.execute(query, lista)

# Deletar Dados (Delete)
lista = [1]
with con:
    cur = con.cursor()
    query = "DELETE FROM biblioteca WHERE id=?"
    cur.execute(query, lista)
