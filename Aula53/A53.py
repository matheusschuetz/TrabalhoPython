from Aula53.Dao.Pessoa_dao import PessoaDao

dao = PessoaDao()
pessoas = dao.list_all()
print(pessoas)
for p in pessoas:
    print(p)

