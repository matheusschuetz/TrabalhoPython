#flask_mysqldb
import MySQLdb

#Listar todas as pessoas 
def listar_todos(c):
    c.execute('SELECT * FROM pessoas')
    pessoas = c.fetchall()
    for p in pessoas:
        print(p)

#Buscar uma pessoa pelo ID
def buscar_por_id(c,id):
    c.execute(f'SELECT * FROM pessoa WHERE ID = {id}')
    pessoa = c.fetchone()
    print(pessoa)

#Buscar uma pessoa pelo sobrenome
def buscar_por_sobrenome(c,sobrenome):
    c.execute(f"SELECT * FROM pessoa WHERE Sobrenome = '{sobrenome}'")
    pessoa = c.fetchone()
    print(pessoa)

#salvar pessoa
def salvar(cn, cr, nome, sobrenome, idade, endereco_id='NULL'):
    cr.execute(f"INSERT INTO pessoa (Nome, Sobrenome, Idade, Endereco_ID) VALUES('{nome}', '{sobrenome}', {idade}, {endereco_id})")
    cn.commit()




#Alterar Pessoa
def alterar(cn, cr, id, nome, sobrenome, idade, endereco_id='NULL' ):
    cr.execute(f"UPDATE pessoa SET Nome = '{nome}',Sobrenome = '{sobrenome}',Idade = {idade},Endereco_ID = {endereco_id} WHERE ID = {id} ")
    cn.commit()




#Deletar pessoa
def deletar(cn, cr, id):
    cr.execute(f'DELETE FROM pessoa WHERE ID = {id}')
    cn.commit()

conexao = MySQLdb.connect(host= '127.0.0.1', database='aula1', user='root')
cursor=conexao.cursor()
# listar_todos(cursor)
# buscar_por_id(cursor, 8)
# buscar_por_sobrenome(cursor, 'Schuetz')
# salvar(conexao, cursor,'João','Pedro', 12, 1)
# alterar(conexao, cursor, 9,'Adriano','Lucas', 12, 1)
# deletar(conexao,cursor,8)