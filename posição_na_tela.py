import customtkinter as ctk

app = ctk.CTk()
app.title("App Centralizado")

# Defina o tamanho da janela
largura = 400
altura = 300

# Obtenha o tamanho da tela do monitor
largura_tela = app.winfo_screenwidth()
altura_tela = app.winfo_screenheight()

# Calcule a posição para centralizar
pos_x = int((largura_tela / 2) - (largura / 2))
pos_y = int((altura_tela / 2) - (altura / 2))

# Aplique a geometria
app.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

app.mainloop()
