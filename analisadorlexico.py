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

        #aqui precisamos completar e linkar estados
        #não sei mexer com python direito ainda, veja se fiz caquinha com self

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