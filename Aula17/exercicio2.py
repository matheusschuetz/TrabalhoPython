from random import randint
aleatorio = randint(1,100)


while True:
    numero = int(input('Digite o seu numero da sorte:'))
    if numero == aleatorio:
        print('Voce acertou, parabens!!')
        break
    elif numero < aleatorio:
        print('EEERRROOOOUUU seu número é menor que o sorteado')
    elif numero > aleatorio:
        print('EEERRROOOOUUU seu número é maior que o sorteado')
