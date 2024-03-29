quantidade_linha = information_matriz = 0
dados_das_matrizes =  dados_divididos_num = list()
dados_matriz = list()
for quant_matrizes in range(0,2):
    quantidade_linha = 0
    print()
    while True:
        quantidade_linha += 1
        information_matriz = input(f'Matriz {quant_matrizes+1} Linhas {quantidade_linha}:')
        dados_divididos_str = information_matriz.split()
        dados_divididos_num = list()
        for c in range(0,len(dados_divididos_str)):
            dados_divididos_num.append(int(dados_divididos_str[c]))
        if len(information_matriz) == 0:
            dados_das_matrizes.append(quantidade_linha-1)
            break
        else:
            #Parte que ler a linha anterior e ver se tem o mesmo número de colunas, mas não dar um conflito
            if quantidade_linha > 1:
                if quant_matrizes == 0:
                    if len(dados_matriz[0]) != len(dados_divididos_num):
                        quantidade_linha -= 1
                        print('Favor digitar o mesmo número de colunas que a linha anterior ')
                    else:
                        dados_matriz.append(dados_divididos_num)
                if quant_matrizes == 1:
                    
                    if len(dados_matriz[len(dados_matriz)-1]) != len(dados_divididos_num):
                        quantidade_linha -= 1
                        print('Favor digitar o mesmo número de colunas que a linha anterior ')
                    else:
                        dados_matriz.append(dados_divididos_num)
            else:
                dados_matriz.append(dados_divididos_num)

def leituraDeMatriz(dado):
    tamanho_matriz_a = dados_das_matrizes[0]
    matriz_A = matriz_B = list()
    #pega os dados da primeira matriz da lista dados_matriz 
    if dado in 'aA':
        for c in range(0,tamanho_matriz_a):
            matriz_A.append(dados_matriz[c])
        return matriz_A
    #pega os dados da segunda matriz da lista dados_matriz 
    if dado in 'bB':
        for c in range(tamanho_matriz_a,len(dados_matriz)):
            matriz_A.append(dados_matriz[c])
        return matriz_B

def mostraMatriz(a,b):
    print(f'{a}:')
    #se por acaso receber uma string, não vai prazer o processo de dividir as linhas
    if isinstance(b,str):
        print(b)
    else:
        for c in range(0,len(b)):
            print(b[c])
            print()

def somaMatrizes(a,b):
    matriz_result_soma = list()
    test = list()
    #a condição para poder fazer a soma de matrizes, se por acaso não estiver com os termos result_soma recebe a string Inexistente!!!
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        for c1 in range(0,len(a)):
            test = list()
            for c2 in range(0,len(a[0])):
                test.append(0)
            matriz_result_soma.append(test)
        for c1 in range(0,len(a)):
            for c2 in range(0,len(a[0])):
                soma = a[c1][c2] + b[c1][c2]
                matriz_result_soma[c1][c2]=soma
        result_soma = matriz_result_soma
    else:
        result_soma = 'Inexistente!!!'
    return result_soma

def multiplicaMatrizes(a,b):
    mult = 0
    matriz_result_mult = list()
    #a condição para poder fazer uma multiplicação de matrizes, se por acaso não estiver diacordo, result_soma recebe a string Inexistente!!!
    if len(a[0]) == len(b):
        for linhas in range(0,len(a)):
            test = list()
            for colunas in range(0,len(b[0])):
                test.append(0)
            matriz_result_mult.append(test)
        for c in range(0,len(a)):
            for c3 in range(0,len(b[0])):
                result = 0
                for c2 in range(0,len(a[0])):
                    mult = a[c][c2] * b[c2][c3]
                    result = mult + result
                matriz_result_mult[c][c3] = result
        result_mult = matriz_result_mult
    else:
        result_mult = 'Inexistente!!'
    return result_mult


valoresB = leituraDeMatriz('b')
valoresA = leituraDeMatriz('a')
valoresSoma = somaMatrizes(valoresA,valoresB)
valoresMult = multiplicaMatrizes(valoresA,valoresB)
mostraMatriz('Matriz A',valoresA)
mostraMatriz('Matriz B:',valoresB)
mostraMatriz('Matriz Soma de A com B',valoresSoma)
mostraMatriz('Matriz multiplicação de A por B',valoresMult)


