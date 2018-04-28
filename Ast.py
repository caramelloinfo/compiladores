#trabalho 28/04/2018

class No:
    def __init__(self,valor):

        self.info=valor
        self.e1=None
        self.oper=None
        self.e2=None

    def insere(self,valor):
        if self.e1 == None:
            self.e1 = No(valor)
            print("________ E :: insere na esquerda")
            print(self.e1.info)

        else:
            if self.oper == None:
                self.oper = No(valor)
                print("________ OPERADOR :: insere no meio")
                print(self.oper.info)
            else:
                if self.e2 == None:
                    self.e2 = No(valor)
                    print("________ E :: insere na direita")
                    print(self.e2.info)
                else:
                    self.e2.insere(valor)

'-------------------------------------------------------'

class Ast:
    def __init__(self):
        self.raiz=None

    def insere(self,valor):
        if self.raiz == None:
            self.raiz = No(valor)
            print("________raiz____________")
            print(self.raiz.info)
        else:
            self.raiz.insere(valor)
            

