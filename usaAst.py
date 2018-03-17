import Ast

a1=Ast.Ast()
a1.insere('E')
'''a1.insere('x')
a1.insere('+')
a1.insere('x')'''

keywords = {
    '+' : 'soma, adição',
    '-' : 'menos, subtração',
    '*' : 'vezes, multiplicação',
    '/' : 'divisão',
    'x' : 'incognita',
    'y' : 'incognita',
    '0' : 'zero',
    '1' : 'um',
    '2' : 'dois',
    '3' : 'três',
    '4' : 'quatro',
    '5' : 'cinco',
    '6' : 'seis',
    '7' : 'sete',
    '8' : 'oito',
    '9' : 'nove',
    }

expressao = "x+y"
exp = None
cont = 0
splitadas = []
for e in expressao:
    exp = expressao[cont]
    a1.insere(exp)
    splitadas.append(exp)
    cont=cont+1

    if exp in keywords:
        print("|| token: ",exp,"\n|| descrição: ", keywords[exp], "\n|| posição: ",expressao.index(exp))


print("splitadas", splitadas)
    
