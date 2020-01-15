from pessoa_db import listar_todos
from pessoa_convert import converter_pessoas_dicionario
from pessoa_exporta import exportar_txt

lpt = listar_todos()
lpd = converter_pessoas_dicionario(lpt)
exportar_txt(lpd)
