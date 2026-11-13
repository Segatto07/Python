import mod_inputs as inp
import operacoes as oper
import mod_sair as sair
import math

def calcula_imc(altura, peso):
    imc = peso / math.pow(altura, 2)
    return imc

def classificacao(imc, idade):
    if idade >= 20 and idade <= 60:
        if imc <= 18.5:
            print("Peso baixo")
        elif imc >= 18.5 and imc <= 24.99:
            print("Peso normal")
        elif imc >= 25 and imc <= 29.99:
            print("Sobrepeso")
        elif imc <= 30:
            print("Obesidade")
    else:
        print("Informação invàlida")
    
    

    

nome = inp.inp_str("Infome o nome do cliente: ")
idade = inp.inp_int("infome a idade: ")
peso = inp.inp_float("Informe o peso: ")
altura = inp.inp_float("informe a altura do cliente: ")
imc = calcula_imc(altura, peso)



print("Seu nome é: ", nome)
print("Você tem: ", idade, "anos")
print("Você pesa: ", peso, "kg")
print("Seu IMC é: ", imc )

classificacao(imc, idade)