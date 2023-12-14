import sqlite3

conn = sqlite3.connect('database.db') 
c = conn.cursor()

# =//=//=//=//=//=//=//= Função pra Criar a Tabela inicial de Clientes =//=//=//=//=//=//=//=
def criando_table_clientes():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS clientes
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 nome TEXT NOT NULL,
                 email TEXT NOT NULL,
                 telefone TEXT)''')
   
    conn.commit()
    conn.close()

# =//=//=//=//=//=//=//= Função pra Inserir dados iniciais de Clientes =//=//=//=//=//=//=//=
def insert_inicial_clientes():
    conn = sqlite3.connect('database.db') 
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM clientes")
    count = c.fetchone()[0]

    if count == 0:
        #Inserindo Informações Iniciais na Tabela de Cliente
        insert_cliente("Jonas Fonseca", "jonas@gmail.com", "(71)98888-9999")
        insert_cliente("Frederick Rasmung", "fred@gmail.com", "(78)99999-9999")
        insert_cliente("Ramon Davilla", "davilla@gmail.com", "(71)98797-9787")

# =//=//=//=//=//=//=//= Função pra Inserir dados de Clientes =//=//=//=//=//=//=//=
def insert_cliente(nome, email, telefone=None):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)",
              (nome, email, telefone))

    conn.commit()
    conn.close()

# =//=//=//=//=//=//=//= Função pra Cadastrar dados de Cliente =//=//=//=//=//=//=//=
def cadastrar_clientes():
    nome = input("Nome do Cliente: ")
    email = input("Email do Cliente: ")
    telefone = input("Telefone do Cliente: ")

    insert_cliente(nome, email, telefone)

# =//=//=//=//=//=//=//= Função pra Listar dados de Cliente =//=//=//=//=//=//=//=
def listagem_clientes():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT * FROM clientes")
    rows = c.fetchall()

    for row in rows:
        print("ID:", row[0])
        print("Nome do Cliente:", row[1])
        print("Email do Cliente:", row[2])
        print("Telefone do Cliente:", row[3])
        print("")

    conn.close()

# =//=//=//=//=//=//=//= Função pra Buscar dados de Cliente por ID =//=//=//=//=//=//=//=
def buscador_cliente(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT * FROM clientes WHERE id = ?",(id))
    rows = c.fetchall()

    for row in rows:
        print("ID:", row[0])
        print("Nome do Cliente:", row[1])
        print("Email do Cliente:", row[2])
        print("Telefone do Cliente:", row[3])
        print("")

    conn.close()

# =//=//=//=//=//=//=//= Função pra Pegar o ID do Cliente pra enviar pra Função de Buscar =//=//=//=//=//=//=//=
def buscar_cliente_id():
    id = input("Insira o ID do Cliente: ")

    buscador_cliente(id)
