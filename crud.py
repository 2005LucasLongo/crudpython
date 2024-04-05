# Usado para criar a conexão
import mysql.connector

# Comandos SQL
import querys

# Connection Factory
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='CRUDPython'
)

cursor = conexao.cursor()

# CRUD
while True:
    print('Escolha uma tabela para manipular:\n0 - Sair\n1 - Clientes\n2 - Produtos')
    opcao = int(input('Sua escolha: '))
    match opcao:
        case 0:
            break
        case 1: # tabela clientes
            while True:
                print('\nVocê está na tabela de clientes!')
                opcao = int(input('Selecione uma ação: \n0 - Voltar\n1 - Ler registros\n2 - Cadastrar\n3 - Atualizar\n4 - Deletar\nSua escolha: '))
                print('')
                match opcao:
                    case 0:
                        break
                    case 1: # read
                        querys.readClientes(cursor)
                    case 2: # create
                        querys.createCliente(cursor, conexao)
                    case 3: # update
                        querys.updateCliente(cursor, conexao)
                    case 4: # delete
                        querys.deleteCliente(cursor, conexao)
        case 2: # tabela produtos
            while True:
                print('\nVocê está na tabela de produtos!')
                opcao = int(input('Selecione uma ação: \n0 - Voltar\n1 - Ler registros\n2 - Cadastrar\n3 - Atualizar\n4 - Deletar\nSua escolha: '))
                print('')
                match opcao:
                    case 0:
                        break
                    case 1: # read
                        querys.readProdutos(cursor)
                    case 2: # create
                        querys.createProduto(cursor, conexao)
                    case 3: # update
                        querys.updateProdutos(cursor, conexao)
                    case 4: # delete
                        querys.deleteProdutos(cursor, conexao)
        case _:
            print('Opcão inválida. Tente novamente.')
    print('')

print('\nFechando conexão...')

# Fim do código
cursor.close()
conexao.close()
print('Fim do programa.')