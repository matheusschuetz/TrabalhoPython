# Crie um método que receba uma string como parâmetro
# Armazene o parêmetro recebido dentro de uma lista
# Retorne mensagem informando que o dado foi armazenado com sucesso

# Leia o nome de uma pessoa no console
# Realize a chamada do método enviando o nome da pessoa como argumento

def receber_string(string: str):
    lista = [string]
    print(f'A string {string} foi armazenada')
    return lista

a = input('Adicione um nome:\n')
receber_string(a)