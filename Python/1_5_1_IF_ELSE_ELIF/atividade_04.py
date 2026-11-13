try:
    temperatura = float(input("Insira a temperatura: ºC").replace(",", "."))

    if temperatura > 30:
        print("Meu Deus, está muito quente!")
    elif temperatura >15 and temperatura <=30:
        print("Perfeito, temperatua ambiente!")
    elif temperatura >0 and temperatura <15:
        print("Ai que frio!!!")

    else:
        print("Pega sua coberta, um chocolate quente, que ta congelando!!!")   

except:
    print("Valor inválido.")            