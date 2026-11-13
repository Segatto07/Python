try:
    nota1 = float(input("Informe sua 1º nota: ").replace(",","."))
    nota2 = float(input("Informe sua 1º nota: ").replace(",","."))
    nota3 = float(input("Informe sua 3º nota: ").replace(",","."))

    resultado = (nota1 + nota2 + nota3) / 3

    print("Sua média é", resultado),str(resultado).replace(".",",")

except:
    print("Nota incorreta. Por favor, informe somente números")
