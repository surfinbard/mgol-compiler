import os.path
import re

i = 0
contador_coluna = 0
aspas_palavra = 0
aspas_lidas = 0
flag_literal = 0
palavra = ""
palavra_anterior = ""
palavra_inicio = ""
caractere_inicio = ""
palavra_meio = ""
caractere_meio = ""
palavra_fim = ""
caractere_fim = ""
pre_aspas = ""
pos_aspas = ""
entre_aspas = ""
caracteres_especiais = False
caractere_no_comeco = False
caractere_no_fim = False
literal_comecou = False
flag_break = False

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

    def __init__(self, l, tabela_simbolos):
        self.l = l
        self.tabela_simbolos = tabela_simbolos

    def scanner(self, palavra, l, tabela_simbolos): 
        global i 
        i = 0
        global contador_coluna
        return self.q0(palavra, l, tabela_simbolos)

    def q0(self, palavra, l, tabela_simbolos):
        global contador_coluna
        global i
        contador_coluna += 1
        if palavra[i:i+1].isdigit(): 
            return self.q1(palavra, l, tabela_simbolos)
        elif palavra[i:i+1].isspace():
            return self.q0(palavra, l, tabela_simbolos)
        elif '"' == palavra[i:i+1]:
            return self.q7(palavra, l, tabela_simbolos)
        elif '{' == palavra[i:i+1]:
            return self.q9(palavra, l, tabela_simbolos)
        elif '<' == palavra[i:i+1]:
            return self.q13(palavra, l, tabela_simbolos)
        elif '=' == palavra[i:i+1]:
            return self.q17(palavra, l, tabela_simbolos)
        elif '>' == palavra[i:i+1]:    
            return self.q18(palavra, l, tabela_simbolos)
        elif '+' == palavra[i:i+1] or '-' == palavra[i:i+1] or '*' == palavra[i:i+1] or '/' == palavra[i:i+1]:
            return self.q20(palavra, l, tabela_simbolos)
        elif '(' == palavra[i:i+1]:
            return self.q21(palavra, l, tabela_simbolos)
        elif ')' == palavra[i:i+1]:
            return self.q22(palavra, l, tabela_simbolos)
        elif ';' == palavra[i:i+1]: 
            return self.q23(palavra, l, tabela_simbolos)
        elif ',' == palavra[i:i+1]:
            return self.q24(palavra, l, tabela_simbolos)
        elif 'e' == palavra[i:i+1]:
            return self.q27(palavra, l, tabela_simbolos)
        elif 'f' == palavra[i:i+1]:
            return self.q38(palavra, l, tabela_simbolos)
        elif 'i' == palavra[i:i+1]:
            return self.q53(palavra, l, tabela_simbolos)
        elif 'l' == palavra[i:i+1]:
            return self.q64(palavra, l, tabela_simbolos)
        elif 'r' == palavra[i:i+1]:
            return self.q70(palavra, l, tabela_simbolos)
        elif 'v' == palavra[i:i+1]:
            return self.q74(palavra, l, tabela_simbolos)
        elif 's' == palavra[i:i+1]:
            return self.q86(palavra, l, tabela_simbolos)
        elif palavra[i:i+1].isalpha():
            return self.q11(palavra, l, tabela_simbolos)
        elif '\\' == palavra[i:i+1]:
            return self.q26(palavra, l, tabela_simbolos)
        else: 
            return self.q25(1, palavra, l)


    def q1(self, palavra, l, tabela_simbolos): # token *num*
        global contador_coluna
        global i
        contador_coluna += 1 
        i += 1
        if palavra[i:i+1]:
            if palavra[i:i+1].isdigit():
                return self.q1(palavra, l, tabela_simbolos)
            elif '.' == palavra[i:i+1]:
                return self.q2(palavra, l, tabela_simbolos)
            elif 'e' == palavra[i:i+1] or 'E' == palavra[i:i+1]: 
                return self.q4(palavra, l, tabela_simbolos)
            else: 
                return self.q25(4, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('NUM', palavra)
            return self.l.procura_na_lista(palavra) 

    def q2(self, palavra, l, tabela_simbolos):  
        global contador_coluna
        global i
        contador_coluna += 1
        i += 1
        if palavra[i:i+1].isdigit():
            return self.q3(palavra, l, tabela_simbolos)
        else: 
            return self.q25(4, palavra, l)

    def q3(self, palavra, l, tabela_simbolos): # token *num*
        global contador_coluna
        global i
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if palavra[i:i+1].isdigit():
                return self.q3(palavra, l, tabela_simbolos)
            elif 'e' == palavra[i:i+1] or 'E' == palavra[i:i+1]: 
                return self.q4(palavra, l, tabela_simbolos)
            else: 
                return self.q25(4, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('NUM', palavra)
            return self.l.procura_na_lista(palavra) 

    def q4(self, palavra, l, tabela_simbolos):
        global contador_coluna
        global i
        contador_coluna += 1
        i += 1
        if palavra[i:i+1].isdigit():
            return self.q6(palavra, l, tabela_simbolos)
        elif '+' == palavra[i:i+1] or '-' == palavra[i:i+1]: 
            return self.q5(palavra, l, tabela_simbolos)
        else: 
            return self.q25(4, palavra, l)

    def q5(self, palavra, l, tabela_simbolos): 
        global contador_coluna
        global i
        contador_coluna += 1
        i += 1
        if palavra[i:i+1].isdigit():
            return self.q6(palavra, l, tabela_simbolos)
        else: 
            return self.q25(4, palavra, l)

    def q6(self, palavra, l, tabela_simbolos): # token *num*
        global contador_coluna
        global i
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if palavra[i:i+1].isdigit():
                return self.q6(palavra, l, tabela_simbolos)
            else: 
                return self.q25(4, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('NUM', palavra)
            return self.l.procura_na_lista(palavra) 

    def q7(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        while palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            if palavra[i:i+1] == '"':
                return self.q8(palavra, l, tabela_simbolos)
            return self.q7(palavra, l, tabela_simbolos)
        return self.q25(2, palavra, l)

    def q8(self, palavra, l, tabela_simbolos): # token *lit*
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            return self.q25(2, palavra, l)
        else: 
            if not self.l.procura_na_lista(palavra):
                l.push('lit', palavra)
            return self.l.procura_na_lista(palavra)

    def q9(self, palavra, l, tabela_simbolos): #Abre { comentário
        global i
        global contador_coluna
        while palavra[i:i+1]:
            contador_coluna += 1
            i += 1
            if palavra[i:i+1] == '}':
                return self.q10(palavra, l, tabela_simbolos)
        return self.q25(1, palavra, l)

    def q10(self, palavra, l, tabela_simbolos): # fecha } comentário
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            return self.q25(3, palavra, l)
        else: 
            return None

    def q11(self, palavra, l, tabela_simbolos): # reconhece *id*
        global i
        global contador_coluna
        contador_coluna += 1       
        i += 1
        if palavra[i:i+1]:
            if palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', palavra)
                tabela_simbolos.push('id', palavra)
            return self.l.procura_na_lista(palavra) 


    def q12(self, palavra, l, tabela_simbolos): # reconhece *EOF*
        global i
        contador_coluna += 1
        i += 1
        if palavra[i:i+1] == '$':
            if not self.l.procura_na_lista(palavra):
                l.push('EOF', '$')
            return self.l.procura_na_lista(palavra)
        else: 
            return self.q25(1, palavra, l)

    def q13(self, palavra, l, tabela_simbolos): # reconhece *<*
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if palavra[i:i+1] == '-':
                return self.q16(palavra, l, tabela_simbolos)
            elif palavra[i:i+1] == '=':
                return self.q15(palavra, l, tabela_simbolos)
            elif palavra[i:i+1] == '>':
                return self.q14(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('OPR', '<')
            return self.l.procura_na_lista(palavra)

    def q14(self, palavra, l, tabela_simbolos): # diferente <>
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            return self.q25(1, palavra, l)
        else: 
            if not self.l.procura_na_lista(palavra):
                l.push('OPR', '<>')
            return self.l.procura_na_lista(palavra)

    def q15(self, palavra, l, tabela_simbolos):  # menor igual <=
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            return self.q25(1, palavra, l)
        else: 
            if not self.l.procura_na_lista(palavra):
                l.push('OPR', '<=')
            return self.l.procura_na_lista(palavra)

    def q16(self, palavra, l, tabela_simbolos): # atribuicao <-
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            return self.q25(1, palavra, l)
        else: 
            if not self.l.procura_na_lista(palavra):
                l.push('RCB', '<-')
            return self.l.procura_na_lista(palavra)

    def q17(self, palavra, l, tabela_simbolos): # =
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            return self.q25(1, palavra, l)
        else: 
            if not self.l.procura_na_lista(palavra):
                l.push('OPR', '=')
            return self.l.procura_na_lista(palavra)

    def q18(self, palavra, l, tabela_simbolos): # reconhece *>
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if palavra[i:i+1] == '=':
                return self.q19(palavra, l, tabela_simbolos)
            else:
                return self.q25(1, palavra, l)
        else: 
            if not self.l.procura_na_lista(palavra):
                l.push('OPR', '>')
            return self.l.procura_na_lista(palavra)

    def q19(self, palavra, l, tabela_simbolos): # maior igual >=
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            return self.q25(1, palavra, l)
        else: 
            if not self.l.procura_na_lista(palavra):
                l.push('OPR', '>=')
            return self.l.procura_na_lista(palavra)

    def q20(self, palavra, l, tabela_simbolos): # operadores + - *  /
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            return self.q25(1, palavra, l)
        else: 
            if not self.l.procura_na_lista(palavra):
                l.push('OPM', palavra)
            return self.l.procura_na_lista(palavra)

    def q21(self, palavra, l, tabela_simbolos): # (
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('AB_P', '(')
            return self.l.procura_na_lista(palavra)

    def q22(self, palavra, l, tabela_simbolos): # )
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('FC_P', ')')
            return self.l.procura_na_lista(palavra)

    def q23(self, palavra, l, tabela_simbolos): # ;
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            return self.q25(1, palavra, l)
        else: 
            if not self.l.procura_na_lista(palavra):
                l.push('PT_V', ';')
            return self.l.procura_na_lista(palavra)

    def q24(self, palavra, l, tabela_simbolos): # ,
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            return self.q25(1, palavra, l)
        else: 
            if not self.l.procura_na_lista(palavra):
                l.push('VIR', ',')
            return self.l.procura_na_lista(palavra)

    def q25(self, cod, palavra, l): # erro
        if not self.l.procura_na_lista(palavra):
            l.push('ERRO'+str(cod), palavra)
        return self.l.procura_na_lista(palavra)

    def q26(self, palavra, l, tabela_simbolos): # \t \s \n
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'n' == palavra[i:i+1] or 's' == palavra[i:i+1] or 't' == palavra[i:i+1]:
                return None 
            else:
                return self.q25(1, palavra, l)
        else:
            return self.q25(1, palavra, l)

    def q27(self, palavra, l, tabela_simbolos): 
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'n' == palavra[i:i+1]:
                return self.q28(palavra, l, tabela_simbolos)
            elif 's' == palavra[i:i+1]:
                return self.q32(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'e')
                tabela_simbolos.push('id', 'e')
            return self.l.procura_na_lista(palavra)

    def q28(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 't' == palavra[i:i+1]:
                return self.q29(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'en')
                tabela_simbolos.push('id', 'en')
            return self.l.procura_na_lista(palavra)

    def q29(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'a' == palavra[i:i+1]:
                return self.q30(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'ent')
                tabela_simbolos.push('id', 'ent')
            return self.l.procura_na_lista(palavra)

    def q30(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'o' == palavra[i:i+1]:
                return self.q31(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'enta')
                tabela_simbolos.push('id', 'enta')
            return self.l.procura_na_lista(palavra)

    def q31(self, palavra, l, tabela_simbolos): # reconhece entao
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if palavra[i:i+1].isalpha() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('entao', 'entao')
            return self.l.procura_na_lista(palavra)

    def q32(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'c' == palavra[i:i+1]:
                return self.q33(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'es')
                tabela_simbolos.push('id', 'es')
            return self.l.procura_na_lista(palavra)

    def q33(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'r' == palavra[i:i+1]:
                return self.q34(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'esc')
                tabela_simbolos.push('id', 'esc')
            return self.l.procura_na_lista(palavra)

    def q34(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'e' == palavra[i:i+1]:
                return self.q35(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'escr')
                tabela_simbolos.push('id', 'escr')
            return self.l.procura_na_lista(palavra)

    def q35(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'v' == palavra[i:i+1]: 
                return self.q36(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'escre')
                tabela_simbolos.push('id', 'escre')
            return self.l.procura_na_lista(palavra)

    def q36(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'a' == palavra[i:i+1]: 
                return self.q37(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'escrev')
                tabela_simbolos.push('id', 'escrev')
            return self.l.procura_na_lista(palavra)

    def q37(self, palavra, l, tabela_simbolos): #reconhece escreva
        global contador_coluna
        global i
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if palavra[i:i+1].isalpha() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('escreva', 'escreva')
            return self.l.procura_na_lista(palavra)

    def q38(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'a' == palavra[i:i+1]: 
                return self.q39(palavra, l, tabela_simbolos)
            elif 'i' == palavra[i:i+1]:  
                return self.q45(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'f')
                tabela_simbolos.push('id', 'f')
            return self.l.procura_na_lista(palavra)

    def q39(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'c' == palavra[i:i+1]:
                return self.q40(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'fa')
                tabela_simbolos.push('id', 'fa')
            return self.l.procura_na_lista(palavra)

    def q40(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'a' == palavra[i:i+1]:
                return self.q41(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'fac')
                tabela_simbolos.push('id', 'fac')
            return self.l.procura_na_lista(palavra)

    def q41(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'a' == palavra[i:i+1]:
                return self.q42(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'faca')
            return self.l.procura_na_lista(palavra)

    def q42(self, palavra, l, tabela_simbolos):
        global contador_coluna
        global i
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 't' == palavra[i:i+1]:
                return self.q43(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'facaa')
                tabela_simbolos.push('id', 'facaa')
            return self.l.procura_na_lista(palavra)

    def q43(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'e' == palavra[i:i+1]:
                return self.q44(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'facaat')
                tabela_simbolos.push('id', 'facaat')
            return self.l.procura_na_lista(palavra)

    def q44(self, palavra, l, tabela_simbolos): # reconhece *facaate
        global contador_coluna
        global i
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if palavra[i:i+1].isalpha() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('facaate', 'facaate')
            return self.l.procura_na_lista(palavra)

    def q45(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'm' == palavra[i:i+1]:   
                return self.q46(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'fi')
                tabela_simbolos.push('id', 'fi')
            return self.l.procura_na_lista(palavra)

    def q46(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'f' == palavra[i:i+1]: 
                return self.q47(palavra, l, tabela_simbolos)
            elif 's' == palavra[i:i+1]:
                return self.q51(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('fim', 'fim')
            return self.l.procura_na_lista(palavra)

    def q47(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'a' == palavra[i:i+1]:
                return self.q48(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'fimf')
                tabela_simbolos.push('id', 'fimf')
            return self.l.procura_na_lista(palavra)

    def q48(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'c' == palavra[i:i+1]:
                return self.q49(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'fimfa')
                tabela_simbolos.push('id', 'fimfa')
            return self.l.procura_na_lista(palavra)

    def q49(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'a' == palavra[i:i+1]:
                return self.q50(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'fimfac')
                tabela_simbolos.push('id', 'fimfac')
            return self.l.procura_na_lista(palavra)

    def q50(self, palavra, l, tabela_simbolos): # reconhece *fimfaca*
        global contador_coluna
        global i
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if palavra[i:i+1].isalpha() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('fimfaca', 'fimfaca')
            return self.l.procura_na_lista(palavra)

    def q51(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'e' == palavra[i:i+1]:
                return self.q52(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'fims')
                tabela_simbolos.push('id', 'fims')
            return self.l.procura_na_lista(palavra)

    def q52(self, palavra, l, tabela_simbolos):  # reconhece *fimse*
        global contador_coluna
        global i
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if palavra[i:i+1].isalpha() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('fimse', 'fimse')
            return self.l.procura_na_lista(palavra) 

    def q53(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'n' == palavra[i:i+1]:
                return self.q54(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'i')
                tabela_simbolos.push('id', 'i')
            return self.l.procura_na_lista(palavra)

    def q54(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'i' == palavra[i:i+1]:
                return self.q55(palavra, l, tabela_simbolos)
            if 't' == palavra[i:i+1]:
                return self.q59(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'in')
                tabela_simbolos.push('id', 'in')
            return self.l.procura_na_lista(palavra)

    def q55(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'c' == palavra[i:i+1]:
                return self.q56(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'ini')
                tabela_simbolos.push('id', 'ini')
            return self.l.procura_na_lista(palavra)

    def q56(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'i' == palavra[i:i+1]:
                return self.q57(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'inic')
                tabela_simbolos.push('id', 'inic')
            return self.l.procura_na_lista(palavra)

    def q57(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'o' == palavra[i:i+1]:    
                return self.q58(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'inici')
                tabela_simbolos.push('id', "inici")
            return self.l.procura_na_lista(palavra)

    def q58(self, palavra, l, tabela_simbolos):  # reconhece *inicio*
        global contador_coluna
        contador_coluna += 1
        if palavra[i:i+1]:
            if palavra[i:i+1].isalpha() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('inicio', 'inicio')
            return self.l.procura_na_lista(palavra)

    def q59(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'e' == palavra[i:i+1]:    
                return self.q60(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'int')
                tabela_simbolos.push('id', 'int')
            return self.l.procura_na_lista(palavra)

    def q60(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'i' == palavra[i:i+1]:
                return self.q61(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'inte')
                tabela_simbolos.push('id', 'inte')
            return self.l.procura_na_lista(palavra)

    def q61(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'r' == palavra[i:i+1]:
                return self.q62(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'intei')
                tabela_simbolos.push('id', 'intei')
            return self.l.procura_na_lista(palavra)

    def q62(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'o' == palavra[i:i+1]:
                return self.q63(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'inteir')
                tabela_simbolos.push('id', 'inteir')
            return self.l.procura_na_lista(palavra)

    def q63(self, palavra, l, tabela_simbolos):  # reconhece *inteiro*
        global i
        global contador_coluna
        contador_coluna += 1
        if palavra[i:i+1]:
            if palavra[i:i+1].isalpha() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('inteiro', 'inteiro')
            return self.l.procura_na_lista(palavra) 

    def q64(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'e' == palavra[i:i+1]:  
                return self.q65(palavra, l, tabela_simbolos)
            elif 'i' == palavra[i:i+1]:   
                return self.q68(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'l')
                tabela_simbolos.push('id', 'l')
            return self.l.procura_na_lista(palavra)

    def q65(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'i' == palavra[i:i+1]: 
                return self.q66(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'le')
                tabela_simbolos.push('id', 'le')
            return self.l.procura_na_lista(palavra)

    def q66(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'a' == palavra[i:i+1]:
                return self.q67(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'lei')
                tabela_simbolos.push('id', 'lei')
            return self.l.procura_na_lista(palavra)

    def q67(self, palavra, l, tabela_simbolos): # reconhece *leia*
        global i
        global contador_coluna
        contador_coluna += 1
        if palavra[i:i+1]:
            if palavra[i:i+1].isalpha() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('leia', 'leia')
            return self.l.procura_na_lista(palavra)

    def q68(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 't' == palavra[i:i+1]:
                return self.q69(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'li')
                tabela_simbolos.push('id', 'li')
            return self.l.procura_na_lista(palavra)

    def q69(self, palavra, l, tabela_simbolos): # reconhece *lit*
        global i
        global contador_coluna
        contador_coluna += 1
        if palavra[i:i+1]:
            if palavra[i:i+1].isalpha() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('lit', 'lit')
            return self.l.procura_na_lista(palavra)

    def q70(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'e' == palavra[i:i+1]: 
                return self.q71(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'r')
                tabela_simbolos.push('id', 'r')
            return self.l.procura_na_lista(palavra)

    def q71(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'a' == palavra[i:i+1]:    
                return self.q72(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 're')
                tabela_simbolos.push('id', 're')
            return self.l.procura_na_lista(palavra)

    def q72(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'l' == palavra[i:i+1]:
                return self.q73(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isdigit() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_': 
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'rea')
                tabela_simbolos.push('id', 'rea')
            return self.l.procura_na_lista(palavra)

    def q73(self, palavra, l, tabela_simbolos): # reconhece *real*
        global i
        global contador_coluna
        contador_coluna += 1
        if palavra[i:i+1]:
            if palavra[i:i+1].isalpha() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('real', 'real')
            return self.l.procura_na_lista(palavra)

    def q74(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1        
        if palavra[i:i+1]:
            if 'a' == palavra[i:i+1]:  
                return self.q75(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isalpha() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'v')
                tabela_simbolos.push('id', 'v')
            return self.l.procura_na_lista(palavra)            

    def q75(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'r' == palavra[i:i+1]: 
                return self.q76(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isalpha() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'va')
                tabela_simbolos.push('id', 'va')
            return self.l.procura_na_lista(palavra)  

    def q76(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'i' == palavra[i:i+1]: 
                return self.q77(palavra, l, tabela_simbolos)
            elif 'f' == palavra[i:i+1]:  
                return self.q83(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isalpha() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'var')
                tabela_simbolos.push('id', 'var')
            return self.l.procura_na_lista(palavra)  

    def q77(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'n' == palavra[i:i+1]:   
                return self.q78(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isalpha() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'vari')
                tabela_simbolos.push('id', 'vari')
            return self.l.procura_na_lista(palavra)  

    def q78(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'i' == palavra[i:i+1]:  
                return self.q79(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isalpha() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'varin')
                tabela_simbolos.push('id', 'varin')
            return self.l.procura_na_lista(palavra)

    def q79(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'c' == palavra[i:i+1]: 
                return self.q80(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isalpha() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'varini')
                tabela_simbolos.push('id', 'varini')
            return self.l.procura_na_lista(palavra)

    def q80(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'i' == palavra[i:i+1]:
                return self.q81(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isalpha() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'varinic')
                tabela_simbolos.push('id', 'varinic')
            return self.l.procura_na_lista(palavra)

    def q81(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'o' == palavra[i:i+1]:
                return self.q82(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isalpha() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'varinici')
                tabela_simbolos.push('id', 'varinici')
            return self.l.procura_na_lista(palavra)

    def q82(self, palavra, l, tabela_simbolos): # reconhece o estado *varinicio*
        global contador_coluna
        contador_coluna += 1
        if palavra[i:i+1]:
            if palavra[i:i+1].isalpha() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('varinicio', 'varinicio')
            return self.l.procura_na_lista(palavra)

    def q83(self, palavra, l, tabela_simbolos):
        global contador_coluna
        global i
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'i' == palavra[i:i+1]:    
                return self.q84(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isalpha() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'varf')
                tabela_simbolos.push('id', 'varf')
            return self.l.procura_na_lista(palavra)

    def q84(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'm' == palavra[i:i+1]:   
                return self.q85(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isalpha() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 'varfi')
                tabela_simbolos.push('id', 'varfi')
            return self.l.procura_na_lista(palavra)

    def q85(self, palavra, l, tabela_simbolos): # reconhece o estado *varfim*
        global i
        global contador_coluna
        contador_coluna += 1
        if palavra[i:i+1]:
            if palavra[i:i+1].isalpha() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('varfim', 'varfim')
            return self.l.procura_na_lista(palavra)

    def q86(self, palavra, l, tabela_simbolos):
        global i
        global contador_coluna
        contador_coluna += 1
        i += 1
        if palavra[i:i+1]:
            if 'e' == palavra[i:i+1]:  
                return self.q87(palavra, l, tabela_simbolos)
            elif palavra[i:i+1].isalpha() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('id', 's')
                tabela_simbolos.push('id', 's')
            return self.l.procura_na_lista(palavra)

    def q87(self, palavra, l, tabela_simbolos): # reconhece o estado *se*
        global i
        global contador_coluna
        contador_coluna += 1
        if palavra[i:i+1]:
            if palavra[i:i+1].isalpha() or palavra[i:i+1].isalpha() or palavra[i:i+1] == '_':
                return self.q11(palavra, l, tabela_simbolos)
            else: 
                return self.q25(1, palavra, l)
        else:
            if not self.l.procura_na_lista(palavra):
                l.push('se', 'se')
            return self.l.procura_na_lista(palavra)

    def erro(self, cod):
        if(cod==2):
            print("Erro " + str(cod) + ". Aspas vêm ao final de constantes literais. Linha " + str(contador_linha) + ", coluna " + str(contador_coluna) + ".")
        elif(cod==3):
            print("Erro " + str(cod) + ". Chaves devem fechar comentários. Linha " + str(contador_linha) + ", coluna " + str(contador_coluna) + ".")
        elif(cod==4):
            print("Erro " + str(cod) + ". Formato numérico permitido: D(.D)(e|E(+|-)D). Linha " + str(contador_linha) + ", coluna " + str(contador_coluna) + ".")
        elif(cod==5):
            print("Erro " + str(cod) + ". Todo comentário deve ser fechado! Linha " + str(contador_linha) + ", coluna " + str(contador_coluna) + ".")
        elif(cod==6):
            print("Erro " + str(cod) + ". Verifique a ordem das chaves e aspas. Linha " + str(contador_linha) + ", coluna " + str(contador_coluna) + ".")
        else:
            print("Erro " + str(cod) + ". caractere inválido, linha " + str(contador_linha) + ", coluna " + str(contador_coluna) + ".")

    def processa_lexemas(self, palavra, l, tabela_simbolos, retorno_scanner, ana):

        retorno_scanner = ana.scanner(palavra, l, tabela_simbolos) 
        if retorno_scanner != None:
            if str(retorno_scanner.classe)[0:4] == "ERRO":
                print("Classe: " + retorno_scanner.classe + ", lexema: " + retorno_scanner.lexema + ", tipo: " + retorno_scanner.tipo + ".")
                cod = int(retorno_scanner.classe[4:5])
                ana.erro(cod)     
            else:
                print("Classe: " + retorno_scanner.classe + ", lexema: " + retorno_scanner.lexema + ", tipo: " + retorno_scanner.tipo + ".")


    def trata_lexemas(self, palavra, tabela_simbolos, l, ana):

        global caractere_no_comeco
        global caractere_no_fim
        global caracteres_especiais
        global caractere_inicio
        global caractere_meio
        global caractere_fim
        global palavra_anterior
        global palavra_inicio
        global palavra_meio
        global palavra_fim
        global pre_aspas
        global pos_aspas
        global entre_aspas
        global literal_comecou
        global flag_literal
        lista_especiais = [';', '=',  ',',  '(',  ')',  '+',  '-',  '*',  '/',  '>',  '<']

        if caracteres_especiais == False:
            retorno_scanner = ana.scanner(palavra, l, tabela_simbolos)
            self.processa_lexemas(palavra, l, tabela_simbolos, retorno_scanner, ana)
        else:
            if palavra_anterior != "":
                retorno_scanner = ana.scanner(palavra_anterior, l, tabela_simbolos) 
                self.processa_lexemas(palavra_anterior, l, tabela_simbolos, retorno_scanner, ana)
                retorno_scanner = ana.scanner(caractere_meio, l, tabela_simbolos)
                self.processa_lexemas(caractere_meio, l, tabela_simbolos, retorno_scanner, ana)     
                retorno_scanner = ana.scanner(palavra_meio, l, tabela_simbolos) 
                self.processa_lexemas(palavra_meio, l, tabela_simbolos, retorno_scanner, ana)
            elif caractere_no_comeco == True: 
                retorno_scanner = ana.scanner(caractere_inicio, l, tabela_simbolos)
                self.processa_lexemas(caractere_inicio, l, tabela_simbolos, retorno_scanner, ana)
                if not any(elemento in palavra_inicio for elemento in lista_especiais):
                    retorno_scanner = ana.scanner(palavra_inicio, l, tabela_simbolos) 
                    self.processa_lexemas(palavra_inicio, l, tabela_simbolos, retorno_scanner, ana) 
                else:
                    flag_break = True
                    ana.separa_lexemas(palavra_inicio, tabela_simbolos, l, ana, flag_literal)

            elif caractere_no_fim == True: 
                retorno_scanner = ana.scanner(palavra_fim, l, tabela_simbolos) 
                self.processa_lexemas(palavra_fim, l, tabela_simbolos, retorno_scanner, ana)
                retorno_scanner = ana.scanner(caractere_fim, l, tabela_simbolos)
                self.processa_lexemas(caractere_fim, l, tabela_simbolos, retorno_scanner, ana)   
            else:
                if pre_aspas != "":
                    retorno_scanner = ana.scanner(pre_aspas, l, tabela_simbolos) 
                    self.processa_lexemas(pre_aspas, l, tabela_simbolos, retorno_scanner, ana)
                retorno_scanner = ana.scanner(entre_aspas, l, tabela_simbolos)
                self.processa_lexemas(entre_aspas, l, tabela_simbolos, retorno_scanner, ana)  
                if pos_aspas != "":
                    retorno_scanner = ana.scanner(pos_aspas, l, tabela_simbolos) 
                    self.processa_lexemas(pos_aspas, l, tabela_simbolos, retorno_scanner, ana)

    def separa_lexemas(self, palavra, tabela_simbolos, l, ana, flag_literal):

        global caractere_no_comeco
        global caractere_no_fim
        global caracteres_especiais
        global caractere_inicio
        global caractere_meio
        global caractere_fim
        global palavra_anterior
        global palavra_inicio
        global palavra_meio
        global palavra_fim
        global aspas_palavra
        global pre_aspas
        global posaspas
        global entre_aspas
        lista_especiais = [';', '=',  ',',  '(',  ')',  '+',  '-',  '*',  '/',  '>',  '<']
        lista_especiais_duplos = ['<-', '<=', '<>', '>=']
        index = 0
        flag_literal = 0
        contador_especiais = 0

        if any(element in palavra for element in lista_especiais_duplos):
            contador_especiais += 1
       
        for item in palavra:
            index += 1
            if (item in lista_especiais and not ((item == '<' and palavra[index] == '-')
                                              or (item == '<' and palavra[index] == '=')
                                              or (item == '<' and palavra[index] == '>')
                                              or (item == '>' and palavra[index] == '='))):
                contador_especiais += 1
            
        index = 0
        #separa lexemas colados quando aplicável    
        for posicao, caractere in enumerate(palavra):
            caractere_no_comeco = False
            caractere_no_fim = False
            caracteres_especiais = False
            #usaremos index para acessar indices seguintes
            index += 1

         #especiais de um caractere só
            if contador_especiais > 0:

                #"\N TA AQUI"
                
                if (caractere == ";" or caractere == "=" or caractere == "," or caractere == "(" or caractere == ")"
                or caractere == "+" or caractere == "-" or caractere == "*" or caractere == "/" or 
                (caractere == '<' and palavra[index] != '-' and palavra[index] != '=' and palavra[index] != '>') or 
                (caractere == '>' and palavra[index] != '=')):

                    caracteres_especiais = True
                    contador_especiais -= 1
                    
                    if palavra[0] == caractere:
                        if flag_break == True:
                            break
                        caractere_inicio = palavra[0]
                        palavra_inicio = palavra[1:]
                        caractere_no_comeco = True
                        palavra_anterior = ""
                        ana.trata_lexemas(palavra, tabela_simbolos, l, ana)
                    elif len(palavra) > index:
                        if flag_break == True:
                            break
                        for caractere in palavra:
                            if palavra[posicao] == caractere:
                                palavra_anterior = palavra[0:posicao]
                                caractere_meio = palavra[posicao]
                                palavra_meio = palavra[posicao+1:] 
                                ana.trata_lexemas(palavra, tabela_simbolos, l, ana)
                    elif palavra[-1] == caractere: 
                        caractere_fim = palavra[-1]
                        palavra_fim = palavra[:-2]
                        caractere_no_fim = True
                        palavra_anterior = ""
                        ana.trata_lexemas(palavra, tabela_simbolos, l, ana)

                    contador_especiais -= 1

                elif ((caractere == '<' and palavra[index] == '-')
                or (caractere == '<' and palavra[index] == '=')
                or (caractere == '<' and palavra[index] == '>')
                or (caractere == '>' and palavra[index] == '=')):
                                    
                    caracteres_especiais = True 

                    if palavra[0] == caractere:
                        if flag_break == True:
                            break
                        caractere_inicio = palavra[0:2]
                        palavra_inicio = palavra[3:]
                        caractere_no_comeco = True
                        ana.trata_lexemas(palavra, tabela_simbolos, l, ana)
                    elif len(palavra) > index:
                        if flag_break == True:
                            break
                        for caractere in palavra:
                            if palavra[posicao] == caractere:
                                palavra_anterior = palavra[:posicao]
                                caractere_meio = palavra[posicao:posicao+2]
                                palavra_meio = palavra[posicao+2:] 
                                ana.trata_lexemas(palavra, tabela_simbolos, l, ana)
                    elif palavra[-2] == caractere:
                        caractere_fim = palavra[-2:]
                        palavra_fim = palavra[:-2]
                        caractere_no_fim = True 
                        ana.trata_lexemas(palavra, tabela_simbolos, l, ana)

                    contador_especiais -= 1

            else:
                if caractere == '"':
                    if palavra[0] == caractere and palavra[-1] == caractere:
                        caracteres_especiais = True
                        entre_aspas = palavra[:]
                        palavra_anterior = ""
                        flag_literal = 1
                        ana.trata_lexemas(palavra, tabela_simbolos, l, ana)
                    elif  aspas_lidas %2 == 0: #inicio do literal
                        caracteres_especiais = True
                        if palavra[0] != caractere:
                            pre_aspas = palavra[:index-1]
                        entre_aspas = palavra[index-1:]
                        palavra_anterior = ""
                        flag_literal = 0
                    elif aspas_lidas %2 != 0: #fim literal
                        caracteres_especiais = True
                        entre_aspas = entre_aspas[:index]
                        if palavra[-1] != caractere:
                            pos_aspas = palavra[index:]
                        palavra_anterior = ""
                        flag_literal = 1
                        ana.trata_lexemas(palavra, tabela_simbolos, l, ana)

        #fim da separação

        if caracteres_especiais == False:
            ana.trata_lexemas(palavra, tabela_simbolos, l, ana)

def main():
        if not os.path.exists('fonte.txt'):
            print("Arquivo não encontrado.\n")
        else: 
            fonte = open('fonte.txt', 'r+')
            fonte.write("$")

            l = lista()
            tabela_simbolos = lista()
            ana = analisador(l, tabela_simbolos)
            retorno_scanner = token()

            tabela_simbolos.push('inicio', 'inicio')
            tabela_simbolos.push('varinicio', 'varinicio')
            tabela_simbolos.push('varfim', 'varfim')
            tabela_simbolos.push('escreva', 'escreva')
            tabela_simbolos.push('leia', 'leia')
            tabela_simbolos.push('se', 'se')
            tabela_simbolos.push('entao', 'entao')
            tabela_simbolos.push('fimse', 'fimse')
            tabela_simbolos.push('facaate', 'facaate')
            tabela_simbolos.push('fimfaca', 'fimfaca')
            tabela_simbolos.push('fim', 'fim')
            tabela_simbolos.push('inteiro', 'inteiro')
            tabela_simbolos.push('lit', 'lit')
            tabela_simbolos.push('real', 'real')

            global contador_linha 
            global contador_coluna
            global aspas_palavra
            global aspas_lidas
            global flag_literal
            contador_linha = 0
            indice = 0

            print('\n')
            for line in fonte:
                contador_linha += 1
                contador_coluna = 0
                while (line[contador_coluna] == " "):
                    contador_coluna += 1

                global literal_comecou
                literal_comecou = False
                comentario_comecou = False
                char_index = 0
                aspas_linha = 0
                aspas_lidas = 0
                chaves_abertura = 0
                chaves_fechameto = 0
                posicao_aspas = []
                posicao_chaves_abertura = []
                posicao_chaves_fechamento = []   
                literal_com_espacos = []
                comentario_com_espacos = []
                tupla = ()


                for item in line:
                    if item == '"':
                        posicao_aspas.append(char_index)
                        aspas_linha += 1  
                    elif item == '{':
                        posicao_chaves_abertura.append(char_index)
                        chaves_abertura += 1  
                    elif item == '}':
                        posicao_chaves_fechamento.append(char_index)
                        chaves_fechameto += 1
                    char_index += 1

                linha = line.split()

                for word in linha:
                    palavra = word

                    if aspas_linha == 0 and chaves_abertura == 0 and chaves_fechameto == 0:

                        ana.separa_lexemas(palavra, tabela_simbolos, l, ana, flag_literal)

                    #tratamento de casos com aspas ou chaves a seguir. pode haver so aspas, so chaves ou os dois
                    #caso haja aspas/chaves, é preciso verificar se o número é par.

                    elif aspas_linha != 0 and chaves_abertura == 0 and chaves_fechameto == 0:

                        if(aspas_linha%2!=0):
                            palavra = "".join(line)
                            retorno_scanner = ana.q7(palavra, l, tabela_simbolos)
                            print("Classe: " + retorno_scanner.classe + ", lexema: " + retorno_scanner.lexema + ", tipo: " + retorno_scanner.tipo + ".")
                            ana.erro(2)   
                            break          
                        else:

                            def inicio_literal(palavra):
                                literal_com_espacos.append(palavra)

                            def palavra_sem_aspas(palavra):
                                if literal_comecou == True:
                                    literal_com_espacos.append(palavra)
                                else:
                                    ana.separa_lexemas(palavra, tabela_simbolos, l, ana, flag_literal)

                            def fim_literal(palavra):
                                literal_com_espacos.append(palavra)
                                tupla = tuple(literal_com_espacos)
                                palavra = " ".join(tupla)
                                ana.separa_lexemas(palavra, tabela_simbolos, l, ana, flag_literal)

                            aspas_palavra = 0
                            for item in palavra:
                                if item == '"':
                                    aspas_palavra += 1
                            
                            if aspas_palavra == 0:
                                palavra_sem_aspas(palavra)
                            elif aspas_palavra %2 == 0: #um ou mais lit dentro da palavra
                                ana.separa_lexemas(palavra, tabela_simbolos, l, ana, flag_literal)
                            elif aspas_palavra == 1 and aspas_lidas %2 == 0: #inicio de literal (lemos numero par  de aspas ate aqui)
                                literal_comecou = True
                                inicio_literal(palavra)
                                aspas_lidas += 1
                            elif aspas_palavra == 1 and aspas_lidas %2 != 0: #fim de literal (lemos numero impar de aspas ate aqui)
                                fim_literal(palavra)
                                aspas_lidas += 1                                
                                literal_comecou = False

                    elif aspas_linha == 0 and (chaves_abertura != 0 or chaves_fechameto != 0):

                        if(chaves_abertura != chaves_fechameto):
                            palavra = "".join(line)
                            retorno_scanner = ana.q9(palavra, l, tabela_simbolos)
                            print("Classe: " + retorno_scanner.classe + ", lexema: " + retorno_scanner.lexema + ", tipo: " + retorno_scanner.tipo + ".")
                            ana.erro(5)   
                            break 
                        else:      
                            def inicio_comentario(palavra):
                                comentario_com_espacos.append(palavra)

                            def palavra_sem_chaves(palavra):
                                if comentario_comecou == True:
                                    comentario_com_espacos.append(palavra)
                                else:
                                    ana.separa_lexemas(palavra, tabela_simbolos, l, ana, flag_literal)

                            def fim_comentario(palavra):
                                comentario_com_espacos.append(palavra)
                                tupla = tuple(comentario_com_espacos)
                                palavra = " ".join(tupla)
                                ana.separa_lexemas(palavra, tabela_simbolos, l, ana, flag_literal)

                            if palavra[0] == '{' and palavra[-1] == '}':
                                ana.separa_lexemas(palavra, tabela_simbolos, l, ana, flag_literal)
                            elif palavra[0] == '{' and palavra[-1] != '}':
                                comentario_comecou = True
                                inicio_comentario(palavra)
                            elif palavra[0] != '{' and palavra[-1] == '}':
                                fim_comentario(palavra)
                                comentario_comecou = False
                            else:
                                if palavra[0] != '{' and palavra[-1] != '}':
                                    palavra_sem_chaves(palavra)

                                    
                            if aspas_palavra == 0:
                                palavra_sem_aspas(palavra)
                            elif aspas_palavra %2 == 0: #um ou mais lit dentro da palavra
                                aspas_lidas += 2
                                ana.separa_lexemas(palavra, tabela_simbolos, l, ana, flag_literal)
                            elif aspas_palavra == 1 and aspas_lidas %2 == 0: #inicio de literal (lemos numero par  de aspas ate aqui)
                                literal_comecou = True
                                aspas_lidas += 1
                                inicio_literal(palavra)
                            elif aspas_palavra == 1 and aspas_lidas %2 != 0: #fim de literal (lemos numero impar de aspas ate aqui)
                                aspas_lidas += 1
                                fim_literal(palavra)
                                literal_comecou = False
                    else:

                        if(aspas_linha%2!=0):
                            palavra = "".join(line)
                            retorno_scanner = ana.q7(palavra, l, tabela_simbolos)
                            print("Classe: " + retorno_scanner.classe + ", lexema: " + retorno_scanner.lexema + ", tipo: " + retorno_scanner.tipo + ".")
                            ana.erro(2)   
                            break     
                        if(chaves_abertura != chaves_fechameto):
                            palavra = "".join(line)
                            retorno_scanner = ana.q9(palavra, l, tabela_simbolos)
                            print("Classe: " + retorno_scanner.classe + ", lexema: " + retorno_scanner.lexema + ", tipo: " + retorno_scanner.tipo + ".")
                            ana.erro(5)   
                            break 

                        def inicio_literal(palavra):
                            literal_com_espacos.append(palavra)

                        def fim_literal(palavra):
                            literal_com_espacos.append(palavra)
                            tupla = tuple(literal_com_espacos)
                            palavra = " ".join(tupla)
                            ana.separa_lexemas(palavra, tabela_simbolos, l, ana, flag_literal)

                        def palavra_solta(palavra):
                            if literal_comecou == True:
                                literal_com_espacos.append(palavra)
                            elif comentario_comecou == True:
                                comentario_com_espacos.append(palavra)
                            else:
                                ana.separa_lexemas(palavra, tabela_simbolos, l, ana, flag_literal)
                        
                        def inicio_comentario(palavra):
                            comentario_com_espacos.append(palavra)

                        def fim_comentario(palavra):
                            comentario_com_espacos.append(palavra)
                            tupla = tuple(comentario_com_espacos)
                            palavra = " ".join(tupla)
                            ana.separa_lexemas(palavra, tabela_simbolos, l, ana, flag_literal)

                        if palavra[0] == '{' and palavra[-1] == '}':
                            ana.separa_lexemas(palavra, tabela_simbolos, l, ana, flag_literal)
                        elif palavra[0] == '"' and palavra[-1] == '"':
                            ana.separa_lexemas(palavra, tabela_simbolos, l, ana, flag_literal)
                        elif palavra[0] == '{' and palavra[-1] != '"':
                            comentario_comecou = True
                            inicio_comentario(palavra)
                        elif palavra[0] != '{' and palavra[-1] == '}' and palavra[0] != '"':
                            fim_comentario(palavra)
                            comentario_comecou = False
                        elif palavra[0] != '{' and palavra[-1] != '}' and palavra[0] != '"' and palavra[-1] != '"':
                            palavra_solta(palavra)
                        elif palavra[0] == '"' and palavra[-1] != '"' and palavra[-1] != '}':
                            literal_comecou = True
                            inicio_literal(palavra)
                        elif palavra[0] != '"' and palavra[-1] == '"' and palavra[0] != '{':
                            fim_literal(palavra)
                            literal_comecou = False

if __name__ == '__main__':
    main()