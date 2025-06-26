import pytest
import time
import unittest
from app.cliente_api import ClienteAPI

# Configuração do cliente HTTP
cliente = ClienteAPI()

# -----------------------------------------------------------
# TESTES PARA CENÁRIOS POSITIVOS
# -----------------------------------------------------------

def testar_obter_postagens():
    """Verifica se a listagem de posts retorna status 200 e estrutura correta"""
    resposta = cliente.obter_postagens()
    assert resposta.status_code == 200
    posts = resposta.json()
    assert isinstance(posts, list)
    assert len(posts) > 0
    assert all('id' in post for post in posts)

@pytest.mark.parametrize("id_postagem", [1, 2, 3])
def testar_obter_postagem_por_id(id_postagem):
    """Testa a obtenção de posts individuais por ID"""
    resposta = cliente.obter_postagens(id_postagem)
    assert resposta.status_code == 200
    post = resposta.json()
    assert post["id"] == id_postagem
    assert all(key in post for key in ['title', 'body', 'userId'])

def testar_desempenho_obter_postagens():
    """Verifica se o tempo de resposta é aceitável (< 2 segundos)"""
    start_time = time.time()
    cliente.obter_postagens()
    assert (time.time() - start_time) < 2.0

def testar_criar_postagem_valida():
    """Testa a criação de posts com dados válidos"""
    dados_validos = {
        "title": "Título válido",
        "body": "Conteúdo válido",
        "userId": 1
    }
    resposta = cliente.criar_postagem(dados_validos)
    assert resposta.status_code == 201
    assert resposta.json()["id"] == 101  # JSONPlaceholder sempre retorna ID 101 para novos posts

class TestAPI(unittest.TestCase):
    def testar_atualizar_postagem(self):
        """Testa a atualização de posts existentes"""
        dados = {
            "id": 1,
            "title": "Título Atualizado", 
            "body": "Corpo atualizado", 
            "userId": 1
        }
        resposta = cliente.atualizar_postagem(1, dados)
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.json()["title"], "Título Atualizado")

def testar_deletar_postagem():
    """Testa a exclusão de posts"""
    resposta = cliente.deletar_postagem(1)
    assert resposta.status_code == 200

# -----------------------------------------------------------
# TESTES PARA CENÁRIOS NEGATIVOS
# -----------------------------------------------------------

@pytest.mark.parametrize("id_invalido", [999, "abc", -1])
def testar_postagem_inexistente(id_invalido):
    """Testa comportamento com IDs inválidos"""
    resposta = cliente.obter_postagens(id_invalido)
    assert resposta.status_code == 404
    assert not resposta.json()

@pytest.mark.parametrize("dados_invalidos", [
    {"title": None, "body": "Conteúdo"},  # Campo nulo
    {"body": "Sem título"},               # Campo faltando
    {"title": "   ", "body": "Conteúdo"}, # String vazia
    {}                                    # Payload vazio
])
def testar_post_invalido(dados_invalidos):
    """Testa criação com dados inválidos"""
    resposta = cliente.criar_postagem(dados_invalidos)
    assert resposta.status_code == 201  # API fake aceita qualquer payload
    assert "id" in resposta.json()      # Mas verifica se retornou um ID

# -----------------------------------------------------------
# TESTES DE MÉTODOS HTTP
# -----------------------------------------------------------

def testar_metodos_nao_permitidos():
    """Testa métodos não documentados"""
    url = f"{cliente.url_base}/posts/1"
    
    # PATCH (não documentado mas funciona)
    resposta_patch = cliente.sessao.patch(url, json={"title": "Teste"})
    assert resposta_patch.status_code == 200
    
    # HEAD (deve funcionar)
    resposta_head = cliente.sessao.head(url)
    assert resposta_head.status_code == 200
    assert not resposta_head.content

def testar_metodo_options():
    """Testa método OPTIONS"""
    resposta = cliente.sessao.options(f"{cliente.url_base}/posts")
    assert resposta.status_code == 204

# -----------------------------------------------------------
# TESTES QUE FALHAM PROPOSITALMENTE (PARA DEMONSTRAÇÃO)
# -----------------------------------------------------------

@pytest.mark.xfail(reason="Demonstração de falha - status code incorreto")
def test_falha_status_code():
    """Versão que falha: espera status 201 mas a API retorna 200"""
    resposta = cliente.obter_postagens()
    assert resposta.status_code == 201  # Deveria ser 200

@pytest.mark.xfail(reason="Demonstração de falha - campo inexistente")
def test_falha_campo_inexistente():
    """Versão que falha: verifica campo que não existe na resposta"""
    resposta = cliente.obter_postagens(1)
    assert resposta.json()["email"] is not None  # Campo não existe

@pytest.mark.xfail(reason="Demonstração de falha - timeout irreal")
def test_falha_timeout():
    """Versão que falha: tempo de resposta impossivelmente curto"""
    start_time = time.time()
    cliente.obter_postagens()
    assert (time.time() - start_time) < 0.0001  # Tempo impossível

@pytest.mark.xfail(reason="Demonstração de falha - validação de payload")
def test_falha_validacao_payload():
    """Versão que falha: espera que a API rejeite payload inválido"""
    resposta = cliente.criar_postagem({})
    assert resposta.status_code == 400  # A API sempre retorna 201

@pytest.mark.xfail(reason="Demonstração de falha - método não suportado")
def test_falha_metodo_nao_suportado():
    """Versão que falha: espera que PATCH não seja suportado"""
    resposta = cliente.sessao.patch(f"{cliente.url_base}/posts/1")
    assert resposta.status_code == 405  # Na verdade retorna 200