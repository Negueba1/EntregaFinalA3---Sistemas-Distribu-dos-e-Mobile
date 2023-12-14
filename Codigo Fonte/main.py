import sqlite3

from Clientes.Cliente import buscar_cliente_id, cadastrar_clientes, criando_table_clientes, insert_inicial_clientes, listagem_clientes
from Produto.Produto import buscar_produto_id, cadastrar_produtos, criando_table_produtos, insert_inicial_produtos, listagem_produtos
from Relatório.Relatorio import relatorio_consumo_medio_cliente, relatorio_produto_baixo_estoque, relatorio_produto_por_cliente, relatorio_produtos_mais_vendidos
from Venda.venda import criando_table_vendas, venda

conn = sqlite3.connect('database.db') 
c = conn.cursor()

# =//=//=//=//=//=//=//= Chamando a função p/ Criar Tabelas Iniciais do Banco =//=//=//=//=//=//=//=
criando_table_clientes()
criando_table_produtos()
criando_table_vendas()

# =//=//=//=//=//=//=//= Chamando a função p/ Inserir dados Iniciais no Banco =//=//=//=//=//=//=//=
insert_inicial_clientes()
insert_inicial_produtos()

# =//=//=//=//=//=//=//= Função pra Encerrar o Programa =//=//=//=//=//=//=//=
def encerrar_programa():
    print('Encerrando Programa')
    conn.close()


# =//=//=//=//=//=//=//= TELA INICIAL DO PROGRAMA =//=//=//=//=//=//=//=
def main():
    while True:
        print("1. Modulo Cliente")
        print("2. Modulo Produto")
        print("3. Modulo Venda")
        print("4. Modulo Relatorio")
        print("5. Encerrar Programa")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            modulo_cliente(ativo=True)
        elif opcao == "2":
            modulo_produto(ativo=True)
        elif opcao == "3":
            modulo_venda(ativo=True)
        elif opcao == "4":
            modulo_relatorio(ativo=True)
        elif opcao == "5":
            encerrar_programa()
            break
        else:
            print("Opção inválida. Tente novamente.")


def modulo_cliente(ativo):
    while ativo:
       print("=//==//==//= Bem Vindo ao Modulo Cliente, escolha uma das opções abaixo! =//==//==//=")
       print("1. Buscar Cliente por ID")
       print("2. Cadastrar Clientes")
       print("3. Listagem Clientes")
       print("4. Voltar ao Home")

       opcao = input("Escolha uma opção: ")

       if opcao == "1":
            buscar_cliente_id()
       elif opcao == "2":
            cadastrar_clientes()
       elif opcao == "3":
            listagem_clientes()
       elif opcao == "4":
            ativo = False
       else:
            print("Opção inválida. Tente novamente.")

def modulo_produto(ativo):
    while ativo:
       print("=//==//==//= Bem Vindo ao Modulo Produto, escolha uma das opções abaixo! =//==//==//=")
       print("1. Buscar Produto por ID")
       print("2. Cadastrar Produtos")
       print("3. Listagem Produtos")
       print("4. Voltar ao Home")

       opcao = input("Escolha uma opção: ")

       if opcao == "1":
            buscar_produto_id()
       elif opcao == "2":
            cadastrar_produtos()
       elif opcao == "3":
            listagem_produtos()
       elif opcao == "4":
            ativo = False
       else:
            print("Opção inválida. Tente novamente.")
            
def modulo_venda(ativo):
    while ativo:
       print("=//==//==//= Bem Vindo ao Modulo de Vendas, escolha uma das opções abaixo! =//==//==//=")
       print("1. Realizar Venda")
       print("2. Voltar ao Home")

       opcao = input("Escolha uma opção: ")

       if opcao == "1":
            venda()
       elif opcao == "2":
            ativo = False
       else:
            print("Opção inválida. Tente novamente.")

def modulo_relatorio(ativo):
    while ativo:
       print("=//==//==//= Bem Vindo ao Modulo de Relatórios, escolha uma das opções abaixo! =//==//==//=")
       print("1. Relatório de produtos mais vendidos")
       print("2. Relatório de produtos vendidos para o cliente")
       print("3. Relatório de consumo médio do cliente")
       print("4. Relatório de produtos com baixo estoque")
       print("5. Voltar ao Home")

       opcao = input("Escolha uma opção: ")

       if opcao == "1":
            print("Relatório de produtos mais vendidos:")
            print(relatorio_produtos_mais_vendidos())
       elif opcao == "2":
            id = input("Insira o ID do Cliente: ")
            print("Relatório de produtos vendidos para o cliente:", id)
            print(relatorio_produto_por_cliente(id))
       elif opcao == "3":
            print("Relatório de consumo médio do cliente:")
            print(relatorio_consumo_medio_cliente())
       elif opcao == "4":
            print("Relatório de produtos com baixo estoque:")
            print(relatorio_produto_baixo_estoque())
       elif opcao == "5":
            ativo = False
       else:
            print("Opção inválida. Tente novamente.")

# =//=//=//=//=//=//=//= Informando que a função "main" é a função principal do programa =//=//=//=//=//=//=//=
if __name__ == "__main__":
    main()
