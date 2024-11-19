from specificExpression import *

def menu():
    print("Bem-vindo ao Solucionador de Lógica Proposicional!")
    print("Escolha uma das opções abaixo:")
    print("1. Gerar tabela verdade")
    print("2. Resolver expressão lógica com valores específicos")
    print("3. Resolver demonstrações com regras de inferência")
    print("4. Sair")
    
    opcao = input("Digite o número da opção desejada: ")
    return opcao

choice = menu();


if choice == "1":
    pass;
    #input_expression = input("Digite a expressão lógica: ")
    #gerar_tabela_verdade(input_expression)

elif choice == "2":
    resolve_expression();
elif choice == "4":
    print("Até mais!")
    exit()

