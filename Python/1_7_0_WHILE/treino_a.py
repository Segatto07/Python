senha = 0

while senha != 1234:
    try:
       senha = int(input("Digite sua senha!"))
    except:
        print("Senha inválida. Por favor, digite apenas números!")
print("Senha digitada com sucesso! ")
