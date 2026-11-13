resultado#receber o nome do usuário
nome = str(input("Digite seu nome completo: "))

#Receber a idade do usuário
idade = int(input("Digite sua idade: "))

#Receber o peso do usuário
peso = float(input("Informe seu peso em kg: ").replace(",","."))
# (replace) usa para trocar de um argumento para outro tipo virgula por ponto, ja que o visual na aceita virgula só ponto

#para chamar uam sbfunção precisa ser ponto nao virgula se nao, nao vai

#Visulizar o nome digiado 
 
print("O nome do usuário é: ", nome)
print("A idade do usuário é: ", idade, "anos")
print("o peso do usuário é: ",str(peso).replace(".", ","), "kg")

# Para fazer o ponto se tornar virgula la no peso, voce deve fazer uma Str junto com o raplace dentro da função print!




