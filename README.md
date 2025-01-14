<div align="center">
  <h1>🕵️‍♂️ BRI-Project</h1>
  <p><strong>Motor de busca para detectar plágio em documentos</strong></p>
</div>

## 📑 Índice

1. [Sobre o Projeto](#sobre-o-projeto)
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)
3. [Instalação](#instalação)
4. [Como Usar](#como-usar)
5. [Contribuição](#contribuição)
6. [Licença](#licença)
7. [Contato](#contato)

---

## Sobre o Projeto

O **BRI-Project** é um motor de busca desenvolvido para detectar plágio em documentos. Ele utiliza técnicas avançadas de recuperação de informação para identificar similaridades entre textos, auxiliando na preservação da integridade acadêmica e profissional.

---

## ⚙️ Tecnologias Utilizadas

<ul>
  <li><a href="https://www.python.org/" target="_blank">Python</a></li>
  <li><a href="https://www.elastic.co/elasticsearch/" target="_blank">ElasticSearch</a></li>
  <li><a href="https://whoosh.readthedocs.io/en/latest/" target="_blank">Whoosh</a></li>
</ul>

---

## 🛠️ Instalação

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/Davi-Cardos/BRI-Project.git

2. **Navegue até o diretório do projeto**:

  ```bash
  cd BRI-Project
```
3. **Crie um ambiente virtual e ative-o**:

  ```bash
python -m venv venv
```
```bash
source venv/bin/activate
# No Windows: venv\Scripts\activate
```
4. **Instale as dependências**:

```bash
pip install -r requirements.txt
```

## 🚀 Como Usar
### Indexe os documentos:

Para indexar usando o ElasticSearch:
```bash
python Indexacao-ElasticSearch.py
```

Para indexar usando o Whoosh:
```bash
python Indexacao-Whoosh.py
```

### Realize consultas para detectar plágio:

Usando o ElasticSearch:
```bash
python Consulta-ElasticSearch.py
```

Usando o Whoosh:
```bash
python Consulta-Whoosh.py
```

Gere gráficos dos resultados:

```bash
python Geracao-Grafico.py
```
## 🤝 Contribuição 
### Para contribuir:

1. Faça um fork do projeto.
   
2. Crie uma branch para sua feature (git checkout -b feature/AmazingFeature).
   
3. Faça o commit das suas alterações (git commit -m 'Add some AmazingFeature').
   
4. Envie para o repositório remoto (git push origin feature/AmazingFeature).

5. Abra um pull request.
   
## 📜 Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.

## 📬 Contato
<div align="center"> <strong>Davi Cardoso de Oliveira</strong><br> <a href="davideoliveira2003@gmail.com">davideoliveira2003@gmail.com</a><br> <a href="https://www.linkedin.com/in/davi-cardoso-874417331/" target="_blank">LinkedIn</a> </div> 
