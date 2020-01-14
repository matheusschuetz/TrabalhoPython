#flask_mysqldb
import MySQLdb


def listar_todos(c):
    c.execute('SELECT * FROM pessoas')
    pessoas = c.fetchall()
    for p in pessoas:
        print(p)

def buscar_por_id(c,id):
    c.execute(f'SELECT * FROM pessoa WHERE ID = {id}')
    pessoa = c.fetchone()
    print(pessoa)

def buscar_por_sobrenome(c,sobrenome):
    c.execute(f"SELECT * FROM pessoa WHERE Sobrenome = '{sobrenome}'")
    pessoa = c.fetchone()
    print(pessoa)

conexao = MySQLdb.connect(host= '127.0.0.1', database='aula1', user='root')
cursor=conexao.cursor()
# listar_todos(cursor)
# buscar_por_id(cursor, 8)
buscar_por_sobrenome(cursor, 'Schuetz')