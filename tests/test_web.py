from app.automacao_web import AutomacaoWeb
import pytest

def testar_titulo_com_selenium():
    web = AutomacaoWeb()
    try:
        driver = web.iniciar_selenium()
        driver.get("https://jsonplaceholder.typicode.com")
        assert "JSONPlaceholder" in driver.title
        elemento_h1 = driver.find_element("tag name", "h1")
        assert elemento_h1.text == "JSONPlaceholder"
    finally:
        web.finalizar()

def testar_titulo_com_playwright(pagina_playwright):
    """Testa o título da página usando Playwright"""
    try:
        pagina = pagina_playwright
        pagina.goto("https://jsonplaceholder.typicode.com")
        
        # Verifica o título da página
        assert "JSONPlaceholder" in pagina.title()
        
        # Tira screenshot
        pagina.screenshot(path="captura_tela.png")
        
        # Verifica o texto do h1 (com tratamento de espaços)
        elemento_h1 = pagina.query_selector("h1")
        texto_h1 = elemento_h1.text_content().strip()  # Remove espaços extras
        assert texto_h1 == "JSONPlaceholder"
        
    except Exception as e:
        pytest.fail(f"Erro durante o teste: {str(e)}")