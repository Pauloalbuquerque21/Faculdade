entrada = 0

resultado=0
vezes=0
media = 0
vezes2 = 0
maior = 0
menor = 0
while True:
    entrada = str(input('Digite um número:'))
    vezes = vezes + len(entrada)
    if len(entrada) != 0:
        try:
            numero = int(entrada)
            resultado = resultado + numero
            vezes2= 1 + vezes2
            media = resultado / vezes2
            if vezes2 == 1:
                maior = numero
                menor = numero
            else:
                if numero > maior:
                    maior = numero
                if numero < menor:
                    menor = numero
        except ValueError:
            print('valor não indentificado')
    else:
        if len(entrada)==0 and numero == 0 and vezes == 0:
           print('Nunhum número foi lido - A primeira linha lida foi vazia')
           break 
        else:
            break
        
        
print('Média:',media,'Maior número:',maior,'Menor número:',menor)


        