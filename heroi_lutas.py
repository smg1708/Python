heroi = input("Qual o nome do heroi? ")
print(f"Classes disponíveis: MAGO, GUERREIRO, MONGE e NINJA")

while True:
    classe = input("Qual a classe do herói? ").strip().lower()

    if classe == "mago":
        print(f"Classe mago escolhida com sucesso")
        break
    elif classe == "guerreiro":
        print(f"Classe guerreiro escolhida com sucesso")
        break
    elif classe == "monge":
        print(f"Classe monge escolhida com sucesso")
        break
    elif classe == "ninja":
        print(f"Classe ninja escolhida com sucesso")
        break
    else:
        print("Classe não liberada ou incorreta. Tente novamente.")

print("Carregando...")

# Definição dos ataques
ataques = {
    "mago": "magia",
    "guerreiro": "espada",
    "monge": "artes marciais",
    "ninja": "shuriken"
}

print(f"O {heroi} entrou em combate com um inimigo")
print(f"Você é um {classe} e atacou com seu {ataques[classe]}")
