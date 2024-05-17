import random
from tkinter import *
#from home2 import a
class suduko():
    def __init__(self,difficult):
        self.difficult = difficult
    def __str__(self):
        return f'{self.difficult}'
    
    def suduku_pricipal(self):
        listas=[[],[],[],[],[],[],[],[],[]]
        for c in range(0,9):
            for c2 in range(0,9):
                listas[c].append(".")
        return listas
    
    def suduko_usuario(self,listas,dificuldade):
        erros = 0
        horinzontal = ['0','1','2','3','4','5','6','7','8']
        vertical = [0,1,2,3,4,5,6,7,8]
        etapa = 0
        linha_maquina = 0
        vezes = 0
        valores_coluna = 0

        #loop do jogo:
        while True:

            lista_visual = list()
            #etapa que a maquina preenche as informações
            if  etapa == 0 : 
                if dificuldade == 0 :
                    if valores_coluna == 4:
                        valores_coluna = 0
                        linha_maquina = linha_maquina + 1
                    coluna = random.randint(0, 8)
                    valor = str(random.randint(1,9))
                    linha = linha_maquina
                elif dificuldade == 1 :
                    if valores_coluna == 3:
                        valores_coluna = 0
                        linha_maquina = linha_maquina + 1
                    coluna = random.randint(0, 8)
                    valor = str(random.randint(1,9))
                    linha = linha_maquina
                elif dificuldade == 2 :
                    if valores_coluna == 2:
                        valores_coluna = 0
                        linha_maquina = linha_maquina + 1
                    coluna = random.randint(0, 8)
                    valor = str(random.randint(1,9))
                    linha = linha_maquina
            #etapa que o jogador começa preencher as informações
            else:

                #tela do jogo, com tkinter
                white = Label(janela_principal,background='white', width=40, height=20)
                white.pack(side='top')

                horizontal_visual = ' '.join(horinzontal)

                print(f'   {horizontal_visual}')
                print('  ------------------')
                texto = f'   {horizontal_visual}\n   ------------------\n'
                for c in range(0,9):
                    hozontal_ventical = '  '.join(horinzontal)
                    lista_visual = '  '.join(listas[c])
                    texto+=f'{vertical[c]}| {lista_visual}\n'
                
                white.config(text=texto)
                #interface dos botões interativos 
                entry()
                
                def entry():
                    global Entry_linha, Entry_coluna, Entry_valor
                    Entry_linha = Entry(janela_principal, width=30 )
                    Entry_linha.pack(side="top")

                    Entry_coluna = Entry(janela_principal, width=30 )
                    Entry_coluna.pack(side="top")

                    Entry_valor = Entry(janela_principal, width=30 )
                    Entry_valor.pack(side="top")

                    botao_ativar = Button(janela_principal, text='Enter', command=valores)
                    botao_ativar.pack(side="bottom")
                

                def valores():
                    global linha,coluna,valor
                    texto_linha = Entry_linha.get()
                    texto_coluna = Entry_coluna.get()
                    texto_valor = Entry_valor.get()
                    #linha, coluna e valor que o usuário deseja
                    linha_usuario = int(texto_linha)
                    coluna_usuario = int(texto_coluna)
                    valor_usuario = str(texto_valor)
                
                    linha = linha_usuario
                    coluna = coluna_usuario
                    valor = valor_usuario
                    white.pack_forget()


            #veriaveis:
            confere_inferior = 0
            confere_superior = 0
            confere_linha = 0
            quadrado = 0
            # conferir se está na linha:
            if valor not in listas[linha]:
                confere_linha += 1
            #verificar as linhas inferiores, mesma coluna:
            for quant2 in range(linha-1,-1,-1):
                if valor != listas[quant2][coluna]:
                    confere_inferior += 1
            #verificar linhas superiores, da mesma coluna:
            for superior in range(linha+1,9):
                if valor != listas[superior][coluna]:
                    confere_superior += 1
            #verificar os quadrados:
            #quadrado 1        
            if (linha <=2) and (coluna <=2):
                for linha_verif in range(0,3):
                    for coluna_verif in range(0,3):
                        if valor == listas[linha_verif][coluna_verif]:
                            quadrado += 1
            
            #quadrado 2
            elif (linha <= 2) and (3 <= coluna <=5):
                for linha_verif in range(0,3):
                    for coluna_verif in range(3,6):
                        if valor == listas[linha_verif][coluna_verif]:
                            quadrado += 1
            #quadrado 3
            elif (linha <=2) and (6<=coluna <=8):
                for linha_verif in range(0,3):
                    for coluna_verif in range(6,9):
                        if valor == listas[linha_verif][coluna_verif]:
                            quadrado += 1
            #quadrado 4
            elif (3<=linha <=5) and (coluna <=2):
                for linha_verif in range(3,5):
                    for coluna_verif in range(0,3):
                        if valor == listas[linha_verif][coluna_verif]:
                            quadrado += 1
            #quadrado 5
            elif (3<=linha <=5) and (3 <= coluna <=5):
                for linha_verif in range(3,6):
                    for coluna_verif in range(3,6):
                        if valor == listas[linha_verif][coluna_verif]:
                            quadrado += 1
            #quadrado 6
            elif (3<=linha <=5) and (6<=coluna <=8):
                for linha_verif in range(3,6):
                    for coluna_verif in range(6,9):
                        if valor == listas[linha_verif][coluna_verif]:
                            quadrado += 1
            #quadrado 7
            elif (6<=linha <=8) and (coluna <=2):
                for linha_verif in range(6,9):
                    for coluna_verif in range(0,3):
                        if valor == listas[linha_verif][coluna_verif]:
                            quadrado += 1
            #quadrado 8
            elif (6<=linha <=8) and (3 <= coluna <=5):
                for linha_verif in range(6,9):
                    for coluna_verif in range(3,6):
                        if valor == listas[linha_verif][coluna_verif]:
                            quadrado += 1
            #quadrado 9
            elif (6<=linha <=8) and (6<=coluna <=8):
                for linha_verif in range(6,9):
                    for coluna_verif in range(6,9):
                        if valor == listas[linha_verif][coluna_verif]:
                            quadrado += 1
            
            #conferir se todas as verificões estão certas:
            if (confere_inferior == linha) and (confere_superior == (9-(linha+1))) and (confere_linha == 1) and (quadrado == 0):
                listas[linha][coluna] = valor
                if etapa == 0:
                    vezes+=1
                    valores_coluna +=1
                    if dificuldade == 0:
                        if vezes == 36:
                            etapa+=1
                    if dificuldade == 1:
                        if vezes == 27:
                            etapa+=1
                    if dificuldade == 2:
                        if vezes == 18:
                            etapa+=1   
                elif etapa == 1:
                    resulta_suduko = 0
                    for verif_list in range(0,8):
                        for verif_col in range(0,8):
                            if listas[verif_list][verif_col] != '.':
                                resulta_suduko +=1
                    print(f'resultado{resulta_suduko}')

            else:
                if etapa == 1:
                    print('-------Jogada errada---------')
                    erros +=1
                    if erros == 4:
                        break




    def detect(self):
            result = 0
            while True:
                if (len(self.difficult) == len('facil')) and (self.difficult[0] == 'f'):#detectar se é facil
                    quant = 0
                    for letra1, letra2 in zip(self.difficult,'facil'):
                        if letra1 == letra2 :
                            quant +=1
                    if quant == 5:
                        result = 0
                        break
                elif len(self.difficult) == len('medio') and (self.difficult[0] == 'm'):#detectar se é medio
                    quant = 0
                    for letra1, letra2 in zip(self.difficult,'medio'):
                        if letra1 == letra2 :
                            quant +=1
                    if quant == 5:
                        result = 1
                        break
                    
                elif len(self.difficult) == len('dificil'):#detectar se é difícil
                    quant = 0
                    for letra1, letra2 in zip(self.difficult,'dificil'):
                        if letra1 == letra2 :
                            quant +=1
                    if quant == 7:
                        result = 2
                        break
                else:
                    print('Favor Digitar corretamente a dificuldade, lembrando sem a acenturação')
                    self.difficult = str(input('Digite a Dificuldade, Sem acentuação[Facil,Medio e Dificil]:').strip().lower())
                        
                      
            return result        


from tkinter import *
#print('-+'*20)
#print(f'SUDOKO'.center(20))
#print('-+'*20)
#print('Regra:\nvocê só tem direito de 3 erros.\nFavor digitar as linhas e colunas de 0 até 8\nDigitar as dificuldade sem acentuação')


#dificuldade = suduko(str(input('Digite a Dificuldade, Sem acentuação[Facil,Medio e Dificil]:').strip().lower()))
#print(f'Dificuldade selecionada:{dificuldade}')
#lista=dificuldade.suduku_pricipal()
#dificul = dificuldade.detect()
#dificuldade.suduko_usuario(lista,dificul)


def dificuldade():
    global dificuldade2, dificuldade1, botao_dificuldade
    #apagar o label infor
    infor.pack_forget()
    botao.pack_forget()
    #dificuldade
    dificuldade1 = Label(janela_principal, text='Digite a dificuldade')
    dificuldade1.pack(side='top')

    #Parte onde escrevemos.
    dificuldade2 = Entry(janela_principal,width=30)
    dificuldade2.pack(side='top')

    botao_dificuldade = Button(janela_principal, text="Enter", command = botao_clicado )
    botao_dificuldade.pack(side="top")

def botao_clicado():
    global a
    #Atribuir o valor do Entry no texto_dificuldade
    texto_dificuldade = dificuldade2.get()
    
    dificuldade = suduko(texto_dificuldade)

    #apagar o dificuldade1,dificuldade2 e voão
    dificuldade1.pack_forget()
    dificuldade2.pack_forget()
    botao_dificuldade.pack_forget()

    #Tela do jogo

    #a.configure(text='test')

    lista=dificuldade.suduku_pricipal()
    dificul = dificuldade.detect()
    #print(f'{lista},{dificul}')
    dificuldade.suduko_usuario(lista,dificul)

    

janela_principal = Tk()

#TITULO
janela_principal.title('SUDUKO')
janela_principal.geometry("400x500")


#labels
infor = Label(janela_principal, text='Regra:\nvocê só tem direito de 3 erros.\nFavor digitar as linhas e colunas de 0 até 8\nDigitar as dificuldade sem acentuação',background='white')
infor.pack(side='top')

botao = Button(janela_principal, text="Iniciar o jogo", command = dificuldade )
botao.pack(side="bottom")

janela_principal.mainloop()

