def cyclic(k, lista_numero):
    for _ in range(k):
        lista_numero.insert(0, lista_numero.pop())
    return lista_numero


lista = [1, 2, 3, 4, 5, 6]
a = cyclic(2, lista)
print(a)
