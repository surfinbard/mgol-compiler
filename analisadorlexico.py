import os.path

i = 0
contador_coluna = 0
palavra = ""

class lista:
    def __init__(self):
        self.raiz = None

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
            temp = temp.proximo
        if temp == None:
            return False
        return temp

class token:
    def __init__(self, proximo=None, anterior=None, classe=None, lexema=None, tipo=None):
        self.proximo = proximo
        self.anterior = anterior
        self.classe = classe
        self.lexema = lexema
        self.tipo = "Nulo"

class analisador:
    lista = lista()
    def scanner(self): 
        global contador_coluna
        contador_coluna += 1
        i = 0
        return self.q0()

    def q0(self):
        global contador_coluna
        global i
        if palavra[i:i+1].isdigit(): 
            contador_coluna += 1
            i += 1
            return self.q1()
        elif '"' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q7()
        elif '{' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q9()
        elif '<' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q13()
        elif '=' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q17()
        elif '>' == palavra[i:i+1]:    
            contador_coluna += 1
            i += 1
            return self.q18()
        elif '+' == palavra[i:i+1] or '-' == palavra[i:i+1] or '*' == palavra[i:i+1] or '/' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q20()
        elif '(' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q21()
        elif ')' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q22()
        elif ';' == palavra[i:i+1]: 
            contador_coluna += 1
            i += 1
            return self.q23()
        elif ',' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q24()
        elif 'e' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q27()
        elif 'f' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q38()
        elif 'i' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q53()
        elif 'l' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q64()
        elif 'r' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q70()
        elif 'v' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q74()
        elif 's' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q86()
        elif palavra[i:i+1].isalpha():
            contador_coluna += 1
            i += 1
            return self.q11()
        elif '\\' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q26()
        else: 
            contador_coluna += 1
            i += 1
            return self.q25(1)


    def q1(self): # token *num*
        global contador_coluna
        global i
        if palavra[i:i+1].isdigit():
            contador_coluna += 1
            i += 1
            return self.q1()
        elif '\\.' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q2()
        elif 'e' == palavra[i:i+1] or 'E' == palavra[i:i+1]: 
            contador_coluna += 1
            i += 1
            return self.q4()
        elif palavra[i:i+1].isspace():
            lista = lista() 
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('NUM', palavra[i:i+1])
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q2(self):  
        global contador_coluna
        global i
        if palavra[i:i+1].isdigit():
            
            contador_coluna += 1
            i += 1
            return self.q3()
        else: 
            return self.q25(1)

    def q3(self): # token *num*
        global contador_coluna
        global i
        if palavra[i:i+1].isdigit():
            
            contador_coluna += 1
            i += 1
            return self.q3()
        elif 'e' == palavra[i:i+1] or 'E' == palavra[i:i+1]: 
            contador_coluna += 1
            i += 1
            return self.q4()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('NUM', palavra)
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q4(self):
        global contador_coluna
        global i
        if palavra[i:i+1].isdigit():
            contador_coluna += 1
            i += 1
            return self.q6()
        elif '+' == palavra[i:i+1] or '-' == palavra[i:i+1]: 
            contador_coluna += 1
            i += 1
            return self.q5()
        else: 
            return self.q25(1)

    def q5(self): 
        global contador_coluna
        global i
        if palavra[i:i+1].isdigit():
            contador_coluna += 1
            i += 1
            return self.q6()
        else: 
            return self.q25(1)

    def q6(self): # token *num*
        global contador_coluna
        global i
        if palavra[i:i+1].isdigit():
            contador_coluna += 1
            i += 1
            return self.q6()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('NUM', palavra)
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q7(self):
        global i
        global contador_coluna
        if palavra[i:i+1] == '\\.':
            
            contador_coluna += 1
            i += 1
            return self.q7()
        elif palavra[i:i+1] == '"':
            
            contador_coluna += 1
            i += 1
            return self.q8()
        else: 
            return self.q25(1)

    def q8(self): # token *lit*
        if palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('lit', palavra)
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(2)

    def q9(self): #Abre { comentário
        global i
        global contador_coluna
        while palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            if palavra[i:i+1] == '}':
                return self.q10()
        return self.q25(1)

    def q10(self): # fecha } comentário
        if palavra[i:i+1].isspace():
            return None
        else: 
            return self.q25(3)

    def q11(self): # reconhece *id*
        global i
        global contador_coluna
        if palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', palavra)
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q12(self): # reconhece *EOF*
        if palavra[i:i+1] == '$':
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('EOF', '$')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q13(self): # reconhece *<*
        global i
        global contador_coluna
        if palavra[i:i+1] == '-':
            contador_coluna += 1
            i += 1
            return self.q16()
        elif palavra[i:i+1] == '=':
            
            contador_coluna += 1
            i += 1
            return self.q15()
        elif palavra[i:i+1] == '>':
            
            contador_coluna += 1
            i += 1
            return self.q14()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('OPR', '<')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q14(self): # diferente <>
        if palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('OPR', '<>')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q15(self):  # menor igual <=
        if palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('OPR', '<=')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q16(self): # atribuicao <-
        if palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('OPR', '<-')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q17(self): # =
        global i
        if palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('OPR', '=')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q18(self): # reconhece *>
        global i
        global contador_coluna
        if palavra[i:i+1] == '=':
            contador_coluna += 1
            i += 1
            return self.q19()
        if palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('OPR', '>')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q19(self): # maior igual >=
        if palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('OPR', '>=')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q20(self): # operadores + - *  /
        if palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('OPM', palavra)
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q21(self): # (
        if palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('AB_P', '(')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q22(self): # )
        if palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('FC_P', ')')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q23(self): # ;
        if palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('PT_V', ';')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q24(self): # ,
        if palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('VIR', ',')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q25(self, entrada): # erro
        return self.erro(entrada)

    def q26(self): # \t \s \n
        if 'n' == palavra[i:i+1] or 's' == palavra[i:i+1] or 't' == palavra[i:i+1]:
            return None
        else: 
            return self.q25(1)

    def q27(self): 
        global i
        global contador_coluna
        if 'n' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q28()
        elif 's' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q32()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'e')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q28(self):
        global i
        global contador_coluna
        if 't' == palavra[i:i+1]:
            
            contador_coluna += 1
            i += 1
            return self.q29()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'en')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q29(self):
        global i
        global contador_coluna
        if 'a' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q30()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'ent')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q30(self):
        global i
        global contador_coluna
        if 'o' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q31()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'enta')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q31(self): # reconhece entao
        if palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('entao', 'entao')
            return lista.procura_na_lista(palavra[i:i+1])
        else:
            return self.q25(1)

    def q32(self):
        global i
        global contador_coluna
        if 'c' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q33()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'es')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q33(self):
        global i
        global contador_coluna
        if 'r' == palavra[i:i+1]:
            
            contador_coluna += 1
            i += 1
            return self.q34()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'esc')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q34(self):
        global i
        global contador_coluna
        if 'e' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q35()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'escr')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q35(self):
        global i
        global contador_coluna
        if 'v' == palavra[i:i+1]: 
            contador_coluna += 1
            i += 1
            return self.q36()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'escre')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q36(self):
        global i
        global contador_coluna
        if 'a' == palavra[i:i+1]: 
            contador_coluna += 1
            i += 1
            return self.q37()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'escrev')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q37(self): #reconhece escreva
        lista = lista()
        if not lista.procura_na_lista(palavra[i:i+1]):
            lista.push('escreva', 'escreva')
        return lista.procura_na_lista(palavra[i:i+1])    

    def q38(self):
        global i
        global contador_coluna
        if 'a' == palavra[i:i+1]: 
            contador_coluna += 1
            i += 1
            return self.q39()
        elif 'i' == palavra[i:i+1]:  
            contador_coluna += 1
            i += 1
            return self.q45()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'f')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q39(self):
        global i
        global contador_coluna
        if 'c' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q40()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'fa')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q40(self):
        global i
        global contador_coluna
        if 'a' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q41()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'fac')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q41(self):
        global i
        global contador_coluna
        if 'a' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q42()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'faca')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q42(self):
        global contador_coluna
        global i
        if 't' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q43()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'facaa')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q43(self):
        global i
        global contador_coluna
        if 'e' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q44()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'facaat')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q44(self): # reconhece *facaate*
        lista = lista()
        if not lista.procura_na_lista(palavra[i:i+1]):
            lista.push('facaate', 'facaate')
        return lista.procura_na_lista(palavra[i:i+1])   

    def q45(self):
        global i
        global contador_coluna
        if 'm' == palavra[i:i+1]:   
            contador_coluna += 1
            i += 1
            return self.q46()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':  
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'fi')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q46(self):
        global i
        global contador_coluna
        if 'f' == palavra[i:i+1]: 
            contador_coluna += 1
            i += 1
            return self.q47()
        elif 's' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q51()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('fim', 'fim')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q47(self):
        global i
        global contador_coluna
        if 'a' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q48()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'fimf')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q48(self):
        global i
        global contador_coluna
        if 'c' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q49()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'fimfa')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q49(self):
        global i
        global contador_coluna
        if 'a' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q50()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'fimfac')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q50(self): # reconhece *fimfaca*
        global i
        lista = lista()
        if not lista.procura_na_lista(palavra[i:i+1]):
            lista.push('fimfaca', 'fimfaca')
        return lista.procura_na_lista(palavra[i:i+1])   

    def q51(self):
        global i
        global contador_coluna
        if 'e' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q51()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'fims')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q52(self):  # reconhece *fimse*
        global i
        lista = lista()
        if not lista.procura_na_lista(palavra[i:i+1]):
            lista.push('fimse', 'fimse')
        return lista.procura_na_lista(palavra[i:i+1])  

    def q53(self):
        global i
        global contador_coluna
        if 'n' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q54()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'i')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q54(self):
        global i
        global contador_coluna
        if 'i' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q55()
        elif 't' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q59()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':  
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'in')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q55(self):
        global i
        global contador_coluna
        if 'c' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q56()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'ini')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q56(self):
        global i
        global contador_coluna
        if 'i' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q57()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'inic')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q57(self):
        global i
        global contador_coluna
        if 'o' == palavra[i:i+1]:    
            contador_coluna += 1
            i += 1
            return self.q58()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':  
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'inici')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q58(self):  # reconhece *inicio*
        lista = lista()
        if not lista.procura_na_lista(palavra[i:i+1]):
            lista.push('inicio', 'inicio')
        return lista.procura_na_lista(palavra[i:i+1])      

    def q59(self):
        global i
        global contador_coluna
        if 'e' == palavra[i:i+1]:  
            contador_coluna += 1
            i += 1
            return self.q60()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':   
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'int')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q60(self):
        global i
        global contador_coluna
        if 'i' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q61()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':  
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'inte')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q61(self):
        global i
        global contador_coluna
        if 'r' == palavra[i:i+1]: 
            contador_coluna += 1
            i += 1
            return self.q62()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'intei')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q62(self):
        global i
        global contador_coluna
        if 'o' == palavra[i:i+1]: 
            contador_coluna += 1
            i += 1
            return self.q62()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':  
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'inteir')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q63(self):  # reconhece *inteiro*
        global i
        lista = lista()
        if not lista.procura_na_lista(palavra[i:i+1]):
            push('inteiro', 'inteiro')
        return lista.procura_na_lista(palavra[i:i+1])      

    def q64(self):
        global i
        global contador_coluna
        if 'e' == palavra[i:i+1]:  
            contador_coluna += 1
            i += 1
            return self.q65()
        elif 'i' == palavra[i:i+1]:   
            contador_coluna += 1
            i += 1
            return self.q68()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':  
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'l')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q65(self):
        global i
        global contador_coluna
        if 'i' == palavra[i:i+1]: 
            contador_coluna += 1
            i += 1
            return self.q66()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'le')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q66(self):
        global i
        global contador_coluna
        if 'a' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q67()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':  
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'lei')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q67(self): # reconhece *leia*
        global i
        lista = lista()
        if not lista.procura_na_lista(palavra[i:i+1]):
            push('leia', 'leia')
        return lista.procura_na_lista(palavra[i:i+1])  

    def q68(self):
        global i
        global contador_coluna
        if 't' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q69()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'li')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)


    def q69(self): # reconhece *lit*
        global i
        lista = lista()
        if not lista.procura_na_lista(palavra[i:i+1]):
            push('lit', 'lit')
        return lista.procura_na_lista(palavra[i:i+1])  

    def q70(self):
        global i
        global contador_coluna
        if 'e' == palavra[i:i+1]: 
            contador_coluna += 1
            i += 1
            return self.q71()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'r')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q71(self):
        global i
        global contador_coluna
        if 'a' == palavra[i:i+1]:    
            contador_coluna += 1
            i += 1
            return self.q72()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 're')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q72(self):
        global i
        global contador_coluna
        if 'l' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q73()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'rea')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q73(self): # reconhece *real*
        global i
        lista = lista()
        if not lista.procura_na_lista(palavra[i:i+1]):
            push('real', 'real')
        return lista.procura_na_lista(palavra[i:i+1]) 

    def q74(self):
        global i
        global contador_coluna
        if 'a' == palavra[i:i+1]:  
            contador_coluna += 1
            i += 1
            return self.q75()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':   
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'v')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q75(self):
        global i
        global contador_coluna
        if 'r' == palavra[i:i+1]: 
            contador_coluna += 1
            i += 1
            return self.q76()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'va')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q76(self):
        global i
        global contador_coluna
        if 'i' == palavra[i:i+1]: 
            contador_coluna += 1
            i += 1
            return self.q77()
        elif 'f' == palavra[i:i+1]:  
            contador_coluna += 1
            i += 1
            return self.q83()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'var')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q77(self):
        global i
        global contador_coluna
        if 'n' == palavra[i:i+1]:   
            contador_coluna += 1
            i += 1
            return self.q78()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'vari')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q78(self):
        global i
        global contador_coluna
        if 'i' == palavra[i:i+1]:  
            contador_coluna += 1
            i += 1
            return self.q79()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':  
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'varin')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q79(self):
        global i
        global contador_coluna
        if 'c' == palavra[i:i+1]: 
            contador_coluna += 1
            i += 1
            return self.q80()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'varini')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q80(self):
        global i
        global contador_coluna
        if 'i' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q81()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'varinic')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q81(self):
        global i
        global contador_coluna
        if 'o' == palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            return self.q82()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'varinici')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q82(self): # reconhece o estado *varinicio*
        global i
        lista = lista()
        if not lista.procura_na_lista(palavra[i:i+1]):
            lista.push('varinicio', 'varinicio')
        return lista.procura_na_lista(palavra[i:i+1]) 

    def q83(self):
        global contador_coluna
        if 'i' == palavra[i:i+1]:    
            contador_coluna += 1
            i += 1
            return self.q84()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'varf')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q84(self):
        global i
        global contador_coluna
        if 'm' == palavra[i:i+1]:    
            contador_coluna += 1
            i += 1
            return self.q85()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 'varfi')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q85(): # reconhece o estado *varfim*
        global i
        lista = lista()
        if not lista.procura_na_lista(palavra[i:i+1]):
            lista.push('varfim', 'varfim')
        return lista.procura_na_lista(palavra[i:i+1]) 

    def q86(self):
        global i
        global contador_coluna
        if 'e' == palavra[i:i+1]:  
            contador_coluna += 1
            i += 1
            return self.q87()
        elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':   
            contador_coluna += 1
            i += 1
            return self.q11()
        elif palavra[i:i+1].isspace():
            lista = lista()
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('id', 's')
            return lista.procura_na_lista(palavra[i:i+1])
        else: 
            return self.q25(1)

    def q87(self): # reconhece o estado *se*
        global i
        lista = lista()
        if palavra[i:i+1].isspace():
            if not lista.procura_na_lista(palavra[i:i+1]):
                lista.push('se', 'se')
            return lista.procura_na_lista(palavra[i:i+1]) 
        else:
            return self.q25(1)

    def q88(self):
        global i
        if palavra[i:i+1].isspace():
            return None
        else:
            return self.q25(1)

    def erro(self, cod):
        if(cod==2):
            print("Erro " + str(cod) + ". Aspas vêm ao final de constantes literais. Linha " + str(contador_linha) + ", coluna " + str(contador_coluna) + ".\n")
        elif(cod==3):
            print("Erro " + str(cod) + ". Chaves devem fechar comentários. Linha " + str(contador_linha) + ", coluna " + str(contador_coluna) + ".\n")
        else:
            print("Erro " + str(cod) + ". caractere inválido, linha " + str(contador_linha) + ", coluna " + str(contador_coluna) + ".\n")

def main():
        if not os.path.exists('fonte.txt'):
            print("Arquivo não encontrado.\n")
        else: 
            fonte = open('fonte.txt', 'r+')
            fonte.write("$")

            l = lista()
            ana = analisador()
            retorno_scanner = token()

            l.push('inicio', 'inicio')
            l.push('varinicio', 'varinicio')
            l.push('varfim', 'varfim')
            l.push('escreva', 'escreva')
            l.push('leia', 'leia')
            l.push('se', 'se')
            l.push('entao', 'entao')
            l.push('fimse', 'fimse')
            l.push('facaate', 'facaate')
            l.push('fimfaca', 'fimfaca')
            l.push('fim', 'fim')
            l.push('inteiro', 'inteiro')
            l.push('lit', 'lit')
            l.push('real', 'real')

            global contador_linha 
            global contador_coluna
            contador_linha = 0

            for line in fonte:
                contador_linha += 1
                contador_coluna = 0
                for word in line.split():
                    palavra = word
                    retorno_scanner = ana.scanner()
                    if(retorno_scanner == "Erro*"):
                        ana.erro(int(retorno_scanner[5:6]))     
                    else:
                        print("Classe: " + retorno_scanner.classe + ", lexema: " + retorno_scanner.lexema + ", tipo: " + retorno_scanner.tipo + ".\n")

if __name__ == '__main__':
    main()