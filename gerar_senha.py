from random import choice
import string

class GeradorSenha:
    def __init__(self, tamanho=8, minuscula=False, maiuscula=False, numero=False):
        self.tamanho = tamanho
        self.minuscula = minuscula
        self.maiuscula = maiuscula
        self.numero = numero

    def gerar(self):
        senha = ""
        caracteres = ""

        if self.minuscula:
            caracteres += string.ascii_lowercase
            senha += choice(string.ascii_lowercase)

        