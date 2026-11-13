try:
    valor_produto = float(input("Informe o valor do produto: ").replace(",", "."))
    valor_desconto = int(input("informe o desconto: "))

    resultado = valor_produto * (1 - (valor_desconto / 100))

    print("O valor total é = $", resultado),str(resultado).replace(".",",")

except:
    print("infome o valor correto")