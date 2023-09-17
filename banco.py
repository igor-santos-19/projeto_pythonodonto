import mysql.connector

conexao = mysql.connector.connect(host='localhost', database='odonto', user='root', password='')

# conexao com o banco com cursor
def conexaoBanco():
    if conexao.is_connected():
        db_info = conexao.get_server_info()
        print('Conectado ao servidor com sucesso', db_info)
        cursor = conexao.cursor()
        cursor .execute("select database();")
        linha = cursor.fetchone()
        print('Conectado ao banco de dados', linha)

# tras dados da tabela
    cursor.execute('select * from pessoa;')
    retornoConsulta = cursor.fetchone()
    for retornoConsulta in cursor:
        print(retornoConsulta)

# fecha conexao com o banco
    if conexao.is_connected():
        cursor.close()
        conexao.close()
        print("Conexão ao MariaDB foi fechada")
        
conexaoBanco()