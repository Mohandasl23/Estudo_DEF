def cafeteria():
    tipos = "1. cafe puro\n2. cafe com leite\n3. chocolate"
    print("--- MENU DA CAFETERIA ---")
    print(tipos)
    print("-------------------------")
    
    try:
        valor = int(input("Digite o numero da sua escolha: "))
        
        if valor == 1:
            print("\n-> Voce escolheu: cafe puro")
        elif valor == 2:
            print("\n-> Voce escolheu: cafe com leite")
        elif valor == 3:
            print("\n-> Voce escolheu: chocolate")
        else:
            print("\n-> Opcao invalida")
    except ValueError:
        print("\n-> Erro: Por favor, digite apenas numeros inteiros.")

cafeteria()
