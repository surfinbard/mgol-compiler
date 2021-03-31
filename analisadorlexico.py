import os

#checar requerimentos
#ao iniciar o programa, a tabela de símbolos deverá ser preenchida com todas as PALAVRAS RESERVAS  da linguagem
#importante notar: nas transições de estados, atualizo o valor de i antes de chamar a transição, portanto "entrada" corresponde ao caractere lido APÓS o estado, ou seja, a próxima entrada
#qual é a flag EOF? tratar estado 12.
#o nosso automato considera que todos os operadores relacionais e símbolos têm ao menos um espaço em seguda

class token:
    def __init__(self, proximo=None, anterior=None, classe=None, lexema=None, tipo=NULL):
        self.proximo = proximo
        self.anterior = anterior
        self.classe = classe
        self.lexema = lexema
    
    def push(self, classe, lexema):
 
        novo_token = token(classe = classe, lexema = lexema)
        if(self.raiz == None):
            self.raiz = novo_token
            return

        self.raiz.anterior = novo_token
        novo_token.proximo = self.raiz
        self.raiz = novo_token
    
    def procura_na_lista(self, lexema):
        temp = self.raiz
        while temp:
            if temp.lexema == lexema:
                break
            temp = temp.next
        if temp == None:
            return False
        return temp

class analisador:

    def scanner(self, entrada):
        global i = 0 
     #   while i < len(entrada)
        contador_coluna += 1
        return q0(entrada[i])
        #se o retorno do q0 for id, verificar na tabela e dar push se nao tiver la
        #se nao for id, só retorna o token reconhecido

    def q0(self, entrada):

        if entrada.isdigit():
            contador_coluna += 1
            i += 1
            return q1(scanner.entrada[i])
        elif '"' == entrada:
            contador_coluna += 1
            i += 1
            return q7(scanner.entrada[i])
        elif '{' == entrada:
            contador_coluna += 1
            i += 1
            return q9(scanner.entrada[i])
        elif '<' == entrada:
            contador_coluna += 1
            i += 1
            return q13(scanner.entrada[i])
        elif '=' == entrada:
            contador_coluna += 1
            i += 1
            return q17(scanner.entrada[i])
        elif '>' == entrada:
            contador_coluna += 1
            i += 1
            return q18(scanner.entrada[i])
        elif '+' == entrada or '-' == entrada or '*' == entrada or '/' == entrada:
            contador_coluna += 1
            i += 1
            return q20(scanner.entrada[i])
        elif '(' == entrada:
            contador_coluna += 1
            i += 1
            return q21(scanner.entrada[i])
        elif ')' == entrada:
            contador_coluna += 1
            i += 1
            return q22(scanner.entrada[i])
        elif ';' == entrada:
            contador_coluna += 1
            i += 1
            return q23(scanner.entrada[i])
        elif ',' == entrada:
            contador_coluna += 1
            i += 1
            return q24(scanner.entrada[i])
        elif 'e' == entrada:
            contador_coluna += 1
            i += 1
            return q27(scanner.entrada[i])
        elif 'f' == entrada:
            contador_coluna += 1
            i += 1
            return q38(scanner.entrada[i])
        elif 'i' == entrada:
            contador_coluna += 1
            i += 1
            return q53(scanner.entrada[i])
        elif 'l' == entrada:
            contador_coluna += 1
            i += 1
            return q64(scanner.entrada[i])
        elif 'r' == entrada:
            contador_coluna += 1
            i += 1
            return q70(scanner.entrada[i])
        elif 'v' == entrada:
            contador_coluna += 1
            i += 1
            return q74(scanner.entrada[i])
        elif 's' == entrada:
            contador_coluna += 1
            i += 1
            return q86(scanner.entrada[i])
        elif entrada.isalpha():
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif '\\' == entrada:
            contador_coluna += 1
            i += 1
            return q26(scanner.entrada[i])
        else: 
            contador_coluna += 1
            i += 1
            return q25(1)


    def q1(self, entrada): # token *num*
        if self.entrada.isdigit():
            contador_coluna += 1
            i += 1
            return q1(scanner.entrada[i])
        elif '\.' == self.entrada:
            contador_coluna += 1
            i += 1
            return q2(scanner.entrada[i])
        elif 'e' == self.entrada or 'E' == self.entrada: 
            contador_coluna += 1
            i += 1
            return q4(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('NUM', main.word)
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q2(self, entrada):  
        if self.entrada.isdigit():
            contador_coluna += 1
            i += 1
            return q3(scanner.entrada[i])
        else: 
            return q25(1)

    def q3(self, entrada): # token *num*
        if self.entrada.isdigit():
            contador_coluna += 1
            i += 1
            return q3(scanner.entrada[i])
        elif 'e' == self.entrada or 'E' == self.entrada: 
            contador_coluna += 1
            i += 1
            return q4(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('NUM', main.word)
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q4(self, entrada):
        if self.entrada.isdigit():
            contador_coluna += 1
            i += 1
            return q6(scanner.entrada[i])
        elif '+' == self.entrada or '-' == self.entrada: 
            contador_coluna += 1
            i += 1
            return q5(scanner.entrada[i])
        else: 
            return q25(1)

    def q5(self, entrada): 
        if self.entrada.isdigit():
            contador_coluna += 1
            i += 1
            return q6(scanner.entrada[i])
        else: 
            return q25(1)

    def q6(self, entrada): # token *num*
        if self.entrada.isdigit():
            contador_coluna += 1
            i += 1
            return q6(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('NUM', main.word)
            return procura_na_lista(main.word)
        else: 
            return q25(1)
    
    def q7(self, entrada):
        if self.entrada == '\.':
            contador_coluna += 1
            i += 1
            return q7(scanner.entrada[i])
        elif self.entrada == '"':
            contador_coluna += 1
            i += 1
            return q8(scanner.entrada[i])
        else: 
            return q25(1)

    def q8(self, entrada): # token *lit*
        if self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('lit', main.word)
            return procura_na_lista(main.word)
        else: 
            return q25(2)

    def q9(self, entrada): #Abre { comentário
        if self.entrada == '\.':
            contador_coluna += 1
            i += 1
            return q9(scanner.entrada[i])
        elif self.entrada == '}':
            contador_coluna += 1
            i += 1
            return q10()
        else: 
            return q25(1)

    def q10(self, entrada) # fecha } comentário
        if self.entrada.isspace():
            return None
        else: 
            return q25(3)

    def q11(self, entrada): # reconhece *id*
        if self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_':
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', main.word)
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q12(self, entrada): # reconhece *EOF*

    def q13(self, entrada): # reconhece *<*
        if self.entrada == '-':
            contador_coluna += 1
            i += 1
            return q16(scanner.entrada[i])
        elif self.entrada == '=':
            contador_coluna += 1
            i += 1
            return q15(scanner.entrada[i])
        elif self.entrada == '>':
            contador_coluna += 1
            i += 1
            return q14(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('OPR', '<')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q14(self, entrada): # diferente <>
        if self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('OPR', '<>')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q15(self, entrada):  # menor igual <=
        if self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('OPR', '<=')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q16(self, entrada): # atribuicao <-
        if self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('OPR', '<-')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q17(self, entrada): # =
        if self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('OPR', '=')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q18(self, entrada): # reconhece *>
        if self.entrada == '=':
            contador_coluna += 1
            i += 1
            return q19(self.entrada[i])
        if self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('OPR', '>')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q19(self, entrada): # maior igual >=
        if self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('OPR', '>=')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q20(self, entrada): # operadores + - *  /
        if self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('OPM', main.word)
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q21(self, entrada): # (
        if self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('AB_P', '(')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q22(self, entrada): # )
        if self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('FC_P', ')')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q23(self, entrada): # ;
        if self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('PT_V', ';')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q24(self, entrada): # ,
        if self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('VIR', ',')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q25(self, entrada): # erro
        return erro(entrada)

    def q26(self, entrada): # \t \s \n
        if 'n' == self.entrada or 's' == self.entrada or 't' == self.entrada:
            return None
        else: 
            return q25(1)

    def q27(self, entrada): 
        if 'n' == self.entrada:
            contador_coluna += 1
            i += 1
            return q28(scanner.entrada[i])
        elif 's' == self.entrada:
            contador_coluna += 1
            i += 1
            return q32(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_':
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'e')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q28(self, entrada):
        if 't' == self.entrada:
            contador_coluna += 1
            i += 1
            return q29(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'en')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q29(self, entrada):
        if 'a' == self.entrada:
            contador_coluna += 1
            i += 1
            return q30(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'ent')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q30(self, entrada):
        if 'o' == self.entrada:
            contador_coluna += 1
            i += 1
            return q31(scanner.enrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'enta')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q31(self, entrada): # reconhece entao
        if self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('entao', 'entao')
            return procura_na_lista(main.word)
        else:
            return q25(1)

    def q32(self, entrada):
        if 'c' == self.entrada:
            contador_coluna += 1
            i += 1
            return q33(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'es')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q33(self, entrada):
        if 'r' == self.entrada:
            contador_coluna += 1
            i += 1
            return q34(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'esc')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q34(self, entrada):
        if 'e' == self.entrada:
            contador_coluna += 1
            i += 1
            return q35(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'escr')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q35(self, entrada):
        if 'v' == self.entrada:
            contador_coluna += 1
            i += 1
            return q36(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'escre')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q36(self, entrada):
        if 'a' == self.entrada:
            contador_coluna += 1
            i += 1
            return q37(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'escrev')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q37(self, entrada) #reconhece escreva
        if not procura_na_lista(main.word):
            push('escreva', 'escreva')
        return procura_na_lista(main.word)    

    def q38(self, entrada):
        if 'a' == self.entrada:
            contador_coluna += 1
            i += 1
            return q39(scanner.entrada[i])
        elif 'i' == self.entrada:
            contador_coluna += 1
            i += 1
            return q45(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'f')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q39(self, entrada):
        if 'c' == self.entrada:
            contador_coluna += 1
            i += 1
            return q40(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'fa')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q40(self, entrada):
        if 'a' == self.entrada:
            contador_coluna += 1
            i += 1
            return q41(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'fac')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q41(self, entrada):
        if 'a' == self.entrada:
            contador_coluna += 1
            i += 1
            return q42(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'faca')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q42(self, entrada):
        if 't' == self.entrada:
            contador_coluna += 1
            i += 1
            return q43(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'facaa')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

        def q43(self, entrada):
        if 'e' == self.entrada:
            contador_coluna += 1
            i += 1
            return q44(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'facaat')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q44(self, entrada) # reconhece *facaate*
        if not procura_na_lista(main.word):
            push('facaate', 'facaate')
        return procura_na_lista(main.word)   

    def q45(self, entrada):
        if 'm' == self.entrada:
            contador_coluna += 1
            i += 1
            return q46(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'fi')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q46(self, entrada):
        if 'f' == self.entrada:
            contador_coluna += 1
            i += 1
            return q47(scanner.entrada[i])
        elif 's' == self.entrada:
            contador_coluna += 1
            i += 1
            return q51(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('fim', 'fim')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q47(self, entrada):
        if 'a' == self.entrada:
            contador_coluna += 1
            i += 1
            return q48(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'fimf')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q48(self, entrada):
        if 'c' == self.entrada:
            contador_coluna += 1
            i += 1
            return q49(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'fimfa')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q49(self, entrada):
        if 'a' == self.entrada:
            contador_coluna += 1
            i += 1
            return q50(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'fimfac')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q50(self, entrada) # reconhece *fimfaca*
        if not procura_na_lista(main.word):
            push('fimfaca', 'fimfaca')
        return procura_na_lista(main.word)   

    def q51(self, entrada):
        if 'e' == self.entrada:
            contador_coluna += 1
            i += 1
            return q51(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'fims')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q52(self, entrada)  # reconhece *fimse*
        if not procura_na_lista(main.word):
            push('fimse', 'fimse')
        return procura_na_lista(main.word)  

    def q53(self, entrada):
        if 'n' == self.entrada:
            contador_coluna += 1
            i += 1
            return q54(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'i')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q54(self, entrada):
        if 'i' == self.entrada:
            contador_coluna += 1
            i += 1
            return q55(scanner.entrada[i])
        elif 't' == self.entrada:
            contador_coluna += 1
            i += 1
            return q59(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'in')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q55(self, entrada):
        if 'c' == self.entrada:
            contador_coluna += 1
            i += 1
            return q56(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'ini')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q56(self, entrada):
        if 'i' == self.entrada:
            contador_coluna += 1
            i += 1
            return q57(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'inic')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q57(self, entrada):
        if 'o' == self.entrada:
            contador_coluna += 1
            i += 1
            return q58(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'inici')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q58(self, entrada)  # reconhece *inicio*
        if not procura_na_lista(main.word):
            push('inicio', 'inicio')
        return procura_na_lista(main.word)      

    def q59(self, entrada):
        if 'e' == self.entrada:
            contador_coluna += 1
            i += 1
            return q60(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'int')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q60(self, entrada):
        if 'i' == self.entrada:
            contador_coluna += 1
            i += 1
            return q61(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'inte')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q61(self, entrada):
        if 'r' == self.entrada:
            contador_coluna += 1
            i += 1
            return q62(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'intei')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q62(self, entrada):
        if 'o' == self.entrada:
            contador_coluna += 1
            i += 1
            return q62(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'inteir')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q63(self, entrada)  # reconhece *inteiro*
        if not procura_na_lista(main.word):
            push('inteiro', 'inteiro')
        return procura_na_lista(main.word)      

    def q64(self, entrada):
        if 'e' == self.entrada:
            contador_coluna += 1
            i += 1
            return q65(scanner.entrada[i])
        elif 'i' == self.entrada:
            contador_coluna += 1
            i += 1
            return q68(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'l')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q65(self, entrada):
        if 'i' == self.entrada:
            contador_coluna += 1
            i += 1
            return q66(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'le')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q66(self, entrada):
        if 'a' == self.entrada:
            contador_coluna += 1
            i += 1
            return q67(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'lei')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q67(self, entrada) # reconhece *leia*
        if not procura_na_lista(main.word):
            push('leia', 'leia')
        return procura_na_lista(main.word)  

    def q68(self, entrada):
        if 't' == self.entrada:
            contador_coluna += 1
            i += 1
            return q69(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'li')
            return procura_na_lista(main.word)
        else: 
            return q25(1)


    def q69(self, entrada) # reconhece *lit*
        if not procura_na_lista(main.word):
            push('lit', 'lit')
        return procura_na_lista(main.word)  

    def q70(self, entrada)
        if 'e' == self.entrada:
            contador_coluna += 1
            i += 1
            return q71(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'r')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q71(self, entrada):
        if 'a' == self.entrada:
            contador_coluna += 1
            i += 1
            return q72(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 're')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q72(self, entrada):
        if 'l' == self.entrada:
            contador_coluna += 1
            i += 1
            return q73(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'rea')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q73(self, entrada): # reconhece *real*
        if not procura_na_lista(main.word):
            push('real', 'real')
        return procura_na_lista(main.word) 

    def q74(self, entrada):
        if 'a' == self.entrada:
            contador_coluna += 1
            i += 1
            return q75(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'v')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q75(self, entrada):
        if 'r' == self.entrada:
            contador_coluna += 1
            i += 1
            return q76(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'va')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q76(self, entrada):
        if 'i' == self.entrada:
            contador_coluna += 1
            i += 1
            return q77(scanner.entrada[i])
        elif 'f' == self.entrada:
            contador_coluna += 1
            i += 1
            return q83(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'var')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q77(self, entrada):
        if 'n' == self.entrada:
            contador_coluna += 1
            i += 1
            return q78(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'vari')
            return procura_na_lista(main.word)
        else: 
            return q25(1)


    def q78(self, entrada):
        if 'i' == self.entrada:
            contador_coluna += 1
            i += 1
            return q79(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'varin')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q79(self, entrada):
        if 'c' == self.entrada:
            contador_coluna += 1
            i += 1
            return q80(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'varini')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q80(self, entrada):
        if 'i' == self.entrada:
            contador_coluna += 1
            i += 1
            return q81(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'varinic')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q81(self, entrada):
        if 'o' == self.entrada:
            contador_coluna += 1
            i += 1
            return q82(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'varinici')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q82(self, entrada): # reconhece o estado *varinicio*
        if not procura_na_lista(main.word):
            push('varinicio', 'varinicio')
        return procura_na_lista(main.word) 

    def q83(self, entrada):
        if 'i' == self.entrada:
            contador_coluna += 1
            i += 1
            return q84(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'varf')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q84(self, entrada):
        if 'm' == self.entrada:
            contador_coluna += 1
            i += 1
            return q85(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 'varfi')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q85(): # reconhece o estado *varfim*
        if not procura_na_lista(main.word):
            push('varfim', 'varfim')
        return procura_na_lista(main.word) 

    def q86(self, entrada):
        if 'e' == self.entrada:
            contador_coluna += 1
            i += 1
            return q87(scanner.entrada[i])
        elif self.entrada.isdigit() or self.entrada.isalpha() or self.entrada == '_': 
            contador_coluna += 1
            i += 1
            return q11(scanner.entrada[i])
        elif self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('id', 's')
            return procura_na_lista(main.word)
        else: 
            return q25(1)

    def q87(self, entrada): # reconhece o estado *se*
        if self.entrada.isspace():
            if not procura_na_lista(main.word):
                push('se', 'se')
            return procura_na_lista(main.word) 
        else:
            return q25(1)

    def q88(self, entrada):
        if self.entrada.isspace():
            return None
        else:
            return q25(1)

    def erro(self, cod):
        if(cod==2):
            print("Erro " + cod + ". Aspas vêm ao final de constantes literais. Linha " + contador_linha + ", coluna " + contador_coluna + ".\n")
        elif(cod==3):
            print("Erro " + cod + ". Chaves devem fechar comentários. Linha " + contador_linha + ", coluna " + contador_coluna + ".\n")
        else:
            print("Erro " + cod + ". caractere inválido, linha " + contador_linha + ", coluna " + contador_coluna + ".\n")

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
                    else
                        print("Classe: " + retorno_scanner.classe + ", lexema: " + retorno_scanner.lexema + ", tipo: " + retorno_scanner.tipo + ".\n")
