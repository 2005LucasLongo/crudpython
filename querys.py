# Querys

# Creates
def createCliente(cursor, conexao):
    while True:
        nome: str = str(input('Nome do cliente: '))
        query = f'INSERT INTO clientes (nome) VALUES ("{nome}");'
        print('Criando cliente...')
        try:
            cursor.execute(query)
            conexao.commit()
        except Exception as e:
            print(f'Erro ao criar cliente: {e}')
            print('Tente novamente.')
            continue
        else:
            print('Cliente criado com sucesso!')
            print(f'O ID do cliente criado foi: {cursor.lastrowid}')
            break

def createProduto(cursor, conexao):
    while True:
        nome: str = str(input('Nome do produto: '))
        preco: float = float(input('Preço do produto: R$ '))
        idcliente: int = int(input('ID do cliente: '))
        query = f'INSERT INTO produtos (nome, preco, ID_cliente) VALUES ("{nome}", {preco}, {idcliente});'
        print('Criando produto...')
        try:
            cursor.execute(query)
            conexao.commit()
        except Exception as e:
            print(f'Erro ao criar produto: {e}')
            print('Tente novamente.')
            continue
        else:
            print('Produto criado com sucesso!')
            print(f'O ID do produto criado foi: {cursor.lastrowid}')
            break

# Reads
def readClientes(cursor):
    query = 'SELECT * FROM clientes;'
    cursor.execute(query)
    resultado = cursor.fetchall()
    print('Listando clientes...')
    for c in range(0, len(resultado), 1):
        print(f'ID: {resultado[c][0]} | Nome: {resultado[c][1]}')

def readProdutos(cursor):
    query = 'SELECT * FROM produtos;'
    cursor.execute(query)
    resultado = cursor.fetchall()
    print('Listando produtos...')
    for c in range(0, len(resultado), 1):
        print(f'ID: {resultado[c][0]} | Nome: {resultado[c][1]} | Preço: {resultado[c][2]} | ID do comprador: {resultado[c][3]}')

# Update
def updateCliente(cursor, conexao):
    while True:
        ID: int = int(input('Qual o ID do cliente que você deseja alterar o nome? '))
        nomeNovo: str = str(input('Qual será o novo nome deste cliente? '))
        query = f'UPDATE clientes SET nome = "{nomeNovo}" WHERE ID = {ID}'
        print('Editando informações do cliente...')
        try:
            cursor.execute(query)
            conexao.commit()
        except Exception as e:
            print(f'Erro ao editar cliente: {e}')
            print('Tente novamente.')
            continue
        else:
            print('O nome do cliente foi alterado com sucesso!')
            break

def updateProdutos(cursor, conexao):
    ID_produto: int = int(input('Qual o ID do produto vendido que você deseja alterar o nome? '))
    alterarNomeProduto: bool = False
    if (str(input('Deseja alterar o nome do produto? [s/n] '))).lower().strip() == 's':
        alterarNomeProduto = True
    alterarPrecoProduto: bool = False
    if (str(input('Deseja alterar o preço do produto? [s/n] '))).lower().strip() == 's':
        alterarPrecoProduto = True
    alterarIDComprador: bool = False
    if (str(input('Deseja alterar o ID do comprador? [s/n] '))).lower().strip() == 's':
        alterarIDComprador = True
    
    if alterarNomeProduto:
        while True:
            nomeNovo: str = str(input('Qual é o novo nome do produto vendido? '))
            query = f'UPDATE produtos SET nome = "{nomeNovo}" WHERE ID = {ID_produto}'
            try:
                cursor.execute(query)
                conexao.commit()
            except Exception as e:
                print(f'Erro ao editar nome do produto: {e}')
                print('Tente novamente')
                continue
            else:
                print('O nome do produto vendido foi alterado com sucesso!')
                break
    if alterarPrecoProduto:
        while True:
            precoNovo: float = float(input('Qual é o novo preço do produto vendido? '))
            query = f'UPDATE produtos SET preco = {precoNovo} WHERE ID = {ID_produto}'
            try:
                cursor.execute(query)
                conexao.commit()
            except Exception as e:
                print(f'Erro ao editar preço do produto: {e}')
                print('Tente novamente')
                continue
            else:
                print('O preço do produto vendido foi alterado com sucesso!')
                break
    if alterarIDComprador:
        while True:
            IDCompradorNovo: int = int(input('Qual é o novo ID do comprador? '))
            query = f'UPDATE produtos SET ID_cliente = {IDCompradorNovo} WHERE ID = {ID_produto}'
            try:
                cursor.execute(query)
                conexao.commit()
            except Exception as e:
                print(f'Erro ao editar ID do comprador: {e}')
                print('Tente novamente')
                continue
            else:
                print('O ID do comprador do produto vendido foi alterado com sucesso!')
                break

# Delete
def deleteCliente(cursor, conexao):
    nome_cliente = str(input('Qual o nome do cliente que será retirado da base de dados? '))
    query1 = f'SELECT * FROM clientes WHERE nome = "{nome_cliente}";'
    cursor.execute(query1)
    resultado = cursor.fetchall()
    print('Listando clientes com este nome...')
    contador = 0
    for c in range(0, len(resultado), 1):
        print(f'ID: {resultado[c][0]} | Nome: {resultado[c][1]}')
        contador = contador + 1
    if contador == 0:
        print('Não existem clientes com este nome!')
        return
    while True:
        ID_cliente = int(input('Qual o ID do cliente que você quer deletar? '))
        query_deletarProdutosDoCliente = f'DELETE FROM produtos WHERE ID_cliente = {ID_cliente};'
        query_deletarCliente = f'DELETE FROM clientes WHERE ID = {ID_cliente};'
        certeza = str(input('Tem certeza que deseja deletar este cliente? [s/n] ')).lower().strip()
        
        if certeza == 's':
            try:
                cursor.execute(query_deletarProdutosDoCliente)
                conexao.commit()
                cursor.execute(query_deletarCliente)
                conexao.commit()
            except Exception as e:
                print(f'Erro ao deletar cliente: {e}')
                print('Tente novamente.')
                continue
            else:
                print('Cliente deletado com sucesso!')
                break
        else:
            continue

def deleteProdutos(cursor, conexao):
    nome_produto = str(input('Qual o nome do produto que você deseja deletar? '))
    query1 = f'SELECT * FROM produtos WHERE nome = "{nome_produto}";'
    cursor.execute(query1)
    resultado = cursor.fetchall()
    print('Listando produtos com este nome...')
    contador = 0
    for c in range(0, len(resultado), 1):
        print(f'ID: {resultado[c][0]} | Nome: {resultado[c][1]} | Preço: {resultado[c][2]} | ID do comprador: {resultado[c][3]}')
        contador = contador + 1
    if contador == 0:
        print('Não existem produtos com este nome!')
        return
    while True:
        ID_produto: int = int(input('Qual o ID do produto vendido que você deseja deletar? '))
        query = f'DELETE FROM produtos WHERE ID = {ID_produto}'
        certeza = str(input('Tem certeza que deseja deletar esse produto? [s/n] ')).lower().strip()
        if certeza == 's':
            try:
                cursor.execute(query)
                conexao.commit()
            except Exception as e:
                print(f'Erro ao deletar o produto vendido: {e}')
                print('Tente novamente.')
                continue
            else:
                print('O produto vendido foi deletado com sucesso!')
                break
        else:
            continue