import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
DATA_DIR = BASE_DIR / 'data'
DATA_DIR.mkdir(exist_ok=True)

DB_PATH = DATA_DIR / 'livraria.db'

# Conexão
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano_publicacao INTEGER NOT NULL,
    preco REAL NOT NULL
)
""")
conn.commit()

# CRUD
def adicionar_livro(titulo, autor, ano, preco):
    cursor.execute(
        "INSERT INTO livros (titulo, autor, ano_publicacao, preco) VALUES (?, ?, ?, ?)",
        (titulo, autor, ano, preco)
    )
    conn.commit()

def atualizar_preco(id_livro, novo_preco):
    cursor.execute("UPDATE livros SET preco = ? WHERE id = ?", (novo_preco, id_livro))
    conn.commit()
    return cursor.rowcount

def remover_livro(id_livro):
    cursor.execute("DELETE FROM livros WHERE id = ?", (id_livro,))
    conn.commit()
    return cursor.rowcount

def buscar_livros():
    cursor.execute("SELECT * FROM livros")
    return cursor.fetchall()

def buscar_por_autor(autor):
    cursor.execute("SELECT * FROM livros WHERE autor LIKE ?", (f'%{autor}%',))
    return cursor.fetchall()

def fechar_conexao():
    conn.close()
