import sqlite3 as lite

# CRUD

# Create = Inserir / Criar
# Read = Ler / Acessar
# Update =  Atualizar
# Delete = Deletar

# Criando conexão
con = lite.connect('dados.db')


# Inserir Dados (Create)
def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO biblioteca (Livro, Autor, Editora, Genero, Data, Pais) VALUES (?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)


# Ler Dados (Read)
def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM biblioteca"
        cur.execute(query)
        informacao = cur.fetchall()

        for i in informacao:
            lista.append(i)
    return lista


# Atualizar Dados (Update)
def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE biblioteca SET Livro=?, Autor=?, Editora=?, Genero=?, Data=?, Pais=? WHERE id=?"
        cur.execute(query, i)

'''
# Deletar Dados (Delete)
lista = [1]
with con:
    cur = con.cursor()
    query = "DELETE FROM biblioteca WHERE id=?"
    cur.execute(query, lista)
'''