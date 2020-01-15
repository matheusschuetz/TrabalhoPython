import MySQLdb
def listar_todos():
    #-----configurar a conexão
    conexao = MySQLdb.connect(host= '127.0.0.1', database='aula1', user='root')
    #-----Salvar o cursor da conexão em variável
    cursor = conexao.cursor()
    #-----criação do comando SQL e passado para o cursor
    comando_sql_select = "SELECT * FROM pessoa"
    cursor.execute(comando_sql_select)
    resultado = cursor.fetchall()
    return resultado