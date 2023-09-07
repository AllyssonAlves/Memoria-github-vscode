import tkinter as tk
from tkinter import messagebox
import random

#Configurações do jogo
linhas = 4
colunas = 4
cartao_size_weight = 10
cartao_size_height = 10
color_cartao = ['red', 'blue', 'green', 'yellow', 'purble', 'orange', 'cyan', 'magenta']
cor_fundo = "#343a40"
cor_letra = "#ffffff"
font_style = ('Arial', 12, 'bold')
tenta_max = 10

#Interface Principal
janela = tk.Tk()
janela.title('Jogo da Memoria')
janela.configure(bg=cor_fundo)

#grade aleatoria cores cartas
def cria_card_grid():
    cores = color_cartao * 2
    random.shuffle(cores)
    grid = []
    for _ in range(linhas):
        linha = []
        for _ in range(colunas):
            cor = cores.pop()
            linha.append(cor)
        grid.append(linha)
    return grid

#grade cartão
grid = cria_card_grid()
cartoes = []
cartao_revelado = []
cartao_correspondentes = []
numero_tentativas = 0

for linha in range(linhas):
    linhas_de_cartoes = []
    for col in range(colunas):
        cartao = tk.Button(janela, width=cartao_size_weight, bg='black', relief=tk.RAISED, bd=3)
        cartao.grid(row=linha, column=col, padx=5, pady=5)
        linhas_de_cartoes
    cartoes.append(linhas_de_cartoes)




#cartões
button_style = {'activebackground': '#f8f9fa', 'font':font_style, 'fg':cor_letra}
janela.option_add('Button', button_style)

#Tentativas
label_tentativas = tk.Label(janela, text='Tentativas: {}/{}'.format(9,tenta_max), fg=cor_letra, bg=cor_fundo, font=font_style)
label_tentativas.grid(row=linhas, column=colunas, padx=10, pady=10)

janela.mainloop()
