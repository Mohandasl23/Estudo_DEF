from tkinter import messagebox, simpledialog, Tk

def cafeteria():
    print("--- MENU DA CAFETERIA ---")
    print("1. cafe puro")
    print("2. cafe com leite")
    print("3. chocolate")
    print("4. cha")
    print("5. suco")
    print("-------------------------")
    
    try:
        valor = int(input("Digite o numero da sua escolha: "))
        
        if valor == 1:
            print("\n-> Voce escolheu: cafe puro")
        elif valor == 2:
            print("\n-> Voce escolheu: cafe com leite")
        elif valor == 3:
            print("\n-> Voce escolheu: chocolate")
        elif valor == 4:
            print("\n-> Voce escolheu: cha")
        elif valor == 5:
            print("\n-> Voce escolheu: suco")
        else:
            print("\n-> Opcao invalida")
    except ValueError:
        print("\n-> Erro: Por favor, digite apenas numeros inteiros.")

cafeteria()

