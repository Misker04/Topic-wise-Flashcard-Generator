import nltk
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
nltk.download('punkt')

embedder = SentenceTransformer('all-MiniLM-L6-v2')

def segment_into_chunks(text, chunk_size=5):
    sentences = nltk.sent_tokenize(text)
    chunks = [" ".join(sentences[i:i + chunk_size]) for i in range(0, len(sentences), chunk_size)]
    return chunks

def cluster_chunks(chunks, n_clusters=5):
    embeddings = embedder.encode(chunks)
    n_clusters = min(n_clusters, len(chunks))  # prevent more clusters than chunks
    kmeans = KMeans(n_clusters=n_clusters, random_state=42).fit(embeddings)
    topic_map = {i: [] for i in range(n_clusters)}
    for idx, label in enumerate(kmeans.labels_):
        topic_map[label].append(chunks[idx])
    return topic_map
