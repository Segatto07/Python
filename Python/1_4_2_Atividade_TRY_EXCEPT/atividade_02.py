try: 
    num1 = float(input("Informe o primeiro número: ").replace(",", "."))
    num2 = float(input("Informe o segundo número: ").replace(",", "."))

    resultado = num1 + num2

    print("O resuldado de", num1, "+", num2, "é =", resultado),str(resultado).replace(".", ",")

except ValueError:
    print("Valor incorreto. Por favor, coloque somente números!")
