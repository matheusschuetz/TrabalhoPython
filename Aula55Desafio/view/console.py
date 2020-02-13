from Aula55.dao.autor_dao import AutorDao

dao = AutorDao()
lista = dao.list_all()
for a in lista:
    print(a)