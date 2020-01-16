from pessoa import Pessoa
from pessoa_db import PessoaDb
p = Pessoa()
p_db = PessoaDb()

lpc = p_db.listar_todos()
p.exportar_txt(lpc)

