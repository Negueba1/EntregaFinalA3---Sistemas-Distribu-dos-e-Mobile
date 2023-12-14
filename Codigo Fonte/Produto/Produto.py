import sqlite3

conn = sqlite3.connect('database.db') 
c = conn.cursor()

# =//=//=//=//=//=//=//= Função pra Criar a Tabela inicial de Produtos =//=//=//=//=//=//=//=
def criando_table_produtos():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS produtos
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 nome TEXT NOT NULL,
                 preco REAL NOT NULL,
                 qtd_estoque INTEGER)''')

    conn.commit()
    conn.close()



# =//=//=//=//=//=//=//= Função pra Inserir dados iniciais de Produtos =//=//=//=//=//=//=//=
def insert_inicial_produtos():
    conn = sqlite3.connect('database.db') 
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM produtos")
    count = c.fetchone()[0]

    if count == 0:
        #Inserindo Informações Iniciais na Tabela de Produto
        insert_produtos("Macarrão", "8.99", 50)
        insert_produtos("Feijão", "10.99", 50)
        insert_produtos("Arroz", "6.99", 50)


# =//=//=//=//=//=//=//= Função pra Inserir dados de Produtos =//=//=//=//=//=//=//=
def insert_produtos(nome, preco, quantidade):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("INSERT INTO produtos (nome, preco, qtd_estoque) VALUES (?, ?, ?)",
              (nome, preco, quantidade))

    conn.commit()
    conn.close()

# =//=//=//=//=//=//=//= Função pra Buscar dados de Produtos por ID =//=//=//=//=//=//=//=
def buscador_produto(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT * FROM produtos WHERE id = ?",(id))
    rows = c.fetchall()

    for row in rows:
        print("ID:", row[0])
        print("Nome Produto:", row[1])
        print("Preço: R$", row[2])
        print("Quantidade:", row[3])
        print("")

    conn.close()

# =//=//=//=//=//=//=//= Função pra Listar dados de Produtos =//=//=//=//=//=//=//=
def listagem_produtos():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT * FROM produtos")
    rows = c.fetchall()

    for row in rows:
        print("ID:", row[0])
        print("Nome Produto:", row[1])
        print("Preço: R$", row[2])
        print("Quantidade:", row[3])
        print("")

    conn.close()

# =//=//=//=//=//=//=//= Função pra Cadastrar dados de Produto =//=//=//=//=//=//=//=
def cadastrar_produtos():
    nome = input("Nome do Produto: ")
    preco = input("Preço do Produto: ")
    quantidade = input("Quantidade do Produto: ")

    insert_produtos(nome, preco, quantidade)

# =//=//=//=//=//=//=//= Função pra Pegar o ID do Produto pra enviar pra Função de Buscar =//=//=//=//=//=//=//=
def buscar_produto_id():
    id = input("Insirao ID do Produto: ")

    buscador_produto(id)

# =//=//=//=//=//=//=//= Função pra Pegar o ID do Produto pra enviar pra Função de Vendas =//=//=//=//=//=//=//=
def buscar_produto_por_id_venda(id_produto):
    c.execute('''
        SELECT * FROM produtos
        WHERE id = ?
    ''', (id_produto,))
    return c.fetchone()
