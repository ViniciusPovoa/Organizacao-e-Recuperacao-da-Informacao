import sys
import os
import math
import spacy

nlp = spacy.load("pt_core_news_sm")

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().splitlines()

def preprocess_text(text):
    doc = nlp(text)
    return [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]

def calculate_tf_idf(term_freq, doc_freq, total_docs):
    tf_idf = {}
    for term, freq in term_freq.items():
        tf = 1 + math.log10(freq)
        idf = math.log10(total_docs / doc_freq[term])
        tf_idf[term] = tf * idf
    return tf_idf

def process_documents(base_path):
    documents = {}
    term_doc_freq = {}
    total_docs = 0

    file_paths = read_file(base_path)

    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            terms = preprocess_text(text)
            total_docs += 1

            term_freq = {}
            for term in terms:
                if term in term_freq:
                    term_freq[term] += 1
                else:
                    term_freq[term] = 1

            for term in set(terms):
                term_doc_freq[term] = term_doc_freq.get(term, 0) + 1

            documents[file_path] = term_freq

    return documents, term_doc_freq, total_docs

def write_index_file(documents):
    with open('indice.txt', 'w', encoding='utf-8') as file:
        for doc, term_freq in documents.items():
            file.write(f"{doc}:\n")
            for term, freq in term_freq.items():
                file.write(f"{term}, {freq}\n")

def write_weights_file(documents, term_doc_freq, total_docs):
    with open('pesos.txt', 'w', encoding='utf-8') as file:
        for doc, term_freq in documents.items():
            tf_idf = calculate_tf_idf(term_freq, term_doc_freq, total_docs)
            non_zero_weights = {term: weight for term, weight in tf_idf.items() if weight != 0}
            if non_zero_weights:
                file.write(f"{os.path.basename(doc)}: ")
                for term, weight in non_zero_weights.items():
                    file.write(f"{term}, {weight:.4f} ")
                file.write("\n")

def dot_product(query_vector, document_vector):
    return sum(query_vector.get(term, 0) * weight for term, weight in document_vector.items())

def calculate_magnitude(vector):
    return math.sqrt(sum(weight ** 2 for weight in vector.values()))

def calculate_similarity(query_vector, document_vector):
    dot_prod = dot_product(query_vector, document_vector)
    query_mag = calculate_magnitude(query_vector)
    doc_mag = calculate_magnitude(document_vector)
    if query_mag * doc_mag == 0:
        return 0
    return dot_prod / (query_mag * doc_mag)

def process_query(query, documents, term_doc_freq, total_docs):
    query_terms = preprocess_text(query)
    query_vector = calculate_tf_idf({term: 1 for term in query_terms}, term_doc_freq, total_docs)
    similarities = {}

    for doc, term_freq in documents.items():
        doc_vector = calculate_tf_idf(term_freq, term_doc_freq, total_docs)
        similarity = calculate_similarity(query_vector, doc_vector)
        if similarity >= 0.001:
            similarities[doc] = similarity

    return similarities

def write_response_file(similarities):
    sorted_similarities = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
    with open('resposta.txt', 'w', encoding='utf-8') as file:
        file.write(f"{len(sorted_similarities)}\n")
        for doc, similarity in sorted_similarities:
            file.write(f"{os.path.basename(doc)} {similarity:.4f}\n")

def main():
    if len(sys.argv) != 3:
        print("Uso: python modelo_vetorial.py base.txt consulta.txt")
        sys.exit(1)

    base_path = sys.argv[1]
    query_path = sys.argv[2]

    documents, term_doc_freq, total_docs = process_documents(base_path)
    write_index_file(documents)
    write_weights_file(documents, term_doc_freq, total_docs)

    with open(query_path, 'r', encoding='utf-8') as file:
        query = file.read().strip()

    similarities = process_query(query, documents, term_doc_freq, total_docs)
    write_response_file(similarities)

if __name__ == "__main__":
    main()
