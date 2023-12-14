import sqlite3

from datetime import datetime

from Produto.Produto import buscar_produto_por_id_venda

conn = sqlite3.connect('database.db') 
c = conn.cursor()

# =//=//=//=//=//=//=//= Função pra Criar a Tabela inicial de Produtos =//=//=//=//=//=//=//=
def criando_table_vendas():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_cliente INTEGER,
        id_produto INTEGER,
        qtd_estoque INTEGER,
        data_venda TEXT,
        FOREIGN KEY (id_cliente) REFERENCES clientes (id),
        FOREIGN KEY (id_produto) REFERENCES produtos (id)
    )''')

    conn.commit()
    conn.close()

def realizar_venda(id_cliente, id_produto, qtd_estoque):
    produto = buscar_produto_por_id_venda(id_produto)
    if produto and produto[3] >= qtd_estoque:
        data_venda = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.execute("INSERT INTO vendas (id_cliente, id_produto, qtd_estoque, data_venda) VALUES (?, ?, ?, ?)", (id_cliente, id_produto, qtd_estoque, data_venda))
        novo_estoque = produto[3] - qtd_estoque
        c.execute('''
            UPDATE produtos
            SET qtd_estoque = ?
            WHERE id = ?
        ''', (novo_estoque, id_produto))
        conn.commit()
        return True
    else:
        print("Não foi possivel realizar a venda pois não temos saldo em estoque desse produto.")
        return False
    
def venda():
    id_cliente = input("Insirao ID do Cliente: ")
    id_produto = input("Insirao ID do Produto: ")
    qtd_estoque = int(input("Insirao Quantidade do Produto: "))

    realizar_venda(id_cliente, id_produto, qtd_estoque)