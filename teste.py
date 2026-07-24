# from tkinter import messagebox, simpledialog, Tk

# def Casa_inteligente():
#     # Esconde a janela principal do Tkinter (necessário ao usar apenas caixas de diálogo)
#     root = Tk()
#     root.withdraw()

#     menu_texto = (
#         "--- MENU DA TV ---\n"
#         "1. LIGAR TV\n"
#         "2. DESLIGAR TV\n"
#         "3. MUDAR CANAL\n"
#         "4. LIGAR SOM\n"
#         "5. DESLIGAR SOM\n\n"
#         "Digite o número da sua escolha:"
#     )

#     # Abre a caixa para o usuário digitar a opção
#     entrada = simpledialog.askstring("Casa_inteligente", menu_texto)

#     # Se o usuário clicar em "Cancelar" ou fechar a janela
#     if entrada is None:
#         return

#     try:
#         valor = int(entrada)
        
#         if valor == 1:
#             messagebox.showinfo("Sucesso", "Você escolheu: LIGAR TV")
#         elif valor == 2:
#             messagebox.showinfo("Sucesso", "Você escolheu: DESLIGAR TV")
#         elif valor == 3:
#             messagebox.showinfo("Sucesso", "Você escolheu: MUDAR CANAL")
#         elif valor == 4:
#             messagebox.showinfo("Sucesso", "Você escolheu: LIGAR SOM")
#         elif valor == 5:
#             messagebox.showinfo("Sucesso", "Você escolheu: DESLIGAR SOM")
#         else:
#             messagebox.showwarning("Aviso", "Opção inválida. Escolha de 1 a 5.")

    


#     except ValueError:
#         messagebox.showerror("Erro", "Por favor, digite apenas números inteiros.")

# Casa_inteligente()