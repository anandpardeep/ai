from llama_index.core import Document, VectorStoreIndex
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.storage.index_store import SimpleIndexStore

# Load the password policy document
def load_document():
    with open("password_policy_document.txt", "r", encoding="utf-8") as file:
        return file.read()

policy_text = load_document()

# Convert the document into a LlamaIndex Document object
policy_doc = Document(text=policy_text)

print("Loaded document successfully.")
