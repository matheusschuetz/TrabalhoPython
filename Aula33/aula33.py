#=======Classes
#-----Importar biblioteca do MySQLdb
import MySQLdb
#-----configurar a conexão
conexao = MySQLdb.connect(host= '127.0.0.1', database='aula1', user='root')
#-----Salvar o cursor da conexão em variável
cursor = conexao.cursor()

#-----criação de uma lista que adiciona os dicionarios
lista_pessoas = []
#-----criação do comando SQL e passado para o cursor
comando_sql_select = "SELECT * FROM pessoa"
cursor.execute(comando_sql_select)

resultado = cursor.fetchall()
for p in resultado:
    #-----Criação do dicionario que representa o nome pessoa
    dicionario_pessoa = {'ID':0,'Nome':'','Sobrenome':'','Idade':0,'Endereco_ID':0}
    #-----Pega cada dicionario e atribui a uma posição
    dicionario_pessoa['ID'] = p[0]
    dicionario_pessoa['Nome'] = p[1]
    dicionario_pessoa['Sobrenome'] = p[2]
    dicionario_pessoa['Idade'] = p[3]
    dicionario_pessoa['Endereco_ID'] = p[4]
    #-----Adiciona cada dicionario na lista
    lista_pessoas.append(dicionario_pessoa)

#-----Cria um arquivo e salva cada dicionario dentro dele
with open('Aula33\pessoas.txt', 'a') as arquivo:
    for p in lista_pessoas:
        arquivo.write(f"{p['ID']};{p['Nome']};{p['Sobrenome']};{p['Idade']};{p['Endereco_ID']}\n")


