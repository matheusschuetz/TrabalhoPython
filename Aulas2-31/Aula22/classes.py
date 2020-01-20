# 1) O que uma pessoa Tem? Quais as caracteristicas? 
###### Atributos --- variáveis
# nome
# idade
# telefone
# sexo

# 2) O que uma pessoa faz? 
###### Métodos --- (função/procedimento)
# respira
# dorme
# corre
# bebe
# come
# multiplica ###

# 3) Como a pessoa está agora? 
###### Atributos de estado ---- Variáveis
# divida
# cansada
# viva
# fome
# sede


class Pessoa:
    '''
    Essa classe é uma demonstração para aula
    '''
    def __init__(self,nome1, idade1, telefone1, sexo1):
        '''
        O__init__é o motor que irá iniciar as variáveis da classe
        o self é o que irá conectar toda a classe
        '''
        #Atributos##########
        self.nome = nome1
        self.idade = idade1
        self.telefone = telefone1
        self.sexo = sexo1
        ####################
        self.divida = None
        self.cansada = 'não'
        self.viva = True
        self.fome = 'não'
        self.sede = 'não'
    ### Métodos
    def respira (self, respirar):
        if self.viva == True:
            if respirar == True:
                self.viva = True
            else:
                self.viva = False
    def corre (self, distancia):
        if self.viva:
            if distancia >= 50 and distancia < 100:
                self.cansada = 'pouco'
                self.sede = 'pouco'
                self.fome = 'pouco'
            elif distancia >= 100 and distancia < 200:
                self.cansada = 'medio'
                self.sede = 'medio'
                self.fome = 'medio'
            elif distancia >=200:
                self.cansada = 'muito'
                self.sede = 'muito'
                self.fome = 'muito'
        
    def dorme (self):
        if self.viva:
            self.cansada = 'não'
            self.bebe()
            self.come()
        
    def bebe (self):
        if self.viva:
            self.sede = 'não'
    def come (self):
        if self.viva:
            self.fome = 'não'

    def multiplica (self):
         if self.viva:
            self.multiplica = 'não'
        

p = Pessoa('Antonio', 18, '479966995', 'm')
p.respira(True)
p.corre(300)
p.come()
p.dorme()
p.bebe()
print(f'Meu nome é {p.nome}')
print(f'Esta vivo? {p.viva}')
print(f'Está com fome? {p.fome}')
print(f' Está com sede? {p.sede}')
print(f'Esta cansado? {p.cansada}')