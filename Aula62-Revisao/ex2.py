def concatenacao(string1: str, string2: str) -> str:
    nova_string = string1 + string2
    return nova_string


a = input("Digite uma palavra:\n")
b = input("Digite mais uma:\n")
r = concatenacao(a, b)
print(f'A concatenação entre {a} e {b} é {r}')
