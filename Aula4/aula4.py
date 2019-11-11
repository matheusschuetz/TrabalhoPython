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
    