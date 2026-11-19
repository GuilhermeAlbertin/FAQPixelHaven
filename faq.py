import json
import os
import unicodedata


def normalizar(txt):
    txtformatado = (
        unicodedata.normalize("NFKD", txt).encode("ascii", "ignore").decode().lower()
    )
    return txtformatado


def carregar_faq(caminho):
    try:
        with open(caminho, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Erro: o arquivo {caminho} não foi encontrado")
    except json.JSONDecodeError:
        print(f"ERRO: O arquivo {caminho} tem um erro de formatação...")
        return []


def buscar_faq(mensagem, faq, limite=3):
    resultados = []
    for entrada in faq:
        contador = 0
        for palavra in entrada["palavras_chave"]:
            if normalizar(palavra) in mensagem:

                contador += 1
        if contador > 0:
            resultados.append((contador, entrada))
    if not resultados:
        print(
            "Não encontrei isso no meu material -  Vou registrar para um atendente humano"
        )
        resultados.sort(key=lambda par: par[0], reverse=True)
    return [entrada for contador, entrada in resultados[:limite]]
