from tkinter import messagebox, simpledialog, Tk

def cafeteria():
    # Esconde a janela principal do Tkinter (necessário ao usar apenas caixas de diálogo)
    root = Tk()
    root.withdraw()

    menu_texto = (
        "--- MENU DA CAFETERIA ---\n"
        "1. Café puro\n"
        "2. Café com leite\n"
        "3. Chocolate\n"
        "4. Chá\n"
        "5. Suco\n\n"
        "Digite o número da sua escolha:"
    )

    # Abre a caixa para o usuário digitar a opção
    entrada = simpledialog.askstring("Cafeteria", menu_texto)

    # Se o usuário clicar em "Cancelar" ou fechar a janela
    if entrada is None:
        return

    try:
        valor = int(entrada)
        
        if valor == 1:
            messagebox.showinfo("Sucesso", "Você escolheu: Café puro")
        elif valor == 2:
            messagebox.showinfo("Sucesso", "Você escolheu: Café com leite")
        elif valor == 3:
            messagebox.showinfo("Sucesso", "Você escolheu: Chocolate")
        elif valor == 4:
            messagebox.showinfo("Sucesso", "Você escolheu: Chá")
        elif valor == 5:
            messagebox.showinfo("Sucesso", "Você escolheu: Suco")
        else:
            messagebox.showwarning("Aviso", "Opção inválida. Escolha de 1 a 5.")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite apenas números inteiros.")

cafeteria()