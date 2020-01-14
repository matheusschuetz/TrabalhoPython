#flask_mysqldb
import MySQLdb

#Listar todos os endereços
def listar_todos(c):
    c.execute('SELECT * FROM endereco')
    enderecos = c.fetchall()
    for e in enderecos:
        print(e)

#Buscar um endereco pelo ID
def buscar_por_id(c,id):
    c.execute(f'SELECT * FROM endereco WHERE ID = {id}')
    endereco = c.fetchone()
    print(endereco)

#Buscar um endereco pelo numero
def buscar_por_numero(c,numero):
    c.execute(f"SELECT * FROM endereco WHERE Numero = '{numero}'")
    endereco = c.fetchone()
    print(endereco)

#salvar endereco
def salvar(cn, cr, logradouro, numero, complemento, bairro, cidade):
    cr.execute(f"INSERT INTO endereco (Logradouro, Numero, Complemento, Bairro, Cidade) VALUES('{logradouro}', '{numero}', '{complemento}', '{bairro}', '{cidade}')")
    cn.commit()




#Alterar Endereco
def alterar(cn, cr, id, logradouro, numero, complemento, bairro, cidade):
    cr.execute(f"UPDATE endereco SET Logradouro = '{logradouro}',Numero = '{numero}',Complemento = '{complemento}',Bairro = '{bairro}' WHERE ID = {id} ")
    cn.commit()




#Deletar pessoa
def deletar(cn, cr, id):
    cr.execute(f'DELETE FROM endereco WHERE ID = {id}')
    cn.commit()

conexao = MySQLdb.connect(host= '127.0.0.1', database='aula1', user='root')
cursor=conexao.cursor()
# listar_todos(cursor)
# buscar_por_id(cursor, 1)
# buscar_por_numero(cursor, '12312')
# salvar(conexao, cursor, 'Ruinha', '321', 'Apartamento', 'Garcia', 'Estador Unidos')
# alterar(conexao, cursor, 1, 'General Osorio', '288', 'Casa', 'Velha', 'Blumenau')
# deletar(conexao,cursor,2)