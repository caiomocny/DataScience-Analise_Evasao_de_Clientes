#!/usr/bin/env python
# coding: utf-8

# # Análise de Dados com Python
# 
# ### Desafio:
# 
# Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone.
# 
# O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes.
# 
# Isso representa uma perda de milhões para a empresa.
# 
# O que a empresa precisa fazer para resolver isso?
# 
# Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=sharing <br>
# Link Original do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset


# Passo 1: Acessar o banco de dados
import pyautogui
import pyperclip
import pandas as pd
from time import sleep

pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=sharing')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
sleep(5)
pyautogui.click(x=354, y=133)
sleep(1)
pyperclip.copy('telecom_users.csv') # escrever nome do arquivo
pyautogui.hotkey('ctrl', 'v')
sleep(1)
pyautogui.press('down')
pyautogui.press('enter') # selecionar arquivo
sleep(2)

# Passo 2: Baixar o banco de dados 
pyautogui.click(x=1291, y=129)
sleep(4)

# Passo 3: importar bd no python -> tabela = pd.read_csv(r'')
tabela = pd.read_csv(r'C:\Users\caiom\Downloads\telecom_users.csv')

# Passo 4: visualizar o banco de dados (tabela)
display(tabela)

## PASSO 5: TRATAR OS DADOS SEMPRE !! ##
# colunas inúteis '(podem confundir e tornar o bd + pesasdo)'
if 'Unnamed: 0' in tabela.columns:
    tabela = tabela.drop('Unnamed: 0', axis = 1) # axis=0 -> linhas / axis=1 -> colunas
else:

    # analisar os types de valores de cada coluna, se estão na forma correta para serem manipulados '(object -> texto)'
    tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce') # modificar a coluna em numérica

    # tratar os valores vazios '(sugestão caso não queira excluir: colocar o valor da média da coluna no dado vazio)'
    tabela = tabela.dropna(axis=1, how='all')
    tabela = tabela.dropna(axis=0, how='any') # o número de valores na coluna que desejo analisar, tem que ser o mesmo número de linhas da tabela


# Passo 6: Análise inicial para identificar possíveis suspeitas da dor
print(tabela['Churn'].value_counts()) # calcular valores
print(tabela['Churn'].value_counts(normalize=True).map('{:.1%}'.format)) # definir porcentagens

# # Instalar o pacote plotly
# !pip install plotly

# Passo 7: Análise detalhada (Manipular os dados)
import plotly.express as px

for coluna in tabela.columns:
    fig = px.histogram(tabela, x=coluna, color="Churn")
    fig.show()

# ### Conclusões e Ações:

# - Pessoas com famílias menores tem mais chance de cancelar:
#     - Pode haver alguma ação promocional que esteja trazendo clientes desqualificados
#     - Podemos criar um plano família e individual para diminuir a taxa de cancelamento
# - Nos primeiros 2 meses, 50% dos clientes cancelam:
#     - 1° experiência pode está sendo maléfica
#     - Dar descontos em planos anuais evitando o contrato mensal
# - Temos um problema com a FIBRA, taxa de cancelamento muito alta
# - Quanto mais serviços mais a chance de cancelamento
# - Diminuir limite de pagamentos em boleto, dar descontos ou bonificações nas demais formas de pagamento


display(tabela.info())
#print(tabela.columns)
print(len(tabela.columns))
print(tabela.columns[1])
fig = px.histogram(tabela, x="Genero", color="Churn")
fig.show()
