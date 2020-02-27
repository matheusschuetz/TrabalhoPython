def Cyclic(k, lista):
    for _ in range(k):
        lista.insert(0, lista.pop())
    return lista
lista = [1,2,3,4,5,6]
a = Cyclic(2,lista)
print(a)
