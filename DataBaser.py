import sqlite3
import sqlite3

#--- Criar conexão
conn = sqlite3.connect('UsersData.db')

#--- Cria cursor
cur = conn.cursor()

#--- Criar tabela
cur.execute("""
CREATE TABLE IF NOT EXISTS User (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Email TEXT NOT NULL,
    Usuario TEXT NOT NULL,
    Senha TEXT NOT NULL

);
""")

print("Conectado ao Banco de Dados!")