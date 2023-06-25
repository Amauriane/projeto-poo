import tkinter
from tkinter import *
from tkinter import ttk



# cores que usamos
co0 = "#000000"
co1 = "#696969"  
co2 = "#fcc058"  
co4 = "#e85151"   
co6 = "#fcc058"  
co7 = "#e85151"  
co8 = "#BA55D3"
fundo = "#DEB887"

# janela principal
janela = Tk()
janela.title('')
janela.geometry('260x370')
janela.configure(bg=fundo)


# Divisão das janelas

frame_cima = Frame(janela, width=240, height=100, bg=co1, relief="raised")
frame_cima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=240, height=300, bg=fundo, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW)


# Frame de cima
app_x = Label(frame_cima, text='X', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co7 )
app_x.place(x=25, y=10)
app_x = Label(frame_cima, text='Jogador 1', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0 )
app_x.place(x=17, y=70)
app_x_pontos = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0 )
app_x_pontos.place(x=80, y=20)

app_separador = Label(frame_cima, text=':', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0 )
app_separador.place(x=110, y=20)

app_o = Label(frame_cima, text='O', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co4 )
app_o.place(x=170, y=10)
app_o = Label(frame_cima, text='Jogador 2', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0 )
app_o.place(x=165, y=70)
app_o_pontos = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0 )
app_o_pontos.place(x=130, y=20)




# Lógica do aplicativo
class jogodavelha:
    def __init__(self):
        self.jogador_1 = "X"
        self.jogador_2 = "O"
        self.titulo("Jogo da Velha")
    
pontuacao_1 = 0
pontuacao_2 = 0

# Divisão da tabela e para saber a posição de cada butão 
# e assim fazer melhor a interface
tabela = [['1','2','3'] , ['4','5','6'] , ['7','8','9']]

jogando ='X'
joga =''
contador = 0
contador_de_rodada = 0

# Função de escolha: Se o jogador quer X ou 0
def escolha():
    int(input("Digite 1 para ser X ou 2 para ser O: "))
    if escolha == '1':
        app_x()
        
    elif escolha == '2':
        app_o()
        
    iniciar_jogo()

botao_escolha = Button(frame_baixo, command=escolha, text='X ou O?', height=1,  font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0 )
botao_escolha.place(x=80, y=165)


def iniciar_jogo():
    botao_jogar.place(x=800, y=350)
    # Função para controlar o jogo
    def controlar(v):
        global jogando
        global contador
        global jogar

        # Para comparar os valores recebidos
        if v==str(1):
            # Para verificar se a posição do botao 0 está vazio ou não
            if botao_0['text']=='':
                # Verificando quem está jogando e definindo a cor do carácter
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8

                # Definindo a cor da palavra que foi colocada no botão
                # Marca a posição na tabela com o valor do jogador atual
                botao_0['fg'] = cor
                botao_0['text'] = jogando
                tabela[0][0]= jogando

                # verificando quem está jogando, para na próxima rodada trocar de jogador
                if jogando =='X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                # Acrescenta o contador na próxima rodada
                contador+=1

        if v==str(2):
            # Para verificar se a posição do botao 0 está vazio ou não
            if botao_1['text']=='':
                # Verificando quem está jogando e definindo a cor do carácter
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8

                # Definindo a cor da palavra que foi colocada no botão
                # Marca a posição na tabela com o valor do jogador atual
                botao_1['fg'] = cor
                botao_1['text'] = jogando
                tabela[0][1] = jogando

                # verificando quem está jogando, para na próxima rodada trocar de jogador
                if jogando =='X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                # Acrescenta o contador para proxima rodada
                contador+=1

        if v==str(3):
            if botao_2['text']=='':
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8

                botao_2['fg'] = cor
                botao_2['text'] = jogando
                tabela[0][2]= jogando
                if jogando =='X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                contador+=1   

        if v==str(4):
            if botao_3['text']=='':
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8
                botao_3['fg'] = cor
                botao_3['text'] = jogando
                tabela[1][0] = jogando
                if jogando =='X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                contador+=1

        if v==str(5):
            if botao_4['text']=='':
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8

                botao_4['fg'] = cor
                botao_4['text'] = jogando
                tabela[1][1] = jogando

                if jogando =='X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                
                contador+=1

        if v==str(6):
            if botao_5['text']=='':
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8

                botao_5['fg'] = cor
                botao_5['text'] = jogando
                tabela[1][2] = jogando

                
                if jogando =='X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                
                contador+=1   

        if v==str(7):
         
            if botao_6['text']=='':
                
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8

                botao_6['fg'] = cor
                botao_6['text'] = jogando
                tabela[2][0] = jogando
                if jogando =='X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

               
                contador+=1

        if v==str(8):
            if botao_7['text']=='':
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8
                botao_7['fg'] = cor
                botao_7['text'] = jogando
                tabela[2][1] = jogando

                if jogando =='X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                contador+=1      

        if v==str(9):
            if botao_8['text']=='':
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8

                botao_8['fg'] = cor
                botao_8['text'] = jogando
                tabela[2][2] = jogando

                if jogando =='X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'

                
                contador+=1

        if contador>=5:
            # LINHAS 
            if tabela[0][0]==tabela[0][1]==tabela[0][2]!="":
                vencedor(jogando)
            elif tabela[1][0] == tabela[1][1]==tabela[1][2]!="":
                vencedor(jogando)
            elif tabela[2][0] == tabela[2][1]==tabela[2][2]!="":
                vencedor(jogando)

            # COLUNAS
            if tabela[0][0] == tabela[1][0]==tabela[2][0]!="":
                vencedor(jogando)
            elif tabela[0][1] == tabela[1][1]==tabela[2][1]!="":
                vencedor(jogando)
            elif tabela[0][2] == tabela[1][2]==tabela[2][2]!="":
                vencedor(jogando)


            # DIAGONAIS
            if tabela[0][0] == tabela[1][1]==tabela[2][2]!="":
                vencedor(jogando)
            elif tabela[0][2] == tabela[1][1]==tabela[2][0]!="":
                vencedor(jogando)

            # EMPATE 
            if contador>=9:
                vencedor('Foi empate') 
    
        
    # Função para decidir o vencedor
    def vencedor(i):
        global tabela
        global pontuacao_1
        global pontuacao_2
        global contador_de_rodada
        global contador

        # Para bloquear os botões já usados
        botao_0['state']='disable'
        botao_1['state']='disable'
        botao_2['state']='disable'
        botao_3['state']='disable'
        botao_4['state']='disable'
        botao_5['state']='disable'
        botao_6['state']='disable'
        botao_7['state']='disable'
        botao_8['state']='disable'

        app_vencedor = Label(frame_baixo, text='', width=17, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2 )
        app_vencedor.place(x=40, y=220)

        if i =='X':
            pontuacao_2+=1
            app_vencedor['text'] = "O jogador 2 venceu!"
            app_o_pontos['text'] =pontuacao_2

        if i =='O':
            pontuacao_1+=1
            app_vencedor['text'] = "O jogador 1 venceu!"
            app_x_pontos['text'] =pontuacao_1

        if i=='Foi empate':
            app_vencedor['text'] = "Velha"

        def comecar():
            # limpando os botoes para outras rodadas
            botao_0['text']=''
            botao_1['text']=''
            botao_2['text']=''
            botao_3['text']=''
            botao_4['text']=''
            botao_5['text']=''
            botao_6['text']=''
            botao_7['text']=''
            botao_8['text']=''

            botao_0['state']='normal'
            botao_1['state']='normal'
            botao_2['state']='normal'
            botao_3['state']='normal'
            botao_4['state']='normal'
            botao_5['state']='normal'
            botao_6['state']='normal'
            botao_7['state']='normal'
            botao_8['state']='normal'

            app_vencedor.destroy()
            botao_jogar.destroy()
        
        # Botão de jogar
        botao_jogar = Button(frame_baixo, command=comecar, text='Próxima rodada', height=1,  font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0 )
        botao_jogar.place(x=70, y=190)


        def jogo_acabou():
            botao_jogar.destroy()
            app_vencedor.destroy()

            terminar()

        if contador_de_rodada>=5:
            jogo_acabou()
        else:
            contador_de_rodada+=1
            # Reiniciando a tabela para outras jogadas
            tabela = [['1','2','3'] , ['4','5','6'] , ['7','8','9']]
            contador = 0



    # Função para terminar o jogo atual
    def terminar():
        global tabela
        global contador_de_rodada
        global pontuacao_1
        global pontuacao_2
        global contador

        tabela = [['1','2','3'] , ['4','5','6'] , ['7','8','9']]
        contador_de_rodada = 0
        pontuacao_1 = 0
        pontuacao_2 = 0
        contador = 0

        # Bloqueando os botões já usados
        botao_0['state']='disable'
        botao_1['state']='disable'
        botao_2['state']='disable'
        botao_3['state']='disable'
        botao_4['state']='disable'
        botao_5['state']='disable'
        botao_6['state']='disable'
        botao_7['state']='disable'
        botao_8['state']='disable'

        fim = Label(frame_baixo, text='Jogo Acabou', width=17, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2 )
        fim.place(x=25, y=90)

        
        # Função caso o jogador queira jogar novamente, depois do jogo ter acabado
        def jogar_denovo():
            app_x_pontos['text'] = '0'
            app_o_pontos['text'] = '0'
            fim.destroy()
            botao_jogar.destroy()

            # Chamando a função iniciar o jogo
            iniciar_jogo()

        # Botão jogar novamente
        botao_jogar = Button(frame_baixo, command=jogar_denovo, text='Jogar novamente', height=1,  font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0 )
        botao_jogar.place(x=80, y=197)


    # LINHAS VERTICAIS
    app_ = Label(frame_baixo, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7 )
    app_.place(x=90, y=15)
    app_ = Label(frame_baixo, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7 )
    app_.place(x=157, y=15)

    # LINHAS HORIZONTAIS
    app_ = Label(frame_baixo, text='', width=46, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7 )
    app_.place(x=30, y=63)
    app_ = Label(frame_baixo, text='', width=46, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7 )
    app_.place(x=30, y=127)

    # LINHA 0
    botao_0 = Button(frame_baixo,command=lambda:controlar('1'), text='', width=3, height=1,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    botao_0.place(x=30, y=15)
    botao_1 = Button(frame_baixo,command=lambda:controlar('2'), text='', width=3, height=1,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    botao_1.place(x=96, y=15)
    botao_2 = Button(frame_baixo,command=lambda:controlar('3'), text='', width=3, height=1,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    botao_2.place(x=163, y=15)


    # LINHA 1
    botao_3 = Button(frame_baixo,command=lambda:controlar('4'), text='', width=3, height=1,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    botao_3.place(x=30, y=75)
    botao_4 = Button(frame_baixo,command=lambda:controlar('5'), text='', width=3, height=1,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    botao_4.place(x=96, y=75)
    botao_5 = Button(frame_baixo,command=lambda:controlar('6'), text='', width=3, height=1,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    botao_5.place(x=163, y=75)

    # LINHA 2
    botao_6 = Button(frame_baixo,command=lambda:controlar('7'), text='', width=3, height=1,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    botao_6.place(x=30, y=135)
    botao_7 = Button(frame_baixo,command=lambda:controlar('8'), text='', width=3, height=1,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    botao_7.place(x=96, y=135)
    botao_8 = Button(frame_baixo,command=lambda:controlar('9'), text='', width=3, height=1,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    botao_8.place(x=163, y=135)

# Botão de jogar
botao_jogar = Button(frame_baixo, command=iniciar_jogo, text='Jogar', width=10, height=1,  font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0 )
botao_jogar.place(x=85, y=197)


janela.mainloop()