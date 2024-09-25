# Objetivo desse codigo e aprender e testar um pouco do Github Codespaces na prática.
# Faremos 3 manipulações básicas e testaremos os resultados. 
# Segue detalhamento dos 3 itens que criaremos:
# 1 - Vamos concatenar 2 strings recebidas via input.
# 2 - Realizaremos prints de uma string recebida via input, também receberemos a quantidade que deveremos printar o texto.
# 3 - Faremos operações matemáticas com 2 inteiros. A operaçao a ser executada e os inteiros serão recebidos via input.

import numpy as np

# Função relacionada ao item 1
def case1 ():
    string1 = input("Digite a primeira string: ")
    string2 = input("Digite a segunda string: ")

    print(string1 + " " + string2)

# Função relacionada ao item 2
def case2 ():
    string1 = input("Digite a string: ")
    qtd_prints = int(input("Digite a quantidade de prints da string: "))
    
    for x in np.arange(0, qtd_prints):
        print(string1)
    
# Função relacionada ao item 3
def case3 ():
    num1 = int(input("Insira o primeiro inteiro: "))
    num2 = int(input("Insira o segundo inteiro: "))
    operation = int(input(" 1 - Adição\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão\n Escolha a operação: "))
    match operation:
        case 1:
            result = num1 + num2
        case 2:
            result = num1 - num2
        case 3:
            result = num1 * num2
        case 4:
            result = num1 / num2

    print(result)

# função para verificar a opçao inserida
def user_option(option):
    match option:
        case 1:
            case1()
        case 2:
            case2()
        case 3:
            case3()
        case _:
            print("Escolha inválida")

# Solicitando opção para o usuário
try:
    option = int(input("1 - Concatena 2 strings.\n2 - Realiza print da sua string quantas vezes você definir.\n3 - Realiza operações matemáticas com 2 inteiros.\nEscolha uma funcionalidade: "))
    # Processando a escolha
    user_option(option)
except ValueError:
    print("Entrada inválida! Por favor, digite um número.")
 