# Eu que fiz

def somar1(a, b, c, d, e ):
    return a + b + c + d + e

def somar2(a, b, c, d, e ):
    return a + b + c + d + e

def somar3(a, b, c, d):
    return a + b + c + d


def exibir_resultado1(a, b, c, d, e, funcao):
    resultado = funcao(a, b, c, d, e)
    print(f"A soma dos elementos da tupla é: {resultado}")


def exibir_resultado2(a, b, c, d, e, funcao):
    resultado = funcao(a, b, c, d, e)
    print(f"A soma dos elementos da tupla é: {resultado}")


def exibir_resultado3(a, b, c, d, funcao):
    resultado = funcao(a, b, c, d)
    print(f"A soma dos elementos da tupla é: {resultado}")

exibir_resultado1(2, 5, 6, 7, 9, somar1)
exibir_resultado2(9, 8, 7, 6, 5, somar2)
exibir_resultado3(50, 50, 50, 50, somar3)

# jeito correto pelo gpt

def somar(tupla):
    return sum(tupla)

def exibir_resultado(tupla, funcao):
    resultado = funcao(tupla)
    print(f"A soma dos elementos da tupla é: {resultado}")

# Entrada do usuário convertida para tupla de inteiros
entrada = input().strip()  # Lê a entrada e remove espaços extras
numeros = tuple(map(int, entrada.split()))  # Converte a entrada para uma tupla de inteiros

# Exibir o resultado
exibir_resultado(numeros, somar)