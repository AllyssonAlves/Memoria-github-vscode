import tkinter as tk
from tkinter import messagebox
import random

#Configurações do jogo
num_linhas = 4
num_colunas = 4
cartao_size_weight = 10
cartao_size_height = 10
cores_cartao = ['red', 'blue', 'green', 'yellow', 'purble', 'orange', 'cyan', 'magenta']
cor_fundo = "#343a40"
cor_letra = "#ffffff"
font_style = ('Arial', 12, 'bold')
max_tentativas= 10

#Interface Principal
janela = tk.Tk()
janela.title('Jogo da Memoria')
janela.configure(bg=cor_fundo)

#Cria uma grade aleatoria de cores para os cartoes
def cria_card_grid():
    cores = cores_cartao * 2
    random.shuffle(cores)
    grid = []
    for _ in range(num_linhas):
        linha = []
        for _ in range(num_colunas):
            cor = cores.pop()
            linha.append(cor)
        grid.append(linha)
    return grid

# Lidar com o Click
def click(linha, coluna):
    cartao = cartoes[linha][coluna]
    cor = cartao['bg']
    if cor == 'black':
        cartao['bg']=grid[linha][coluna]
        cartao_revelado.append(cartao)
        if len(cartao_revelado) == 2:
            check_match()
        

#Cria grade cartoes
grid = cria_card_grid()
cartoes = []
cartao_revelado = []
cartao_correspondentes = []
numero_tentativas = 0

for linha in range(num_linhas):
    linha_de_cartoes = []
    for col in range(num_colunas):
        cartao = tk.Button(janela, command=lambda r=linha, c=col: click(r, c), width=cartao_size_weight, bg='black', relief=tk.RAISED, bd=3)
        cartao.grid(row=linha, column=col, padx=5, pady=5)
        linha_de_cartoes.append(cartao)
    cartoes.append(linha_de_cartoes)


#Personalizando o botao
button_style = {'activebackground': '#f8f9fa', 'font':font_style, 'fg':cor_letra}
janela.option_add('Button', button_style)



#verificar se iguais
def check_match():
    carta1, carta2 = cartao_revelado
    if carta1['bg'] == carta2['bg']:
        carta1.after(1000,carta1.destroy)
        carta2.after(1000,carta2.destroy)
        cartao_correspondentes.extend([carta1, carta2])
        check_win()
    else:
        carta1.after(1000,lambda:carta1.config(bg='black'))
        carta2.after(1000,lambda:carta2.config(bg='black'))
    cartao_revelado.clear()
    update_score()
    


#check win
def check_win():
    if len(cartao_correspondentes) == num_linhas * num_colunas:
        messagebox.showinfo('Parabens!', 'Voce ganhou o jogo"')
        janela.quit()
        
#update
def update_score():
    global numero_tentativas
    numero_tentativas +=1
    label_tentativas.config(text='Tentativas: {}/{}'.format(numero_tentativas,max_tentativas))
    if numero_tentativas >= max_tentativas:
        messagebox.showinfo('Fim de Jogo, voce perdeu!!')
        janela.quit()
        


#Tentativas
label_tentativas = tk.Label(janela, text='Tentativas: {}/{}'.format(numero_tentativas,max_tentativas), fg=cor_letra, bg=cor_fundo, font=font_style)
label_tentativas.grid(row=num_linhas, column=num_colunas, padx=10, pady=10)

janela.mainloop()
