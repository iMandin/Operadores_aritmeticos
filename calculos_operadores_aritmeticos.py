#******************************************************************************
#Olá!
#Esse código foi feito por mim (Amanda Brito), como um pequeno projeto de calculos com operadores aritméticos.
#Note que adicionei diversos comentários para que seja de fácil entendimento para todos.
#Bons estudos! :)
#*******************************************************************************

import os

print('Deseja fazer uma conta?') #Imprimindo mensagem inicial
def main(): #Definindo função
    a = input("Digite o primeiro numero: ") #Primeira entrada de usuario
    b = input("Digite o segundo numero: ") #Segunda entrada de usuario
    op = input("Escolha o operador (+-*/): ") #Terceira entrada de usuario

    command = a + op + b #Solicitação de calculo
    print(command) #Imprime a conta na tela 
    res = eval(command) #Avalia valor de result
    print(res) #Imprime o valor na tela
    print('Até a próxima! :)')

main()
