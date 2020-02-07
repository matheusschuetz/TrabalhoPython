from Aula54.Dao.Pessoa_dao import PessoaDao

dao = PessoaDao()
for p in dao.list_all():
    print(p)


print('_'*50)
print(dao.buscar_por_id(6))
print('_'*50)

