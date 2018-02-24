#http://wiki.python.org.br/ManipulandoStringsComPython

import re
keywords = {
    'é' : 'definicao 1',
    'a' : 'definicao a',
    'teste' : 'definicao 2'
    }

codigo = "este é um código fonte de continua \n teste"
outras = []
linha = codigo.split(' ')
coluna = codigo.split('\n')
posicaox = 0
lenlinha = 0
posicaoy = 0

for k in linha:
    if k in keywords:        
        print("setença - ",k,":", keywords[k])
        print("posição final dos caractere:",codigo.find(k)) #encontra a posição da coluna de cada caractere
        print("qtd de caracteres:",len(k))
        print("posição:",linha.index(k))
        print("_________________________")

           
    else:
        outras.append(k)
        
print("setença(s) não própria(s) da linguagem:\n",outras)

        

       
           

