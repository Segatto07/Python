try:
    num1 = float(input("Digite o primero número: "))
    num2 = float(input("Digite o segundo número: "))
    
    resultado = num1 / num2 
    print("O resultado de", num1, "/", num2, "é =", resultado)

except ValueError:
    print("Número informado inválido. Por favor, digite apenas números inteiros")
except ZeroDivisionError:
    print("Erro! Não é possivel dividir um número por zero (0)")