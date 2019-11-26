#Resolução que fiz na frente

def calcular(num1,num2):
    res = num1 + num2
    print(f'O resultado entre {num1} + {num2} é {res}')
#Os inputs poderiam ser colocados dentro do Def, desde que fosse chamada a função como esta no final, porem sem precisar do x e y, ja que são
#   criadas la dentro


x = int(input('Digite o primeiro número:'))
y = int(input('Digite um segundo número:'))


#As variáveis são substituidas em ordem, portanto x se torna num1 e y num2
#A função precisa ser chamada para funcionar
#Para printar fora da função, basta apenas colocar antes do "calcular()", res = calcular(x,y) e o print logo na linha de baixo
calcular(x,y)                                                            #Ou pode colocar qualquer outra variavel, pois se torna uma nova 

#True = 1 
#False = 2

#1 + 1
print(True + True)
#0 + 0
print(False + False)
#0 + 1
print(False + True)