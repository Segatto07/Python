try:
    valor  = float(input("Insira o valor: $").replace(",","."))
    if valor >500:
        print("Parabéns! Você ganhou 15% de desconto!")
    elif valor >100 and valor <=500:
        print("Parabéns! Você ganhou 10% de desconto!")
    else:
        print("Sem desconto. Gaste mais!")

except:
    print("valor inválido.")        
               