while True:
        try:
            numero = int(input("Digite o número: "))
            break
        except:
            print("Número inválido. Informe somente números.")
i = 1
while i <= 10:
        print(numero, "X", i, "é =", numero * i)
        i = i + 1