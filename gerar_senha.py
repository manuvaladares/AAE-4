from random import choice
import string

class GeradorSenha:
    def __init__(self, tamanho=8, minuscula=False, maiuscula=False, numero=False, simbolo=False):
        self.tamanho = tamanho
        self.minuscula = minuscula
        self.maiuscula = maiuscula
        self.numero = numero
        self.simbolo = simbolo

    def gerar(self):
        senha = ""
        caracteres = ""

        if self.minuscula:
            caracteres += string.ascii_lowercase
            senha += choice(string.ascii_lowercase)
            
        if self.maiuscula:
            caracteres += string.ascii_uppercase
            senha += choice(string.ascii_uppercase)
            
        if self.numero:
            caracteres += string.digits
            senha += choice(string.digits)
        
        if self.simbolo:
            caracteres += "!@#$%&*"
            senha += choice("!@#$%&*")
        
        if not caracteres:
            raise ("Você deve selecionar pelo menos um critério para gerar uma senha")

        while len(senha) < self.tamanho:
            senha += choice(caracteres)
            
        return senha

gerador = GeradorSenha(tamanho=10, minuscula=False, maiuscula=False, numero=False, simbolo=False)
print(gerador.gerar())