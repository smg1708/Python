texto = input("")
VOGAIS = "AEIOUaeiou"
contador = sum(1 for letra in texto if letra in VOGAIS)
print(f"O número de vogais na string '{texto}' é: {contador}")
