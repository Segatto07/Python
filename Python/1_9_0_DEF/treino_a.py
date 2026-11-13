def somar(num1, num2):
    soma = num1 + num2
    return soma

start = True
while start:
    try:
        num1 = float(input("Digite o primeiro número: ").replace(",", "."))
        start = False
    except:
        print(" Valor inválido, Por favor, digite apenas números")
start = True
while start:
    try:
        num2 = float(input("Digite o segundo número: ").replace(",", "."))
        start = False
    except:
        print(" Valor inválido, Por favor, digite apenas números")       

resultado = somar(num1, num2)
print("O resultado da soma é =", resultado)