#Resolução do exercicio do git

from calculo_imposto import calculo_inss, calculo_irrf


print('='*50, '\n')

salario = float( input('Digite seu salario:') )

inss = calculo_inss(salario)
irrf = calculo_irrf(salario, inss)

salario_liquido = salario - inss - irrf
print(f'Inss: {inss}')
print(f'Irrf: {irrf}')
print(f'Seu salário liquido é {salario_liquido}')

print( '\n'*2,'='*50)