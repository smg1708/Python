class Conversor:
    def __init__(self, celsius):
        self.celsius = celsius

    def celsius_para_fahrenheit(self):
        fahrenheit = ((self.celsius * 9/5) +32 )
        return fahrenheit
        
celsius = float(input())

convert = Conversor(celsius)
f = convert.celsius_para_fahrenheit()
print(f)