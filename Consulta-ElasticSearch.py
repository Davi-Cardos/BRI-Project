import os
import nltk
import numpy as np
from elasticsearch import Elasticsearch
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt

nltk.download("punkt")
nltk.download("stopwords")

es = Elasticsearch("http://localhost:9200")

def ler_txt(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        return arquivo.read()

def extrair_palavras_chave(texto, idioma="english", top_n=200):
    stop_words = set(stopwords.words(idioma))
    palavras = word_tokenize(texto.lower())
    palavras_filtradas = [palavra for palavra in palavras if palavra.isalnum() and palavra not in stop_words]
    frequencias = Counter(palavras_filtradas)
    return [palavra for palavra, _ in frequencias.most_common(top_n)]

def buscar_com_palavras_chave(palavras_chave):
    consulta = {
        "query": {
            "bool": {
                "should": [{"match": {"content": palavra}} for palavra in palavras_chave],
                "minimum_should_match": 200
            }
        }
    }
    response = es.search(index="files_index", body=consulta, size=200)
    return response['hits']['hits']


def calcular_precision_recall_at_k(results, k_values):

    p_at_k = []
    r_at_k = []
    
    for k in k_values:
        retrieved_documents = results[:k]
        relevant_documents = [result for result in retrieved_documents if result['_score'] > 0]

        # Calcular Precision@K
        precision = len(relevant_documents) / k if k > 0 else 0
        p_at_k.append(precision)
        
        # Calcular Recall@K
        recall = len(relevant_documents) / len(results) if len(results) > 0 else 0
        r_at_k.append(recall)
    
    return p_at_k, r_at_k

def processar_arquivo(caminho_arquivo, k_values=[2, 4, 6, 8, 10]):
    conteudo = ler_txt(caminho_arquivo)
    palavras_chave = extrair_palavras_chave(conteudo, top_n=200)
    resultados = buscar_com_palavras_chave(palavras_chave)
    
    p_at_k, r_at_k = calcular_precision_recall_at_k(resultados, k_values)
    
    return k_values, p_at_k, r_at_k

# Função para gerar os gráficos
def gerar_grafico(folder_path):
    all_p_at_k = {k: [] for k in [2, 4, 6, 8, 10]}
    all_r_at_k = {k: [] for k in [2, 4, 6, 8, 10]}
    
    # Iterar por todas as subpastas e arquivos dentro da pasta
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(".txt"):  # Verificar se é um arquivo de texto
                file_path = os.path.join(root, file_name)
                ks, p_at_k, r_at_k = processar_arquivo(file_path)
                
                # Armazenando os resultados
                for k in ks:
                    all_p_at_k[k].append(p_at_k[ks.index(k)])
                    all_r_at_k[k].append(r_at_k[ks.index(k)])
    
    # Calculando a média de P@K e R@K, ignorando NaN (Not a Number)
    avg_p_at_k = [np.nanmean(all_p_at_k[k]) for k in [2, 4, 6, 8, 10]]
    avg_r_at_k = [np.nanmean(all_r_at_k[k]) for k in [2, 4, 6, 8, 10]]

    # Plotando os gráficos
    plt.figure(figsize=(12, 6))

    # Precision at K
    plt.subplot(1, 2, 1)
    plt.plot([2, 4, 6, 8, 10], avg_p_at_k, label="Precision at K", marker='o')
    plt.xlabel("K")
    plt.ylabel("Precision at K")
    plt.title("Precision at K (P@K)")
    plt.legend()

    # Recall at K
    plt.subplot(1, 2, 2)
    plt.plot([2, 4, 6, 8, 10], avg_r_at_k, label="Recall at K", marker='o')
    plt.xlabel("K")
    plt.ylabel("Recall at K")
    plt.title("Recall at K (R@K)")
    plt.legend()

    plt.tight_layout()
    plt.show()


# Caminho para a pasta principal com as subpastas
pasta_principal = "suspicious-document"
gerar_grafico(pasta_principal)