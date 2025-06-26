#### Configuração do Ambiente

1.  **Crie e Ative o Ambiente Virtual:**
    **Windows:**
       ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
2.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    playwright install
    ```

### Executando os Testes
 **Executar Todos os Testes:**
   ```bash
    python -m pytest tests/ -v
    ```
    Este comando executará todos os testes encontrados no diretório `tests/` e mostrará um relatório detalhado (`-v` para modo verboso).

* **Executar Apenas Testes de API:**
    ```bash
    python -m pytest tests/test_api.py -v
    ```

* **Executar Apenas Testes Web:**
    ```bash
    python -m pytest tests/test_web.py -v
    ```

* **Ignorar Testes XFAIL (Falhas Esperadas):**
    ```bash
    python -m pytest tests/ -v -m "not xfail"
    ```
    #Útil para focar apenas nos testes que devem passar.

* **Executar Apenas Testes XFAIL (Falhas Esperadas):**
    ```bash
    python -m pytest tests/ -v -m "xfail"
    ```
    #Ideal para monitorar bugs conhecidos ou requisitos em desenvolvimento.

* **Filtrar Testes por Palavra-Chave:**
    ```bash
    python -m pytest tests/test_api.py -k "postagem_inexistente or post_invalido" -v
    ```
    #Execute testes cujo nome contenha as palavras-chave especificadas.

* **Executar um Teste Específico:**
    ```bash
    python -m pytest tests/test_api.py::testar_obter_postagens -v
    ```
    #Útil para depuração rápida de um único cenário.
