def multi(num1: float, num2: float, num3: float = 1.0) -> float:
    resultado = num1 * num2 * num3
    return resultado


a = float(input('Digite um float:\n'))
b = float(input('Digite outro float:\n'))
print(f'O resultado entre {a}, {b} é {multi(a, b)}')
a = float(input('Digite um float:\n'))
b = float(input('Digite outro float:\n'))
c = float(input('Digite mais um float:\n'))
print(f'O resultado entre {a}, {b}, {c} é {multi(a, b, c)}')
