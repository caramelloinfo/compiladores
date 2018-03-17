#Trabalho 01

keywords = {
    'and' : 'conjunção',
    'del' : 'apagar',
    'from' : 'origem',
    'not' : 'não',
    'while' : 'enquanto',
    'as' : 'como',
    'elif' : 'se se',
    'global' : 'serve para todas as funções',
    'or' : 'ou',
    'with' : 'com',
    'assert' : 'afirmar',
    'else' : 'se não',
    'if' : 'se',
    'object' : 'objeto',
    'pass' : 'passar',
    'yield' : 'produção',
    'break' : 'pauso',
    'except' : 'exceto',
    'import' : 'importar',
    'print' : 'imprimir',
    'class' : 'classe',
    'exec' : 'executar - o código será executado no escopo atual',
    'in' : 'dentro',
    'len' : 'retorna o número de itens de um objeto',
    'range' : 'iniciar, parar',
    'raise' : 'permite que o programador force uma exceção especificada a ocorrer',
    'continue' : 'continuar',
    'finally' : 'finalmente',
    'is' : 'é',
    'list' : 'lista',
    'return' : 'retornar',
    'def' : 'usado para definir função',
    'for' : 'para',
    'try' : 'especifica manipuladores de exceção e / ou código de limpeza para um grupo de instruções',
    'self' : 'auto - no sentido ele mesmo',
    'split' : 'dividir - separa as palavras de um texto',
    '+' : 'operador adicionar',
    '-' : 'operador subtrair',
    '*' : 'multiplicação',
    '**' : 'exponenciação',
    '/' : 'divisão',
    '//' : 'divisão - retorna inteiro',
    '%' : 'restante',
    '<<' : 'x << y - retorna x com os bits deslocados para a esquerda por lugares y',
    '>>' : 'x >> y - retorna x com os bits deslocados para a direita por lugares y',
    '&' : 'x & y - faz um "bitwise and". Cada bit da saída é 1 se o bit correspondente de x AND de y for 1, caso contrário, é 0',
    '|' : 'x | y - faz "bitwise ou". Cada bit da saída é 0 se o bit correspondente de x AND de y for 0, caso contrário, é 1',
    '~' : '~ x - retorna o complemento de x - o número que você recebe mudando cada 1 para 0 e cada 0 para um 1. Isto é o mesmo que -x-1',
    '^' : 'x ^ y - faz um "bitwise exclusive ou". Cada bit da saída é o mesmo que o bit correspondente em x se esse bit em y for 0, e é o complemento do bit em x se esse bit em y for 1',
    '<' : 'menor que',
    '>' : 'maior que', 
    '<=' : 'menor ou igual',
    '>=' : 'maior ou igual',
    '==' : 'igual',
    '!=' : 'diferente',
    '(' : 'abre parênteses',
    ')' : 'fecha parênteses',
    '[' : 'abre colchete',
    ']' : 'fecha colchete',
    '{' : 'abre chave',
    '}' : 'fecha chave',
    '@' : 'declaração',
    ',' : 'virgula',
    ':' : 'dois pontos',
    '=' : 'recebe',
    '+=' : 'incrementar',
    '-=' : 'decrementar',
    '*=' : 'recebe a multiplicação',
    '/=' : 'receber a divisão',
    }

codigo = "este é um código fonte de continua ^ / try"
outras = []
linha = codigo.split(' ')
coluna = codigo.split('\n')
posicaox = 0
lenlinha = 0
posicaoy = 0

for k in linha:
    if k in keywords:        
        print("|| token:",k,"\n|| descrição:", keywords[k], "\n|| identificação:",linha.index(k))
        print("_________________________________________________________________________")

           
    else:
        outras.append(k)
        
print("setença(s) não própria(s) da linguagem:\n",outras)

        

       
           

