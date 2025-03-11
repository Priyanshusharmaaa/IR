from sortedcontainers import SortedDict
import re  # For efficient pattern matching

class RBTreeSearch:
    def __init__(self):
        self.forward_tree = SortedDict()    # Prefix Search
        self.backward_tree = SortedDict()   # Suffix Search

    # Insert a word into the RBTree
    def add_document(self, document, doc_id):
        words = document.lower().split()
        for word in words:
            # Forward Tree (normal word)
            if word in self.forward_tree:
                self.forward_tree[word].add(doc_id)
            else:
                self.forward_tree[word] = {doc_id}

            # Backward Tree (reversed word)
            reversed_word = word[::-1]
            if reversed_word in self.backward_tree:
                self.backward_tree[reversed_word].add(doc_id)
            else:
                self.backward_tree[reversed_word] = {doc_id}

    # Search functions
    def search(self, query):
        if "*" in query:
            return self._complex_wildcard(query)
        else:
            return [(query, sorted(self.forward_tree.get(query, [])))]

    def _prefix_search(self, prefix):
        results = []
        for word in self.forward_tree:
            if word.startswith(prefix):
                results.append((word, sorted(self.forward_tree[word])))
        return results

    def _suffix_search(self, suffix):
        results = []
        for word in self.backward_tree:
            if word.startswith(suffix[::-1]):  # Reverse logic for suffix search
                results.append((word[::-1], sorted(self.backward_tree[word])))
        return results

    def _complex_wildcard(self, pattern):
        # Convert the wildcard pattern to a regex pattern
        regex_pattern = pattern.replace("*", ".*")
        regex = re.compile(f"^{regex_pattern}$")

        results = []
        for word in self.forward_tree:
            if regex.match(word):
                results.append((word, sorted(self.forward_tree[word])))
        return results
