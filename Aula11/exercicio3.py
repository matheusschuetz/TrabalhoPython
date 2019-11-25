# crie um programa de investimento
# solicitar valor a ser investido no tesouro selic
# calcular o valor total ate o vencimento do titulo

print('Programa de investimeto Selic:')

cotas = float(input('Digite o numero de cotas a serem compradas:'))
lista = []
taxa = 0.46 / 100
if cotas >= 0.01:
    valor = (10410 / cotas) 
    for i in range(1,7):
        juros = valor * (0.02 / 100) + taxa
        valor = juros + valor
        lista.append(valor)
else:
    print('Não aceitamos um valor tão baixo')
print(lista)