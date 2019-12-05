# Aula 19 - 04-12-2019
# Lista com for e metodos
from random import randint
arquivo = open('19-Aula19/exercicios/nomes.txt','r')
nomes1 = []
for i in arquivo:
    i = i.strip()
    nomes1.append(i)
arquivo.close()

nomes = []
for i in range(500):
    sorteio = nomes1[randint(0,len(nomes1)-1)]
    while sorteio in nomes:
        sorteio = nomes1[randint(0,len(nomes1)-1)]
    nomes.append(sorteio)



idade = []
for i in nomes:
    idade.append(randint(16,50))

sexo = []
for i in nomes:
    sex = randint(0,1)
    if sex == 1:
        sexo.append('f')
    else:
        sexo.append('m')

email = []
arquivo = open('19-Aula19/exercicios/emails.txt','r')
for i in arquivo:
    i = i.strip()
    email.append(i)
arquivo.close()

email_sort = []

for i in nomes:
    sorteio = email[randint(0,len(email)-1)]
    while sorteio in email_sort:
        sorteio = email[randint(0,len(email)-1)]
    email_sort.append(sorteio)

fone = []

ddd = list(range(11,59))
for i in nomes:
    
    sorteio=randint(0,len(ddd)-1)
    telefone = f'0{ddd[sorteio]}9{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}'
    fone.append(telefone)

cab = ['nome','idade','sexo','email','telefone']

arquivos = open('19-Aula19/exercicios/cadastro3.txt','a')
j=len(nomes)
for i in range(j):
    texto = f'{i+1};{nomes[i]};{idade[i]};{sexo[i]};{email_sort[i]};{fone[i]}\n'
    arquivos.write(texto)
arquivos.close()

