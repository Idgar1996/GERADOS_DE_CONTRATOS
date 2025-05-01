import customtkinter as ctk
import smtplib
import random
from email.message import EmailMessage

# Configuração de e-mail remetente
EMAIL_REMETENTE = 'cudecamelooficial@gmail.com'
SENHA_REMETENTE = 'bbbg jjgw gfjr hbfy'

# Variável para armazenar o código gerado
codigo_verificacao = None

# Função para enviar e-mail
def enviar_codigo(email_destino):
    global codigo_verificacao
    codigo_verificacao = str(random.randint(100000, 999999))

    msg = EmailMessage()
    msg['Subject'] = 'Código de Recuperação de Senha'
    msg['From'] = EMAIL_REMETENTE
    msg['To'] = email_destino
    msg.set_content(f'Seu código de verificação é: {codigo_verificacao}')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_REMETENTE, SENHA_REMETENTE)
            smtp.send_message(msg)
            resultado.configure(text="Código enviado! Verifique seu e-mail.", text_color="green")
    except Exception as e:
        resultado.configure(text=f"Erro ao enviar: {e}", text_color="red")

# Função para verificar o código digitado
def verificar_codigo():
    if entry_codigo.get() == codigo_verificacao:
        resultado.configure(text="Código verificado! Insira nova senha.", text_color="green")
        entry_nova_senha.configure(state="normal")
        botao_redefinir.configure(state="normal")
    else:
        resultado.configure(text="Código incorreto!", text_color="red")

# Função para redefinir a senha
def redefinir_senha():
    nova = entry_nova_senha.get()
    if nova:
        resultado.configure(text="Senha redefinida com sucesso!", text_color="green")
        # Aqui você colocaria a lógica para salvar a nova senha
    else:
        resultado.configure(text="Insira uma nova senha.", text_color="red")

# ================= INTERFACE ===================
app = ctk.CTk()
app.geometry("400x500")
app.title("Recuperação de Senha")

ctk.CTkLabel(app, text="E-mail cadastrado:").pack(pady=(20, 5))
entry_email = ctk.CTkEntry(app, width=300)
entry_email.pack()

ctk.CTkButton(app, text="Enviar código", command=lambda: enviar_codigo(entry_email.get())).pack(pady=10)

ctk.CTkLabel(app, text="Digite o código recebido:").pack(pady=(20, 5))
entry_codigo = ctk.CTkEntry(app, width=150)
entry_codigo.pack()

ctk.CTkButton(app, text="Verificar código", command=verificar_codigo).pack(pady=10)

ctk.CTkLabel(app, text="Nova senha:").pack(pady=(20, 5))
entry_nova_senha = ctk.CTkEntry(app, width=300, show="*")
entry_nova_senha.pack()
entry_nova_senha.configure(state="disabled")

botao_redefinir = ctk.CTkButton(app, text="Redefinir senha", command=redefinir_senha, state="disabled")
botao_redefinir.pack(pady=10)

resultado = ctk.CTkLabel(app, text="")
resultado.pack(pady=10)

app.mainloop()
