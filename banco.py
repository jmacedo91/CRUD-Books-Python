# Importando SQLite
import sqlite3 as lite

# Criando Conexão
con = lite.connect('dados.db')

# Criando Tabela
with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE biblioteca(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
     Livro TEXT, Autor TEXT, Editora TEXT, Genero TEXT, Data DATE, Pais TEXT)')

