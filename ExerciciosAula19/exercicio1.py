# Aula 19 - 04-12-2019
# Lista com for e metodos

# 1 - Com a seguinte lista imprima na tela (unsado a indexação e f-string) 

cadastroHBSIS = ['nome',   ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
                'telefone',['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
                'email',   ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
                'idade',   ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]
                ]


# nome  Alex telefone: 4799991
# idade Carlos é 15 anos
# email de Mateus é d@d.com
print(f'''{cadastroHBSIS[0]} {cadastroHBSIS[1][0]} 
{cadastroHBSIS[6]} {cadastroHBSIS[1][4]} é {cadastroHBSIS[7][4]} anos
{cadastroHBSIS[4]} de {cadastroHBSIS[1][3]} é {cadastroHBSIS[5][3]}''')
# 2 - usando o for, imprima todos nomes um abaixo do outro
for i in range(7):
    lista_nomes = cadastroHBSIS[1][i]
    print(lista_nomes)

# 3 - Usando a indexação faça uma lista com 3 bibliotecas contendo os dados do Mateus, Paulo e João
#  contendo como chaves: nome, email, idade, telefone (nesta  sequencia)
lista = []
for i in range(3):
    dicionario = {}
    lista.append(dicionario)
for j in range(0,7,2):
    dados = cadastroHBSIS[j + 1][1:6:2]
    contador = 0
    for dado in dados:
        lista[contador][cadastroHBSIS[j]] = dado
        contador = contador + 1
            
print(lista)

