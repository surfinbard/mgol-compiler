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
flag = False

i = 0
contador_coluna = 0
contador_linha = 0
j = 0
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

    def __init__(self, l, tabela_simbolos):
        self.l = l
        self.tabela_simbolos = tabela_simbolos


    def scanner(self, arquivo_fonte, l, tabela_simbolos): 
        global j 
        global contador_coluna
        j = contador_coluna
        return self.q0 (arquivo_fonte, l, tabela_simbolos)

    def Operadores(self, arquivo_fonte): #verifica se é operador
        global contador_coluna
        operadores = "= + - * / ! > <"
        if arquivo_fonte[contador_coluna] in operadores:
            return True
        return False

    def Delimitadores(self, arquivo_fonte):#verifica se é delimitador
        global contador_coluna
        operadores = "; , ( ) { } [ ]"
        if arquivo_fonte[contador_coluna] in operadores:
            return True
        return False
    def Delimitadores_ABP(self, arquivo_fonte):#verifica se é delimitador para abra parênteses
        global contador_coluna
        operadores = "( ) { } [ ]"
        if arquivo_fonte[contador_coluna] in operadores:
            return True
        return False
    def q0(self, arquivo_fonte, l, tabela_simbolos):
        global contador_coluna
        global j

        if arquivo_fonte[contador_coluna].isdigit(): 
            return self.q1(arquivo_fonte, l, tabela_simbolos)
        elif '"' == arquivo_fonte[contador_coluna]:
            return self.q7(arquivo_fonte, l, tabela_simbolos)
        elif '{' == arquivo_fonte[contador_coluna]:
            return self.q9(arquivo_fonte, l, tabela_simbolos)
        elif '<' == arquivo_fonte[contador_coluna]:
            return self.q12(arquivo_fonte, l, tabela_simbolos)
        elif '=' == arquivo_fonte[contador_coluna]:
            return self.q16(arquivo_fonte, l, tabela_simbolos)
        elif '>' == arquivo_fonte[contador_coluna]:    
            return self.q17(arquivo_fonte, l, tabela_simbolos)
        elif '+' == arquivo_fonte[contador_coluna] or '-' == arquivo_fonte[contador_coluna] or '*' == arquivo_fonte[contador_coluna] or '/' == arquivo_fonte[contador_coluna]:
            return self.q19(arquivo_fonte, l, tabela_simbolos)
        elif '(' == arquivo_fonte[contador_coluna]:
            return self.q20(arquivo_fonte, l, tabela_simbolos)
        elif ')' == arquivo_fonte[contador_coluna]:
            return self.q21(arquivo_fonte, l, tabela_simbolos)
        elif ';' == arquivo_fonte[contador_coluna]: 
            return self.q22(arquivo_fonte, l, tabela_simbolos)
        elif ',' == arquivo_fonte[contador_coluna]:
            return self.q23(arquivo_fonte, l, tabela_simbolos)
        elif arquivo_fonte[contador_coluna].isalpha():
            return self.q11(arquivo_fonte, l, tabela_simbolos)
        elif '\t' == arquivo_fonte[contador_coluna]:
            contador_coluna += 1
            j = contador_coluna
            return self.q0(arquivo_fonte, l, tabela_simbolos)
        elif arquivo_fonte[contador_coluna].isspace():
            contador_coluna+= 1
            j = contador_coluna
            return self.q0(arquivo_fonte, l, tabela_simbolos)
        elif '\n' == arquivo_fonte[contador_coluna]:
            return None
        else:
            return self.q24(1, arquivo_fonte, l)

    def q1(self, arquivo_fonte, l, tabela_simbolos): # token *num*
        global contador_coluna
        global j
        global contador_coluna
        global palavra

        contador_coluna +=1        
        if arquivo_fonte[contador_coluna].isspace() or self.Delimitadores(arquivo_fonte) or self.Operadores(arquivo_fonte) or arquivo_fonte[contador_coluna]=='\n': 
            palavra = arquivo_fonte[j:contador_coluna]
            if not self.l.procura_na_lista(palavra):
                l.push('NUM', palavra)
            return self.l.procura_na_lista(palavra)        
        if arquivo_fonte[contador_coluna].isdigit():
            return self.q1(arquivo_fonte, l, tabela_simbolos)
        elif '.' == arquivo_fonte[contador_coluna]:
            return self.q2(arquivo_fonte, l, tabela_simbolos)
        elif 'e' == arquivo_fonte[contador_coluna] or 'E' == arquivo_fonte[contador_coluna]: 
            return self.q4(arquivo_fonte, l, tabela_simbolos)
        else: 
            return self.q24(4,arquivo_fonte, l) 

    def q2(self, arquivo_fonte, l, tabela_simbolos):  
        global j 
        global contador_coluna
        contador_coluna += 1        
        if arquivo_fonte[contador_coluna].isspace() or arquivo_fonte[contador_coluna].isdigit():
            return self.q3(arquivo_fonte, l, tabela_simbolos)
        else: 
            return self.q24(4, arquivo_fonte, l)

    def q3(self, arquivo_fonte, l, tabela_simbolos): # token *num*
        global j 
        global contador_coluna
        global palavra
        contador_coluna += 1        
        if arquivo_fonte[contador_coluna].isspace() or self.Delimitadores(arquivo_fonte) or self.Operadores(arquivo_fonte) or arquivo_fonte[contador_coluna]=='\n': 
            palavra = arquivo_fonte[j:contador_coluna]
            if not self.l.procura_na_lista(palavra):
                l.push('NUM', palavra)
            return self.l.procura_na_lista(palavra)
        if arquivo_fonte[contador_coluna].isdigit():
            return self.q3(arquivo_fonte, l, tabela_simbolos)
        elif 'e' == arquivo_fonte[contador_coluna] or 'E' == arquivo_fonte[contador_coluna]: 
            return self.q4(arquivo_fonte, l, tabela_simbolos)
        else: 
            return self.q24(4, arquivo_fonte, l)
 
    def q4(self, arquivo_fonte, l, tabela_simbolos):
        global j 
        global contador_coluna
       
        contador_coluna += 1        
        if arquivo_fonte[contador_coluna].isdigit():
            return self.q6(arquivo_fonte, l, tabela_simbolos)
        elif '+' == arquivo_fonte[contador_coluna] or '-' == arquivo_fonte[contador_coluna]: 
            return self.q5(arquivo_fonte, l, tabela_simbolos)
        else: 
            return self.q24(4, arquivo_fonte, l)


    def q5(self, arquivo_fonte, l, tabela_simbolos): 
        global j 
        global contador_coluna
       
        contador_coluna += 1        
        if arquivo_fonte[contador_coluna].isdigit():
            return self.q6(arquivo_fonte, l, tabela_simbolos)
        else: 
            return self.q24(4, arquivo_fonte, l)

    def q6(self, arquivo_fonte, l, tabela_simbolos): # token *num*
        global j 
        global contador_coluna
        global palavra
        contador_coluna += 1        
        if arquivo_fonte[contador_coluna].isspace() or self.Delimitadores(arquivo_fonte) or self.Operadores(arquivo_fonte) or arquivo_fonte[contador_coluna]=='\n': 
            palavra = arquivo_fonte[j:contador_coluna]
            if not self.l.procura_na_lista(palavra):
                l.push('NUM', palavra)
            return self.l.procura_na_lista(palavra)
        if arquivo_fonte[contador_coluna].isdigit():
            return self.q6(arquivo_fonte, l, tabela_simbolos)
        else: 
            return self.q24(4, arquivo_fonte, l)

    def q7(self, arquivo_fonte, l, tabela_simbolos): #começa lit
        global j
        global contador_coluna
        while arquivo_fonte[contador_coluna] !="\n":
            contador_coluna +=1
            if arquivo_fonte[contador_coluna] == '"':
                return self.q8(arquivo_fonte, l, tabela_simbolos)
            return self.q7(arquivo_fonte, l, tabela_simbolos)
        return self.q24(2, arquivo_fonte, l)
    
    def q8(self, arquivo_fonte, l, tabela_simbolos): # token *lit*
        global j
        global contador_coluna
        global palavra
        contador_coluna += 1
        if arquivo_fonte[contador_coluna].isspace() or self.Delimitadores(arquivo_fonte) or self.Operadores(arquivo_fonte):
            palavra = arquivo_fonte[j:contador_coluna] 
            if not self.l.procura_na_lista(palavra):
                l.push('lit', palavra)
            return self.l.procura_na_lista(palavra)
        else:
            return self.q24(2, arquivo_fonte, l)

    def q9(self, arquivo_fonte, l, tabela_simbolos): #Abre { comentário
        global j
        global contador_coluna
        while arquivo_fonte[contador_coluna] !="\n":
            contador_coluna += 1
            if arquivo_fonte[contador_coluna] == '}':
                return self.q10(arquivo_fonte, l, tabela_simbolos)
        return self.q24(3, arquivo_fonte, l)

    def q10(self, arquivo_fonte, l, tabela_simbolos): # fecha } comentário
        global j
        global contador_coluna
        contador_coluna += 1
        return None

    def q11(self, arquivo_fonte, l, tabela_simbolos): # reconhece *id*
        global j 
        global contador_coluna
        global palavra
        contador_coluna += 1
        i = 0
        erro = 0
        if not (arquivo_fonte[contador_coluna].isspace() or self.Delimitadores(arquivo_fonte) or self.Operadores(arquivo_fonte) or arquivo_fonte[contador_coluna] == '\n'):
            return self.q11(arquivo_fonte, l, tabela_simbolos)
        else:
            i = j
            while i < contador_coluna:
                if arquivo_fonte[i].isdigit() or arquivo_fonte[i].isalpha() or arquivo_fonte[i] == '_':
                    i += 1
                else:
                    i += 1
                    erro = 1
            if erro == 0:
                palavra = arquivo_fonte[j:contador_coluna]
                if self.tabela_simbolos.procura_na_lista(palavra):
                    return self.tabela_simbolos.procura_na_lista(palavra)
                if not self.l.procura_na_lista(palavra):
                    l.push('id', palavra)
                return self.l.procura_na_lista(palavra)
            else:
                return self.q24(5, arquivo_fonte, l)

    def q12(self, arquivo_fonte, l, tabela_simbolos): # reconhece *<*
        global j 
        global contador_coluna
        global palavra
        contador_coluna += 1       
        if arquivo_fonte[contador_coluna].isalpha() or arquivo_fonte[contador_coluna].isdigit() or arquivo_fonte == '"' or arquivo_fonte[contador_coluna].isspace():
            palavra = arquivo_fonte[j:contador_coluna]
            if not self.l.procura_na_lista(palavra):
                l.push('OPR', '<')
            return self.l.procura_na_lista(palavra)
        if arquivo_fonte[contador_coluna] == '-':
            return self.q15(arquivo_fonte, l, tabela_simbolos)
        elif arquivo_fonte[contador_coluna] == '=':
            return self.q14(arquivo_fonte, l, tabela_simbolos)
        elif arquivo_fonte[contador_coluna] == '>':
            return self.q13(arquivo_fonte, l, tabela_simbolos)
        else: 
            return self.q24(1, arquivo_fonte, l)

    def q13(self, arquivo_fonte, l, tabela_simbolos): # diferente <>
        global j
        global contador_coluna
        global palavra
        contador_coluna += 1        
        if arquivo_fonte[contador_coluna].isalpha() or arquivo_fonte[contador_coluna].isdigit() or arquivo_fonte == '"' or arquivo_fonte[contador_coluna].isspace() or arquivo_fonte[contador_coluna]=='\n':
            palavra = arquivo_fonte[j:contador_coluna]
            if not self.l.procura_na_lista(palavra):
                l.push('OPR', '<>')
            return self.l.procura_na_lista(palavra)
        else: 
            return self.q24(1,arquivo_fonte, l)

    def q14(self, arquivo_fonte, l, tabela_simbolos):  # menor igual <=
        global j
        global contador_coluna
        global palavra
        contador_coluna += 1        
        if arquivo_fonte[contador_coluna].isalpha() or arquivo_fonte[contador_coluna].isdigit() or arquivo_fonte == '"' or arquivo_fonte[contador_coluna].isspace() or arquivo_fonte[contador_coluna]=='\n':
            palavra = arquivo_fonte[j:contador_coluna]
            if not self.l.procura_na_lista(palavra):
                l.push('OPR', '<=')
            return self.l.procura_na_lista(palavra)
        else: 
            return self.q24(1,arquivo_fonte, l)

    def q15(self, arquivo_fonte, l, tabela_simbolos): # atribuicao <-
        global j 
        global contador_coluna
        global palavra
        contador_coluna += 1        
        if arquivo_fonte[contador_coluna].isalpha() or arquivo_fonte[contador_coluna].isdigit() or arquivo_fonte == '"' or arquivo_fonte[contador_coluna].isspace() or arquivo_fonte[contador_coluna]=='\n':
            palavra = arquivo_fonte[j:contador_coluna]
            if not self.l.procura_na_lista(palavra):
                l.push('RCB', '<-')
            return self.l.procura_na_lista(palavra)
        else: 
            return self.q24(1, arquivo_fonte, l)

    def q16(self, arquivo_fonte, l, tabela_simbolos): # =
        global j 
        global contador_coluna
        global palavra 
        contador_coluna  += 1
        if arquivo_fonte[contador_coluna].isalpha() or arquivo_fonte[contador_coluna].isdigit() or arquivo_fonte == '"' or arquivo_fonte[contador_coluna].isspace() or arquivo_fonte[contador_coluna]=='\n':
            palavra = arquivo_fonte[j:contador_coluna]
            if not self.l.procura_na_lista(palavra):
                l.push('OPR', '=')
            return self.l.procura_na_lista(palavra)
        else: 
            
            return self.q24(1, arquivo_fonte, l)

    def q17(self, arquivo_fonte, l, tabela_simbolos): # reconhece *>*
        global j 
        global contador_coluna
        global palavra
        contador_coluna += 1        
        if arquivo_fonte[contador_coluna].isalpha() or arquivo_fonte[contador_coluna].isdigit() or arquivo_fonte == '"' or arquivo_fonte[contador_coluna].isspace() or arquivo_fonte[contador_coluna]=='\n':
            palavra = arquivo_fonte[j:contador_coluna]
            if not self.l.procura_na_lista(palavra):
                l.push('OPR', '>')
            return self.l.procura_na_lista(palavra)
        if arquivo_fonte[contador_coluna] == '=':
            return self.q18(arquivo_fonte, l, tabela_simbolos)
        else: 
            return self.q24(1, arquivo_fonte, l)

    def q18(self, arquivo_fonte, l, tabela_simbolos): # maior igual >=
        global j 
        global contador_coluna
        global palavra
        contador_coluna += 1        
        if arquivo_fonte[contador_coluna].isalpha() or arquivo_fonte[contador_coluna].isdigit() or arquivo_fonte == '"' or arquivo_fonte[contador_coluna].isspace() or arquivo_fonte[contador_coluna]=='\n':
            palavra = arquivo_fonte[j:contador_coluna]
            if not self.l.procura_na_lista(palavra):
                l.push('OPR', '>=')
            return self.l.procura_na_lista(palavra)
        else: 
            return self.q24(1, arquivo_fonte, l)

    def q19(self, arquivo_fonte, l, tabela_simbolos): # operadores + - *  /
        global j 
        global contador_coluna
        global palavra
        contador_coluna += 1        
        if arquivo_fonte[contador_coluna].isalpha() or arquivo_fonte[contador_coluna].isdigit() or arquivo_fonte == '"' or arquivo_fonte[contador_coluna].isspace() or arquivo_fonte[contador_coluna]=='\n':
            palavra = arquivo_fonte[j:contador_coluna]
            if not self.l.procura_na_lista(palavra):
                l.push('OPM', palavra)
            return self.l.procura_na_lista(palavra)
        else: 
            return self.q24(1, arquivo_fonte, l)

    def q20(self, arquivo_fonte, l, tabela_simbolos): # (
        global j 
        global contador_coluna
        global palavra
        contador_coluna += 1        
        if arquivo_fonte[contador_coluna].isalpha() or arquivo_fonte[contador_coluna].isdigit() or arquivo_fonte[contador_coluna] == '"' or arquivo_fonte[contador_coluna].isspace() or self.Delimitadores_ABP(arquivo_fonte) or arquivo_fonte[contador_coluna] =='\n':
            palavra = arquivo_fonte[j:contador_coluna]
            if not self.l.procura_na_lista(palavra):
                l.push('AB_P', '(')
            return self.l.procura_na_lista(palavra)
        else: 
            return self.q24(1, arquivo_fonte, l)

    def q21(self, arquivo_fonte, l, tabela_simbolos): # )
        global j 
        global contador_coluna
        global palavra
        contador_coluna += 1        
        if arquivo_fonte[contador_coluna].isalpha() or arquivo_fonte[contador_coluna].isdigit() or arquivo_fonte[contador_coluna] == '"' or arquivo_fonte[contador_coluna].isspace() or self.Delimitadores_ABP(arquivo_fonte) or arquivo_fonte[contador_coluna] =='\n':
            palavra = arquivo_fonte[j:contador_coluna]
            if not self.l.procura_na_lista(palavra):
                l.push('FC_P', ')')
            return self.l.procura_na_lista(palavra)
        else: 
            return self.q24(1, arquivo_fonte, l)

    def q22(self, arquivo_fonte, l, tabela_simbolos): # ;
        global j
        global palavra 
        global contador_coluna
        global palavra
        contador_coluna += 1
        erro = contador_coluna + 1        
        if arquivo_fonte[contador_coluna]: 
            palavra = arquivo_fonte[j:contador_coluna]
            if not self.l.procura_na_lista(palavra):
                l.push('PT_V', ';')
            return self.l.procura_na_lista(palavra)
        if arquivo_fonte[erro]:
            return self.q24(1, arquivo_fonte, l)

    def q23(self, arquivo_fonte, l, tabela_simbolos): # ,
        global j 
        global contador_coluna
        global palavra
        contador_coluna += 1        
        if arquivo_fonte[contador_coluna].isspace() or arquivo_fonte[contador_coluna].isalpha():
            palavra = arquivo_fonte[j:contador_coluna]
            if not self.l.procura_na_lista(palavra):
                l.push('VIR', ',')
            return self.l.procura_na_lista(palavra)
        else: 
            return self.q24(1, arquivo_fonte, l)


    def q24(self, cod, arquivo_fonte, l): # erro
        global palavra
        global j
        global contador_coluna
        contador_coluna+=1
        if cod ==2 or cod == 3 or cod ==5:
            palavra = arquivo_fonte[j:contador_coluna-1]
            if not self.l.procura_na_lista (palavra):
                l.push('ERRO'+str(cod), palavra)
            return self.l.procura_na_lista(palavra)
        else:
            palavra = arquivo_fonte[j:contador_coluna]
            if not self.l.procura_na_lista (palavra):
                l.push('ERRO'+str(cod), palavra)
            return self.l.procura_na_lista(palavra)


    def erro(self, cod):
        if(cod==2):
            print("Erro " + str(cod) + ". Aspas vêm ao final de constantes literais. Linha " + str(contador_linha) + ", coluna " + str(j+1) +" à coluna "+str(contador_coluna-1) +".")
        elif(cod==3):
            print("Erro " + str(cod) + ". Chaves devem fechar comentários. Linha " + str(contador_linha) + ", coluna " + str(j+1) +"  à coluna "+str(contador_coluna-1) +".")
        elif(cod==4):
            print("Erro " + str(cod) + ". Formato numérico permitido: D(.D)(e|E(+|-)D). Linha " + str(contador_linha) + ", coluna " + str(contador_coluna) + ".")
        elif(cod==5):
            print("Erro " + str(cod) + ". Há pelo menos um caractere inválido no id. Linha " + str(contador_linha) + ", coluna " + str(j+1) +" à coluna "+str(contador_coluna-1) +".")
        else:
            print("Erro " + str(cod) + ". caractere inválido, linha " + str(contador_linha) + ", coluna " + str(contador_coluna) + ".")
     
def main():
    if not os.path.exists('f.txt'):
        print("Arquivo não encontrado.\n")
    else: 
        #fonte = open('f.txt', 'a+') #abre arquivo
        #fonte.write(" EOF ")
        #fonte.close()
        fonte = open('f.txt', 'r+')
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
        tabela_simbolos.push('EOF', 'EOF')


        global contador_linha 
        global contador_coluna
        global arquivo_fonte
        contador_linha = 1
        contador_coluna = 0
        tamanho = 0

        for arquivo_fonte in fonte:
            contador_coluna = 0
            tamanho = len(arquivo_fonte)-1
            while contador_coluna < tamanho:
                retorno_scanner = ana.scanner(arquivo_fonte, l, tabela_simbolos)

                if retorno_scanner != None:
                    if str(retorno_scanner.classe)[0:4] == "ERRO":
                        print("Classe: " + retorno_scanner.classe + ", lexema: " + retorno_scanner.lexema + ", tipo: " + retorno_scanner.tipo + ".")
                        cod = int(retorno_scanner.classe[4:5])
                        ana.erro(cod)     
                    else:
                        print("Classe: " + retorno_scanner.classe + ", lexema: " + retorno_scanner.lexema + ", tipo: " + retorno_scanner.tipo + ".")      
            contador_linha += 1  
        fonte.close()

if __name__ == '__main__':
    main()