'''
dias_de_cada_mes = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

qual_mes = int(input('Digite aqui o mês que você quer:'))

print(f'O Mês {qual_mes} tem {dias_de_cada_mes[qual_mes]}')
print(sum(list(dias_de_cada_mes.values())[qual_mes-1:]))

total = 0
for mes in range(qual_mes,12+1):
    total += dias_de_cada_mes[mes]
print('modo estruturado')
print('total de dias até o final do ano', total)
###################################################################################################################
#For no dicionario
for chave in dias_de_cada_mes:
    print('tenho uma chave nessa linha', chave)
    print('se tenho uma chave, tenho o valor', dias_de_cada_mes[chave])
###################################################################################################################
#Chave e valor no dicionario 
for chave, valor in dias_de_cada_mes.items():
    print('Para a chave',chave, 'o valor', valor)
'''
###################################################################################################################
#for em tupla
tupla = ('Texto', 42, 5.01, int, str, list)
#tupla mais simples
tupla = ('Text', 'texto de novo', 'textei', 'textamento')
for isto in tupla:
    print(type(isto))
    print(isto)

###################################################################################################################