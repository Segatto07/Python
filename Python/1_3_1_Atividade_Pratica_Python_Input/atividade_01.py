num1 = float(input("Digite o primeiro valor:").replace(",", "."))

num2 = float(input("Digite o segundo valor:").replace(",", "."))

resultado = num1 * num2

print("O valor da multiplicação de", num1, "X", num2, "é =",str(resultado).replace(".", ","))
