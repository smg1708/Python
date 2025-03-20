def cont(texto):
    contador = {}
    for letra in texto:
        contador[letra] = contador.get(letra, 0) + 1
    return contador

entrada = input()
resultado = cont(entrada)
print(f"{resultado}")
        












# 
#     resultado = funcao(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z)
#     print(f"{resultado}")

# exibir_resultado(entrada,co)




#     saida = sum(1 for letra in entrada if letra == letra)
# print(saida)
# contar_caracteres = sum(1 for letra in entrada if letra == letra)# contador = entrada.count
# def contar_caracteres(string):
#     return
