import sqlite3

conn = sqlite3.connect('database.db') 
c = conn.cursor()

def relatorio_produtos_mais_vendidos():
    c.execute('''
        SELECT produtos.nome, SUM(vendas.qtd_estoque) as total_vendido
        FROM produtos
        JOIN vendas ON produtos.id = vendas.id_produto
        GROUP BY produtos.id
        ORDER BY total_vendido DESC
    ''')
    return c.fetchall()

def relatorio_produto_por_cliente(id_cliente):
    c.execute('''
        SELECT produtos.nome, vendas.qtd_estoque
        FROM produtos
        JOIN vendas ON produtos.id = vendas.id_produto
        WHERE vendas.id_cliente = ?
    ''', (id_cliente,))
    return c.fetchall()

def relatorio_consumo_medio_cliente():
    c.execute('''
        SELECT clientes.nome, AVG(vendas.qtd_estoque) as consumo_medio
        FROM clientes
        JOIN vendas ON clientes.id = vendas.id_cliente
        GROUP BY clientes.id
    ''')
    return c.fetchall()

def relatorio_produto_baixo_estoque():
    c.execute('''
        SELECT * FROM produtos
        WHERE qtd_estoque < 10
    ''')
    return c.fetchall()