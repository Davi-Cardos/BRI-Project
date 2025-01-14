import os
from elasticsearch import Elasticsearch
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import time

nltk.download("punkt")
nltk.download("stopwords")

es = Elasticsearch("http://localhost:9200")

def read_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def remove_stopwords(text, language="english"):
    stop_words = set(stopwords.words(language))
    words = word_tokenize(text.lower())
    filtered_words = [word for word in words if word not in stop_words and word.isalnum()]
    return " ".join(filtered_words)

def index_file(file_path, filename):
    start_time = time.time()

    content = read_txt(file_path)
    content = remove_stopwords(content)

    document = {
        "file_name": filename,
        "content": content
    }

    es.index(index="files_index", document=document)
    print(f"Indexed file: {filename}")

    end_time = time.time()
    processing_time = end_time - start_time
    return processing_time

def index_files_in_directory(directory_path):
    total_time = 0
    file_count = 0

    for root, dirs, files in os.walk(directory_path):
        print(f"Processing folder: {root}")
        for filename in files:
            if filename.endswith(".txt"):
                file_path = os.path.join(root, filename)

                print(f"Indexing file: {filename}")
                processing_time = index_file(file_path, filename)
                if processing_time:
                    total_time += processing_time
                    file_count += 1

    if file_count > 0:
        average_time = total_time / file_count
        print(f"Total processing time for all files: {total_time:.4f} seconds")
        print(f"Average processing time per file: {average_time:.4f} seconds")
    else:
        print("No files processed.")

directory_path = "source-document"

index_files_in_directory(directory_path)