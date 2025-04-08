import sqlite3

conn = sqlite3.connect('meds.db')
cursor = conn.cursor()

# Criação da tabela meds se não existir
# Esta tabela armazena os medicamentos com os seguintes campos:
cursor.execute('''
    CREATE TABLE IF NOT EXISTS meds (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        codigo_ficticio TEXT NOT NULL,
        validade DATE NOT NULL,
        preco REAL NOT NULL
    )
''')

# Função para inserir medicamentos
def inserir_medicamento(nome, codigo_ficticio, validade, preco):
    cursor.execute('''
        INSERT INTO meds (name, codigo_ficticio, validade, preco)
        VALUES (?, ?, ?, ?)
    ''', (nome, codigo_ficticio, validade, preco))
    conn.commit()

# Função para consultar medicamentos
# Esta função retorna todos os medicamentos cadastrados no banco de dados   
def consultar_medicamentos():
    cursor.execute('SELECT * FROM meds')
    return cursor.fetchall()

inserir_medicamento('Paracetamol', '123456', '2025-12-31', 10.50)
inserir_medicamento('Ibuprofeno', '654321', '2024-06-30', 15.75)
inserir_medicamento('AAS', '789012', '2023-11-30', 8.99)
inserir_medicamento('Dipirona', '345678', '2026-01-15', 12.00)
inserir_medicamento('Omeprazol', '901234', '2025-05-20', 20.00)
inserir_medicamento('Amoxicilina', '567890', '2024-08-10', 25.50)
inserir_medicamento('Cetirizina', '234567', '2023-12-31', 18.00)
inserir_medicamento('Losartana', '890123', '2025-03-15', 30.00)
inserir_medicamento('Simvastatina', '456789', '2024-07-20', 22.50)
inserir_medicamento('Tadalafila', '012345', '2023-10-31', 35.00)
inserir_medicamento('Sertralina', '678901', '2025-02-28', 40.00)
inserir_medicamento('Metformina', '234567', '2024-09-15', 28.00)
inserir_medicamento('Atorvastatina', '890123', '2023-11-30', 32.50)
inserir_medicamento('Levotiroxina', '456789', '2025-04-10', 45.00)
inserir_medicamento('Clonazepam', '012345', '2024-12-31', 50.00)
inserir_medicamento('Fluoxetina', '678901', '2023-10-15', 55.00)
inserir_medicamento('Ranitidina', '234567', '2025-01-20', 60.00)
inserir_medicamento('Loratadina', '890123', '2024-03-05', 65.00)
inserir_medicamento('Furosemida', '456789', '2023-09-30', 70.00)

# Consultar medicamentos cadastrados
medicamentos = consultar_medicamentos()
for med in medicamentos:
    print(f'ID: {med[0]}, Nome: {med[1]}, Código Fictício: {med[2]}, Validade: {med[3]}, Preço: {med[4]}')

# este código fecha a conexão com o banco de dados   
conn.close()

        