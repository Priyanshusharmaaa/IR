import pickle

if __name__ == "__main__":
    with open("rbtree_index.pkl", "rb") as f:
        search_engine = pickle.load(f)

    while True:
        query = input("Enter search query (* for wildcard, 'exit' to quit): ")
        if query.lower() == "exit":
            break
        results = search_engine.search(query)
        print("Search Results:", results)
