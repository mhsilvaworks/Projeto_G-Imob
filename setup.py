import sqlite3

# 1. Conectar ao banco (cria o arquivo 'gerimovel.db' se não existir)
conn = sqlite3.connect('gerimovel.db')
cursor = conn.cursor()

# 2. Habilitar chaves estrangeiras
cursor.execute("PRAGMA foreign_keys = ON;")

# --- CRIANDO AS TABELAS ---

# Tabela: Inquilino
cursor.execute('''
CREATE TABLE IF NOT EXISTS Inquilino (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT UNIQUE,
    descricao TEXT,
    data_nascimento TEXT,
    telefone TEXT,
    foto BLOB                 
);
''')

# Tabela: Imovel
cursor.execute('''
CREATE TABLE IF NOT EXISTS Imovel (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    endereco TEXT NOT NULL,
    cep TEXT,
    foto BLOB                  
);
''')

# Tabela: Contrato (Mantém a lógica de ligar os dois)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Contrato (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    inquilino_id INTEGER NOT NULL,
    imovel_id INTEGER NOT NULL,
    data_inicio TEXT NOT NULL,
    data_fim TEXT NOT NULL,
    valor REAL NOT NULL,
    dia_pagamento INTEGER NOT NULL,
    
    FOREIGN KEY (inquilino_id) REFERENCES Inquilino(id),
    FOREIGN KEY (imovel_id) REFERENCES Imovel(id)
);
''')

print("Banco de dados criado!")

conn.commit()
conn.close()