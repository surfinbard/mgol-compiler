import os
import util

class token:
    def __init__(self, proximo=None, anterior=None, classe=None, lexema=None, tipo=NULL):
        self.proximo = proximo
        self.anterior = anterior
        self.classe = classe
        self.lexema = lexema
    
    def push(self, classe, lexema):
 
        novo_token = token(classe = classe, lexema = lexema)
 
        novo_token.proximo = self.raiz
        novo_token.anterior = None
    
        if self.raiz is not None:
            self.raiz.anterior = novo_token
        self.raiz = novo_token

class analisador:

    def scanner(self, entrada):
        for i in range(0, len(entrada))
            contador_coluna += 1
            q0()

    def q0(self):

        # aqui precisamos completar e linkar estados
        # não sei mexer com python direito ainda, veja se fiz caquinha com self
        if próprio.isdigit():
            self.q1()
        elif '"' == próprio
            self.q7()
        elif '{' == próprio
            self.q9()
        elif '<' == próprio
            self.q13()
        elif '=' == próprio
            self.q17()
        elif '>' == próprio
            self.q18()
        elif '+' == próprio or '-' == próprio or '*' == próprio or '/' == próprio
            self.q21()
        elif '(' == próprio
            self.q21()
        elif ')' == próprio
            self.q22()
        elif ';' == próprio
            self.q23()
        elif ',' == próprio
            self.q24()
        elif 'e' == próprio
            self.q27()
        elif 'f' == próprio
            self.q38()
        elif 'i' == próprio
            self.q53()
        elif 'l' == próprio
            self.q64()
        elif 'r' == próprio
            self.q70()
        elif 'v' == próprio
            self.q74()
        elif 's' == próprio
            self.q86()
        elif próprio.isupper() or próprio.islower() or próprio == '_'
            self.q11()
        # verificar fim de linha
        #self.q86()
        #vericar \t \s \n
        #self.q26()
         else: #erro
        self.q25()


    def q1(self): # token *num*

    def q2(self):

    def q3(self): # token *num*

    def q4(self):

    def q5(self):

    def q6(self): # token *num*

    def q7(self): # literal

    def q8(self): # token *lit*

    def q9(self): #Abre { comentário

    def q10(self): # fecha } comentário

    def q11(self): # reconhece *id*

    def q12(self): # reconhece *EOF*

    def q13(self): # reconhece *<*
        if '>' == self.caracter:
            self.q14()
        elif '=' == self.caracter:
            self.q15()
        elif '-' == self.caracter:
            self.q16()
        else #erro

    def q14(self): # diferente <>

    def q15(self):  # menor igual <=

    def q16(self): # atribuicao <-

    def q17(self): # =

    def q18(self): # reconhece *>*			elif '=' == self.caracter:
        if '=' == self.caracter:
            self.q15()
        else  # erro

    def q19(self): # maior igual >=

    def q20(self): # operadores + - *  /

    def q21(self): # (

    def q22(self): # )

    def q23(self): # ;

    def q24(self): # ,

    def q25(self): # erro

    def q26(self): # \t \s \n

    def q27(self): # self.caracter = self.__obter_caracter()
        if 'n' == self.caracter:
            self.q28()
        elif 's' == self.caracter:
            self.q32()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q28(self):
        # self.caracter = self.__obter_caracter()
        if 't' == self.caracter:
            self.q29()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q29(self):
        # self.caracter = self.__obter_caracter()
        if 'a' == self.caracter:
            self.q30()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q30(self):
        # self.caracter = self.__obter_caracter()
        if 'o' == self.caracter:
            self.q31()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q31(): # reconhece o comando *entao*

    def q32(self):
        # self.caracter = self.__obter_caracter()
        if 'c' == self.caracter:
            self.q33()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q33(self):
        # self.caracter = self.__obter_caracter()
        if 'r' == self.caracter:
            self.q34()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q34(self):
        # self.caracter = self.__obter_caracter()
        if 'e' == self.caracter:
            self.q35()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: #implementa erro

    def q35(self):
        # self.caracter = self.__obter_caracter()
        if 'v' == self.caracter:
            self.q36()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q36(self):
        # self.caracter = self.__obter_caracter()
        if 'a' == self.caracter:
            self.q37()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q37(self): # reconhece o comando *escreva*

    def q38(self):
        # self.caracter = self.__obter_caracter()
        if 'a' == self.caracter:
            self.q39()
        elif 'i' == self.caracter:
            self.q45()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q39(self):
        # self.caracter = self.__obter_caracter()
        if 'c' == self.caracter:
            self.q40()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q40(self):
        # self.caracter = self.__obter_caracter()
        if 'a' == self.caracter:
            self.q41()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q41(self):
        # self.caracter = self.__obter_caracter()
        if 'a' == self.caracter:
            self.q42()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q42(self):
        # self.caracter = self.__obter_caracter()
        if 't' == self.caracter:
            self.q43()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

        def q43(self):
        # self.caracter = self.__obter_caracter()
        if 'e' == self.caracter:
            self.q44()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q44(): # reconhece o comando *facaate*

    def q45(self):
        # self.caracter = self.__obter_caracter()
        if 'm' == self.caracter:
            self.q46()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q46(self):
        # self.caracter = self.__obter_caracter()
        if 'f' == self.caracter:
            self.q47()
        elif 's' == self.caracter:
            self.q51()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q47(self):
        # self.caracter = self.__obter_caracter()
        if 'a' == self.caracter:
            self.q48()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q48(self):
        # self.caracter = self.__obter_caracter()
        if 'c' == self.caracter:
            self.q49()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui
    def q49(self):
        # self.caracter = self.__obter_caracter()
        if 'a' == self.caracter:
            self.q50()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q50(self): # reconhece o comando *fimfaca*

    def q51(self):
        # self.caracter = self.__obter_caracter()
        if 'e' == self.caracter:
            self.q52()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q52(self):  # reconhece o comando *fimse*

    def q53(self):
        # self.caracter = self.__obter_caracter()
        if 'n' == self.caracter:
            self.q54()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q54(self):
        # self.caracter = self.__obter_caracter()
        if 'i' == self.caracter:
            self.q55()
        elif 't' == self.caracter:
            self.q59()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q55(self):
        # self.caracter = self.__obter_caracter()
        if 'c' == self.caracter:
            self.q56()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else:


    # implementa erro aqui
    def q56(self):
        # self.caracter = self.__obter_caracter()
        if 'i' == self.caracter:
            self.q57()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui
    def q57(self):
        # self.caracter = self.__obter_caracter()
        if 'o' == self.caracter:
            self.q58()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q58():  # reconhece o estado *inicio*

    def q59(self):
        # self.caracter = self.__obter_caracter()
        if 'e' == self.caracter:
            self.q60()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q60(self):
        # self.caracter = self.__obter_caracter()
        if 'i' == self.caracter:
            self.q61()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q61(self):
        # self.caracter = self.__obter_caracter()
        if 'r' == self.caracter:
            self.q62()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q62(self):
        # self.caracter = self.__obter_caracter()
        if 'o' == self.caracter:
            self.q63()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q63():  # reconhece o estado *inteiro*

    def q64(self):
        # self.caracter = self.__obter_caracter()
        if 'e' == self.caracter:
            self.q65()
        elif 'i' == self.caracter:
            self.q68()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q65(self):
        # self.caracter = self.__obter_caracter()
        if 'i' == self.caracter:
            self.q66()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q66(self):
        # self.caracter = self.__obter_caracter()
        if 'a' == self.caracter:
            self.q67()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else:  # implementa erro aqui

    def q67(): # reconhece o estado *leia*

    def q68(self):
        # self.caracter = self.__obter_caracter()
        if 't' == self.caracter:
            self.q69()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q69(): # reconhece o estado *lit*

    def q70(self):
        # self.caracter = self.__obter_caracter()
        if 'e' == self.caracter:
            self.q71()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q71(self):
        # self.caracter = self.__obter_caracter()
        if 'a' == self.caracter:
            self.q72()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else:  # implementa erro aqui
    def q72(self):
        # self.caracter = self.__obter_caracter()
        if 'l' == self.caracter:
            self.q73()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q73(): # reconhece o estado *leia*

    def q74(self):
        # self.caracter = self.__obter_caracter()
        if 'a' == self.caracter:
            self.q75()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q75(self):
        # self.caracter = self.__obter_caracter()
        if 'r' == self.caracter:
            self.q76()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q76(self):
        # self.caracter = self.__obter_caracter()
        if 'i' == self.caracter:
            self.q77()
        if 'f' == self.caracter:
            self.q83()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q77(self):
        # self.caracter = self.__obter_caracter()
        if 'n' == self.caracter:
            self.q78()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: #implementa erro aqui

    def q78(self):
        # self.caracter = self.__obter_caracter()
        if 'i' == self.caracter:
            self.q79()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else:  # implementa erro aqui

    def q79(self):
        # self.caracter = self.__obter_caracter()
        if 'c' == self.caracter:
            self.q80()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else:  # implementa erro aqui

    def q80(self):
        # self.caracter = self.__obter_caracter()
        if 'i' == self.caracter:
            self.q81()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else:  # implementa erro aqui

    def q81(self):
        # self.caracter = self.__obter_caracter()
        if 'o' == self.caracter:
            self.q82()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q82(): # reconhece o estado *varinicio*

    def q83(self):
        # self.caracter = self.__obter_caracter()
        if 'i' == self.caracter:
            self.q84()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q84(self):
        # self.caracter = self.__obter_caracter()
        if 'm' == self.caracter:
            self.q85()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else: # implementa erro aqui

    def q85(): # reconhece o estado *varfim*

    def q86(self):
        # self.caracter = self.__obter_caracter()
        if 'e' == self.caracter:
            self.q87()
        elif self.caracter.isdigit() or self.caracter.islower() or self.caracter.isupper or self.caracter == '_'
            self.q11()
        elif self.caracter.isspace()  # reconheceu o lexema e deve ser lido o prox token
            # ler prox lexema
            # self.__lexema = self.__lexema[:len(self.__lexema) -1]
            # self.__cabeca -= 1
            # self.q10()
        else:  # implementa erro aqui

    def q87(): # reconhece o estado *se*


    def erro(self, cod):
        if(cod==1):
            print("Erro " + cod + ". Caractere inválido, linha " + contador_linha + ", coluna " + contador_coluna + ".\n")

    def main(self, fonte):
        if not os.path.exists(fonte)
            print("Arquivo não encontrado.\n")
        else 
            global contador_linha = 0        
            for line in fonte
                contador_linha += 1
                global contador_coluna = 0
                for word in line.split():
                    retorno_scanner = scanner(word)
                    if(casefold(retorno_scanner)=="erro*")
                        erro(int(retorno_scanner[5:6]))     
                    else"
                        print("Classe: " + retorno_scanner.classe + ", lexema: " + retorno_scanner.lexema + ", tipo: " + retorno_scanner.tipo + ".\n")