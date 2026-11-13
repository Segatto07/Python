try:
    num1 = float(input("digite o primeiro número: ").replace(",", "."))
except: 
    print("valor inválido para o primeiro número!")  

try:
    num2 = float(input("digite o segundo número: ").replace(",", "."))
except: 
    print("valor inválido para o segundo número!") 

try:
    print("digite uma das operações a seguir: \n ")

    print("Para adição digite +")

    print("para subtração digite -")

    print("Para divisão digite /")

    print("Para multiplicação digite * \n")


    operador = str(input("digite uma operação: "))
except:
    print("Operador inválido1")

match operador:
    case "+":
            resultado = num1 + num2
            print("O resultado de", num1, operador, num2, 'é =', resultado)
    case "-":
            resultado = num1 - num2 
            print("O resultado de", num1, operador, num2, 'é =', resultado)
    case "/":
            resultado = num1 / num2
            print("O resultado de", num1, operador, num2, 'é =', resultado)
    case "*":
            resultado = num1 * num2
            print("O resultado de", num1, operador, num2, 'é =', resultado)
    case _:
        print("Operador inválido")