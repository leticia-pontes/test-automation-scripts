import math

def gerar_numeros_primos(n_elementos):
    
    numeros = []

    if not isinstance(n_elementos, int):
        return 'Erro: O argumento deve ser um número inteiro'

    if n_elementos <= 0:
        return 'Erro: O número deve ser maior que zero'
    
    for n in range(2, n_elementos + 1):
        if is_primo(n):
            numeros.append(n)

    return numeros

def is_primo(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

lista = gerar_numeros_primos(17)

print(lista)