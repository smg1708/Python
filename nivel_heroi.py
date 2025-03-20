xp_heroi= 0
while True:
    xp_heroi = int(input("Qual o xp do heroi? "))
    if xp_heroi <= 1000:
            print("Se XP for menor do que 1.000 = Ferro")
            break
    if 1001 <= xp_heroi <= 2000:
        print("Se XP for entre 1.001 e 2.000 = Bronze")
        break
    if 2001 <= xp_heroi <= 5000:
        print("Se XP for entre 2.001 e 5.000 = Prata Ouro")
        break
    if 5001 <= xp_heroi <= 8000:
        print("Se XP for entre 5.001 e 8.000 = Platina Diamante")
        break
    if 8001 <= xp_heroi <= 9000:
        print("Se XP for entre 8.001 e 9.000 = Ascendente")
        break
    if 9001 <= xp_heroi <= 10000:
        print("Se XP for entre 9.001 e 10.000 = Imortal")
        break
    if 10001 <= xp_heroi:
        print("Se XP for maior ou igual a 10.001 = Radiante")
        break
