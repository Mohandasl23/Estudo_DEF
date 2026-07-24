import tkinter as tk

# 1. CRIAR A JANELA PRINCIPAL
janela = tk.Tk()
janela.title("Minha Primeira Interface")
janela.geometry("400x300") # Largura x Altura em pixels

# 2. ADICIONAR ELEMENTOS (WIDGETS) E ORGANIZAR
rotulo = tk.Label(janela, text="Bem-vindo à Cafeteria!", font=("Arial", 14))
rotulo.pack(pady=10) # Põe o texto na tela com um espacinho vertical

botao = tk.Button(janela, text="Clique Aqui", command=lambda: print("Botão clicado!"))
botao.pack(pady=10)

# 3. MANTER A JANELA ABERTA (LOOP PRINCIPAL)
janela.mainloop()