
# ==> Funcao para alternar a visibilidade da senha no login <==
def alternar_visibilidade_senha_login(entry, checkbox): # Função que será usada para um conjunto de parametros que será especificado posteriormente
    if checkbox.get() == 1: # Define que a se a caixa de seleção estiver desmarcada (0 = false {caso a checkbox esteja descelecionado}, 1 = true {caso a checkbox esteja selecionada})
        entry.configure(show="") # Define que na variavel entry, que sera determinada posteriormente, não sobreporá nenhuma informação sobre os dados inseridos pelo cliente
    else: # Função que define para a situação inversa, caso a checkbox não tenha sido marcada pelo cliente
        entry.configure(show="*") # Define que na variavel entry, que sera determinada posteriormente, sobreporá com o caracter '*', com intuito de esconder a senha do cliente

