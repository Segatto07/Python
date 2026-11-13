numero = int(input("Tabuada de qual número?: "))
    
for numero in range(1,11):
    print("Tabuada do numero", numero)
    for i in range(1, 11):
        print(f"{numero} x {1} = {numero * i}")


