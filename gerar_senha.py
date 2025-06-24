from random import choice
import string

class GeradorSenha:
    def _init_(self, tamanho=8, minuscula=False, maiuscula=False, simbolo=False, numero=False):
        self.tamanho = tamanho
        self.minuscula = minuscula
        self.maiuscula = maiuscula
        self.simbolo = simbolo
        self.numero = numero

    def gerar(self):
        while len(self.senha) < self.tamanho:
            if self.minuscula:
                letra = choice(string.ascii_lowercase)
                self.senha += letra
        return self.senha

gerador = GeradorSenha(minuscula=True)
print(gerador.gerar())