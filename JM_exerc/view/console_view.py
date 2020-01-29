import sys
sys.path.append('C:/Users/900152/Documents/Dados/TrabalhoPython/JM_exerc')
from model.Back_model import BackEnd
from controller.Back_controller import BackController


s = BackEnd(0, 'Teste','Algo ai', 'beta')




contr=  BackController()
save_id = contr.save(s)
