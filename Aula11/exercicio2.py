from calculos import  calculo_rentabilidade


print('\nRentabilidade anual de um investimento:')
investido = float(input('Insira o valor que você investiu:\n'))

rentabilidade = (0.018)

lista = calculo_rentabilidade(investido, rentabilidade)
print(lista)

print(f'Primeiro mês: {lista[0]:.2f}Segundo mês:{lista[1]:.2f}Terceiro mês:{lista[2]:.2f}Quarto mês:{lista[3]:.2f}Quinto mês:{lista[4]:.2f}Sexto mês:{lista[5]:.2f}Sétimo mês:{lista[6]:.2f}Oitavo mês:{lista[7]:.2f}Nono mês:{lista[8]:.2f}Décimo mês:{lista[9]:.2f}Décimo primeiro mês:{lista[10]:.2f}Décimo segundo mês:{lista[11]:.2f}')



    


