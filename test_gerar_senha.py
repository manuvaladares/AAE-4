from gerar_senha import GeradorSenha

class TestGeradorSenha:
    def test_minuscula(self):
        gerador = GeradorSenha(minuscula=True)
        senha = gerador.gerar()
        assert any(c.islower() for c in senha)