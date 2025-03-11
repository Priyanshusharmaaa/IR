import os
import pickle
from btree_search import RBTreeSearch

def load_documents_from_directory(directory):
    documents = {}
    for doc_id, filename in enumerate(sorted(os.listdir(directory)), start=1):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
                documents[doc_id] = file.read().strip()
    return documents

if __name__ == "__main__":
    search_engine = RBTreeSearch()

    documents = load_documents_from_directory("C:/Users/DELL/Desktop/docs")

    for doc_id, text in documents.items():
        search_engine.add_document(text, doc_id)

    with open("rbtree_index.pkl", "wb") as f:
        pickle.dump(search_engine, f)

    print("Index successfully built and saved as 'rbtree_index.pkl'.")
