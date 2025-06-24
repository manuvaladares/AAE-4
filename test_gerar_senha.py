from gerar_senha import GeradorSenha

class TestGeradorSenha:
    def test_minuscula(self):
        gerador = GeradorSenha(minuscula=True)
        senha = gerador.gerar()
        assert any(c.islower() for c in senha)
    
    def test_maiuscula(self):
        gerador = GeradorSenha(maiuscula=True)
        senha = gerador.gerar()
        assert any(c.isupper() for c in senha)
    
    def test_numero(self):
        gerador = GeradorSenha(numero=True)
        senha = gerador.gerar()
        assert any(c.isdigit() for c in senha)
        
    def test_simbolo(self):
        gerador = GeradorSenha(tamanho=8, simbolo=True)
        senha = gerador.gerar()
        assert any(c in "!@#$%&*" for c in senha)
    
    def test_tamanho_da_senha_gerada(self):
        tamanho_esperado = 12
        gerador = GeradorSenha(tamanho=tamanho_esperado, minuscula=True)
        senha = gerador.gerar()
        assert len(senha) == tamanho_esperado