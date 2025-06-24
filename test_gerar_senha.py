from gerar_senha import GeradorSenha

class TestGeradorSenha:
    def test_minuscula(self):
        gerador = GeradorSenha(minuscula=True)
        senha = gerador.gerar()
        assert any(c.islower() for c in senha)
    
    # def test_maiuscula(self):
    #     gerador = GeradorSenha(maiuscula=True)
    #     senha = gerador.gerar()
    #     assert any(c.isupper() for c in senha)
    
    # def test_numero(self):
    #     gerador = GeradorSenha(numero=True)
    #     senha = gerador.gerar()
    #     assert any(c.isdigit() for c in senha)