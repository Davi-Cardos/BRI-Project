import os
import string
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import nltk

nltk.download('stopwords')


caminho_base = 'source-document'


text = ''


for root, dirs, files in os.walk(caminho_base):
    for arquivo in files:
        if arquivo.endswith(".txt"):
            
            with open(os.path.join(root, arquivo), 'r', encoding='utf-8-sig') as f:
                text += f.read() + " "  

    print(f"Pasta '{root}' concluída!")


text = text.translate(str.maketrans('', '', string.punctuation))


fd = FreqDist(word.lower() for word in text.split())
print("Frequências calculadas!")

# 1. Tamanho do vocabulário
tamanho_vocabulario = len(fd)

# 2. Total de palavras na coleção
total_palavras = sum(fd.values())

# Exibir o tamanho do vocabulário e o total de palavras
print(f"Tamanho do vocabulário: {tamanho_vocabulario}")
print(f"Total de palavras no arquivo: {total_palavras}")

# 3. As 10 palavras mais frequentes
mais_frequentes = fd.most_common(10)
print("\n10 palavras mais frequentes e suas frequências:")
for palavra, freq in mais_frequentes:
    print(f"'{palavra}': {freq}")


frequencia_minima = min(fd.values())  
menos_frequentes = [(palavra, freq) for palavra, freq in fd.items() if freq == frequencia_minima][:10]
print("\n10 palavras menos frequentes e suas frequências:")
for palavra, freq in menos_frequentes:
    print(f"'{palavra}': {freq}")


stopwords_ingles = set(stopwords.words('english'))
stopwords_no_corpus = {palavra: freq for palavra, freq in fd.items() if palavra in stopwords_ingles}

# Stopwords mais frequentes
stopwords_mais_frequentes = sorted(stopwords_no_corpus.items(), key=lambda x: x[1], reverse=True)[:10]
print("\nStopwords mais frequentes no corpus:")
for palavra, freq in stopwords_mais_frequentes:
    print(f"'{palavra}': {freq}")

# Stopwords menos frequentes
stopwords_menos_frequentes = sorted(stopwords_no_corpus.items(), key=lambda x: x[1])[:10]
print("\nStopwords menos frequentes no corpus:")
for palavra, freq in stopwords_menos_frequentes:
    print(f"'{palavra}': {freq}")

# Plotar o gráfico de frequência
p = fd.plot(50, show=False, title="Distribuição das palavras nos documentos")
p.set_xlabel("Amostra")
p.set_ylabel("Frequência")
plt.show()