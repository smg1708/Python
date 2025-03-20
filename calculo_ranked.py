while True:
    vitorias = int(input("Quantas vitorias o jogador obteve? "))
    derrotas = int(input("Quantas derrotas o jogador obteve? "))
    saldo = vitorias - derrotas
    if saldo <= 10:
            nivel = "Ferro"
            break
    if 11 <= saldo <= 20:
        nivel = "Bronze" 
        break
    if 21 <= saldo <= 50:
        nivel = "Prata"
        break
    if 51 <= saldo <= 80:
        nivel = "Ouro"
        break
    if 81 <= saldo <= 90:
        nivel = "Diamante"
        break
    if 91 <= saldo <= 100:
        nivel = "Lendario"
        break
    if 101 <= saldo:
        nivel = "Imortal"
        break
print(f"O Herói tem de saldo de vitorias igual a {saldo} é está no nivel: {nivel}")