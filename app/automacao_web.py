import sys
from pathlib import Path


# Adiciona o diretório app ao PATH
sys.path.append(str(Path(__file__).parent))

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    SELENIUM_INSTALADO = True
except ImportError:
    SELENIUM_INSTALADO = False

try:
    from playwright.sync_api import sync_playwright
    PLAYWRIGHT_INSTALADO = True
except ImportError:
    PLAYWRIGHT_INSTALADO = False

class AutomacaoWeb:
    def __init__(self):
        if not SELENIUM_INSTALADO:
            raise ImportError("Selenium não está instalado. Execute: pip install selenium webdriver-manager")
        if not PLAYWRIGHT_INSTALADO:
            raise ImportError("Playwright não está instalado. Execute: pip install playwright && playwright install")
        
        self.driver = None
        self.playwright = None
        self.browser = None
        self.page = None

    def iniciar_selenium(self):
        """Inicializa o navegador com Selenium"""
        try:
            service = ChromeService(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service)
            return self.driver
        except Exception as e:
            raise RuntimeError(f"Erro ao iniciar Selenium: {str(e)}")

    def iniciar_playwright(self):
        """Inicializa o navegador com Playwright"""
        try:
            self.playwright = sync_playwright().start()
            self.browser = self.playwright.chromium.launch(headless=False)
            self.page = self.browser.new_page()
            return self.page
        except Exception as e:
            raise RuntimeError(f"Erro ao iniciar Playwright: {str(e)}")

    def finalizar(self):
        """Encerra todos os recursos"""
        try:
            if self.driver:
                self.driver.quit()
            if self.browser:
                self.browser.close()
            if self.playwright:
                self.playwright.stop()
        except Exception as e:
            print(f"Aviso: Erro ao finalizar recursos: {str(e)}")