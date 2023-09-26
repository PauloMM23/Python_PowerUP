# Passo a passo do projeto

# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui # importa a biblioteca pyautogui
import time # importa a biblioteca time

# pyautogui.click # Clica onde estiver o mouse
# pyautogui.write # Escreve onde estiver o mouse
# pyautogui.press # Aperta uma tecla
# pyautogui.hotkey # Aperta uma combinação de teclas

pyautogui.PAUSE = 0.5 # pausa de 0.5 segundos entre cada comando

# abrir o Navegador Opera GX
pyautogui.press("win")
pyautogui.write("Navegador Opera GX")
pyautogui.press("enter")

# entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# esperar site carregar
time.sleep(3) # espera 3 segundos

# Passo 2: Fazer login
pyautogui.click(x=810, y=357) # clica no campo de email
pyautogui.write("pythonimpressionador@gmail.com") # escreve o email

pyautogui.press("tab") # aperta a tecla tab
pyautogui.write("Impressionador") # escreve a senha

pyautogui.press("tab") # muda para o botão de login
pyautogui.press("enter") # clica no botão de login

# Passo 3: Importar a base de dados de produtos
import pandas

tabela = pandas.read_csv("produtos.csv") # lê a tabela de produtos
print(tabela) # mostra a tabela de produtos

for linha in tabela.index:

    # Passo 4: Cadastrar 1 produto
    pyautogui.click(x=826, y=241) # clica no botão de adicionar produto

    codigo = tabela.loc[linha, "codigo"] # pega o código da tabela

    # preencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"] # pega a observação da tabela
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    # apertar para enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(50000)