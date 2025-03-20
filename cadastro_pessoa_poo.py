class Pessoa:
    def __init__(self, Nome, Idade):
        self.Nome = Nome
        self.Idade = Idade

    def __str__(self):
        return f"{', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"

Nome = input()
Idade = int(input())

p = Pessoa(Nome, Idade)
print(p)
