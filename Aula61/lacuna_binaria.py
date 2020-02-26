def return_gap(N):
    string = str(bin(N))
    corte = string[2:]
    lista = []
    for i in corte:
        lista.append(i)
    counter = 0
    lista_contadores = []
    for i in lista:
        if i != '1':
            counter = counter + 1
        elif i == '1':
            lista_contadores.append(counter)
            counter = 0
    return max(lista_contadores)

a = return_gap(1041)
print(a)
