import streamlit as st
import pickle

# Load the search engine
@st.cache_resource
def load_search_engine():
    with open("rbtree_index.pkl", "rb") as f:
        return pickle.load(f)

search_engine = load_search_engine()

# Streamlit UI
st.title("🔎 Wildcard Search Engine")
st.markdown("Search for words using wildcard patterns like **`pro*`**, **`*ion`**, or **`p*r*l`**.")

# Search bar
query = st.text_input("Enter your search query (e.g., `p*r*l`)", "")

# Search logic
if st.button("Search"):
    if query.strip() == "":
        st.warning("⚠️ Please enter a valid search query.")
    else:
        with st.spinner("Searching..."):
            results = search_engine.search(query)
            if results:
                st.success(f"✅ Found {len(results)} results for query: **{query}**")
                for word, doc_ids in results:
                    st.write(f"- **{word}** (Documents: {', '.join(map(str, doc_ids))})")
            else:
                st.error(f"❌ No results found for query: **{query}**")

# Clear Search History
if st.button("Clear Search History"):
    st.experimental_rerun()

# Footer
st.markdown("---")
st.markdown("💻 **Wildcard Search Engine using RBTree with Streamlit UI** | 🚀 Powered by Python")
