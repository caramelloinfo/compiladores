class No:
    def __init__(self,valor):

        self.info=valor
        self.esq=None
        self.meio=None
        self.dir=None

    def insere(self,valor):
        if self.esq == None:
            self.esq = No(valor)
            print("________insere na esquerda_________")
            print(self.esq.info)

        else:
            if self.meio == None:
                self.meio = No(valor)
                print("________insere no meio_________")
                print(self.meio.info)
            else:
                if self.dir == None:
                    self.dir = No(valor)
                    print("________insere na direita_________")
                    print(self.dir.info)
                else:
                    self.dir.insere(valor)

'-------------------------------------------------------'

class Ast:
    def __init__(self):
        self.raiz=None

    def insere(self,valor):
        if self.raiz == None:
            self.raiz = No(valor)
            print("________insere na raiz_________")
            print(self.raiz.info)
        else:
            self.raiz.insere(valor)
            print("raiz ocupada, ver os lador e meio")
