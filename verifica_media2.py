aluno = input("Qual o nome do aluno? ")
media_final = 6
b1 = float(input("Qual a nota do aluno no 1° bimestre: "))
b2 = float(input("Qual a nota do aluno no 2° bimestre: "))
b3 = float(input("Qual a nota do aluno no 3° bimestre: "))
b4 = float(input("Qual a nota do aluno no 4° bimestre: "))
media = b1 + b2 + b3 + b4
aritmetica = media / 4
print(f"As notas de {aluno}, sendo feita a media das respectivas notas {b1, b2, b3, b4} é igual a {aritmetica}")
print(f"Carregando.....")

if aritmetica < media_final:
        print(f"{aluno} foi reprovado")
else:
        print(f"{aluno} foi aprovado")





