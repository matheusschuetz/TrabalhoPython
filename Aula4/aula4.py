idade = 25
numero = int(input('digite aqui seu numero:'))
valor = int(input('digite aqui outro valor:'))
print('seus numeros são:',numero, valor)

x = numero
y = valor

adicao = x + y
sub = x - y
multi = x * y
divi = x / y
print('soma:', adicao, 'subtração:', sub,'multiplicação', multi, 'divisão:', divi)

if numero > valor:
    print('seu maior número é:', numero)
else:
    print('seu maior número é:', valor)

#if simples é a validação de apenas uma condição
if idade < 18:
    print('Você é menor de idade')
#if com else, saco a condição validade pelo if não seja verdadeira, ele irá automaticamente validar o else
if idade < 18:
    print('Você é menor de idade')
else:
    print('Você é maior de idade')
#elif, caso o if não seja verdaeiro, o elif irá verificar mais uma condição, e caso ele também não seja verdadeiro, o Else será validado
if idade < 18:
    print('Você é menor de idade')
elif idade ==18:
    print('Você tem 18 anos')
else:
    print('Você é maior de idade')
#Em caso de variável boleana, não é necessário a validação(==True)
#Pois o IF ja valida se o conteúdo da variável é True, senão vai para o Else
