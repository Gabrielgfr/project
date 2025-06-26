import pytest
from app.automacao_web import AutomacaoWeb

@pytest.fixture(scope="module")
def navegador_selenium():
    web = AutomacaoWeb()
    driver = web.iniciar_selenium()
    yield driver
    web.finalizar()

@pytest.fixture
def pagina_playwright():
    web = AutomacaoWeb()
    try:
        pagina = web.iniciar_playwright()
        yield pagina
    finally:
        web.finalizar()