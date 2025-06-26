import requests
import logging

class ClienteAPI:
    def __init__(self, url_base="https://jsonplaceholder.typicode.com"):
        self.url_base = url_base
        self.sessao = requests.Session()
        logging.basicConfig(level=logging.INFO)

    def obter_postagens(self, id_postagem=None):
        url = f"{self.url_base}/posts/{id_postagem}" if id_postagem else f"{self.url_base}/posts"
        resposta = self.sessao.get(url)
        logging.info(f"GET {url} - Status: {resposta.status_code}")
        return resposta

    def criar_postagem(self, dados):
        url = f"{self.url_base}/posts"
        resposta = self.sessao.post(url, json=dados)
        logging.info(f"POST {url} - Status: {resposta.status_code}")
        return resposta

    def atualizar_postagem(self, id_postagem, dados):
        url = f"{self.url_base}/posts/{id_postagem}"
        resposta = self.sessao.put(url, json=dados)
        logging.info(f"PUT {url} - Status: {resposta.status_code}")
        return resposta

    def deletar_postagem(self, id_postagem):
        url = f"{self.url_base}/posts/{id_postagem}"
        resposta = self.sessao.delete(url)
        logging.info(f"DELETE {url} - Status: {resposta.status_code}")
        return resposta