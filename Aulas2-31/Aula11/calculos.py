
def calculo_iss(valor):
    valor_iss = valor * 0.05
    return valor_iss


def calc_mes(valor, rent):
    val_mes = valor * rent
    return val_mes

def calc_ano(valor, rent):
    montante = (valor*(1+rent)**12)-valor 
    return montante

def calculo_rentabilidade(investido,rentabilidade):
    lista = []
    for i in range(1,13):
        juros = (investido * rentabilidade)
        investido = juros + investido
        lista.append(investido)
    return lista


