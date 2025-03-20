def elementos_comuns(lista1, lista2):
    # Converte as listas de strings em conjuntos de inteiros
    set1 = set(map(int, lista1.split()))
    set2 = set(map(int, lista2.split()))
    # Retorna a lista dos elementos comuns
    return list(set1.intersection(set2))
# Entrada do usuário
lista1 = input().strip()
lista2 = input().strip()
# Verifica se ambas as listas contêm apenas números inteiros antes da conversão
if all(item.isdigit() for item in lista1.split()) and all(item.isdigit() for item in lista2.split()):
    comuns = elementos_comuns(lista1, lista2)
    print(f"Elementos comuns às duas listas: {comuns}")
else:
    print("Entrada inválida.")
