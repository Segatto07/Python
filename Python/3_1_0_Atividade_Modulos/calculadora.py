import operacoes as oper
import mod_inputs
import mod_sair

num1 = mod_inputs.inp_float("Digite o primeiro número: ")
num2 = mod_inputs.inp_float("Digite o segundo número: ")

print("somar: ", oper.somar(num1, num2))
print("subtrair", oper.subtrair(num1, num2))
print("multiplicação", oper.multiplicar(num1,num2))

if num2 != 0:
    print("Divisão: ", oper.divisao(num1, num2))
else:
    print("não é possivel dividir um número por zero!")

mod_sair.finalizar()



