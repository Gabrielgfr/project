# Projeto de Testes Automatizados

## Configuração do Ambiente
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
playwright install


# Execução dos Testes
# Executar todos os testes: python app/executar_testes.py


# Ou diretamente com pytest: 



#Estrutura do Projeto
app/cliente_api.py: Cliente HTTP para API

app/automacao_web.py: Funções para automação web

tests/test_api.py: Testes de API

tests/test_web.py: Testes de interface web