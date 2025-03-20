while True:
    numeros = input("Escreva um numero ou sair: ")
    pares = []
       
    if numeros == "sair":
        print("saindo....")
        break
    
    try:
        numero = int(numeros)
        if numero % 2 == 0:
            pares.append(numero)
            print("esse numero e par")
        else:
            print("esse numero e impar")
    except ValueError:
        print("Escreva um numero inteiro")
