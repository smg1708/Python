class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def somar(self):
        return self.num1 + self.num2
        

num1 = int(input())
num2 = int(input())
calc = Calculadora(num1, num2)
resultado = calc.somar()
print(resultado)