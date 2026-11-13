import mod_inputs
#Se você quiser só uma especifica coloque from "mod_inputs" import str
import mod_sair

# a mensagem personalizada fica dentro da aspas do inp_str(aqui)
start = True
while start:

    nome = mod_inputs.inp_str("Digite seu nome: ")

    idade = mod_inputs.inp_int("Digite sua idade em anos: ")

    peso = mod_inputs.inp_float("Digite seu peso em kg: ")

    print("\n========NOME=========")
    print("Seu nome é ", nome, "\n")
    print("========IDADE========")
    print("Sua idade é ", idade, "anos\n")
    print("========PESO========\n")
    print("Seu peso é ", peso, "Kg")

    start = mod_sair.finalizar()