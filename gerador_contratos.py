from customtkinter import *
import customtkinter as ctk
from PIL import Image, ImageEnhance, ImageTk
from customtkinter import CTkImage


# ===> Setando a aparencia <===
app = CTk()
app.resizable(False, False) # impede o redimensionamento
ctk.set_appearance_mode('system') # define a aparencia de acordo com o do Windows

# ==> Definindo os parâmetros <==
largura_app = 500 # define a largura do aplicativo
altura_app = 500 # define a altura do aplicativo
largura_da_janela = app.winfo_screenwidth() # determina a largura da tela do monitor
altura_da_janela = app.winfo_screenheight() # determina a altura da tela do monitor
x = int((largura_da_janela - largura_app)/2) # calcula a centralizacao no eixo x (horizontalmente)
y = int((altura_da_janela - altura_app)/2) # calcula a centralizacao no eixo y (verticalmente)

# ==> Definindo geometria e posicao do APP ao abrir <==
app.geometry(f'{largura_app}x{altura_app}+{x}+{y}') # define a posicao para que o app inicialize centralizado na tela


# ===> Definição do layout <===

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ===> Criacao dos frames <===
box_registro = CTkFrame(app,
                        width=200,
                        height=100,
                        corner_radius=32,
                        border_color='black',
                        border_width=4,
                        fg_color='#1e1e1e')
box_registro.place(relx=0.5, rely=0.8, anchor='center')

# => Botões de login <=
btn_login = CTkButton(box_registro,
                hover_color='#dc9f46',
                border_width=1,
                border_color='black',
                text='Faça login',
                bg_color='transparent',)
btn_login.place(relx=0.5, rely=0.3, anchor='center')


# => Botões de registro <=
btn_registro = CTkButton(box_registro,
                hover_color='#dc9f46',
                border_width=1,
                border_color='black',
                bg_color='transparent',
                text='Registre-se')
btn_registro.place(relx=0.5, rely=0.7, anchor='center')


# ===> Botao de definir o tema <===
# ==> Funcao de definir o tema <==
def alternar_tema():
    if switch_tema.get() == 1:
        ctk.set_appearance_mode('dark') # ao clicar muda o tema para escuro
        switch_tema.configure(text='Modo escuro') # define o texto que aparece no botao switch
    else:
        ctk.set_appearance_mode('light') # ao clicar muda o tema para claro
        switch_tema.configure(text='Modo claro') # define o texto que aparece no botao switch

# => Definindo a aparencia do botao switch <=
switch_tema = CTkSwitch(
    app, 
    command=alternar_tema,
    fg_color='#2b2b2b', # deixa o fundo do botao transparente
    progress_color='#1f6aa5', # define a cor da parte dinamica do botao
    button_color='lightgray', # define a cor do botaso redondo
    text='Modo escuro', # texto que aparece ao abrir o APP
    border_color='white', # define a cor da borda
    border_width=1 # define a espessura da borda
    ) 

# => Posicao do botao switch <=
switch_tema.place(relx=0.98, rely=0.02, anchor='ne')













app.mainloop()