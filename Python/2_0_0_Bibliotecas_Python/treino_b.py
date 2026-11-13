import math

def calculadora():
    try:
        num1 = int(input("Digite o primeiro número inteiro: "))
        num2 = int(input("Digite o segundo número inteiro: "))

        raiz = math.sqrt(num1)
        potencia = math.pow(num1, num2)
        
        print("\n--- RESULTADOS ---")
        print("Primeiro número:", num1)
        print("Segundo número:", num2)
        print("Raiz quadrada:", raiz)
        print("Potência:", potencia)

    except ValueError:
        print("Erro! Digite apenas números inteiros.")
        
    except Exception as erro:
        print("Ocorreu um erro:", erro)

calculadora()
