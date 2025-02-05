python
# Step 1: Load DNA sequences from a file
from Bio import SeqIO

sequences = []
for record in SeqIO.parse("input.fasta", "fasta"):
    sequences.append(str(record.seq))
print(f"Loaded {len(sequences)} sequences!")

# Step 2: Convert DNA to numbers (one-hot encoding)
import numpy as np

def one_hot_encode(seq):
    mapping = {'A': [1,0,0,0], 'T': [0,1,0,0], 'C': [0,0,1,0], 'G': [0,0,0,1]}
    return [mapping.get(char, [0,0,0,0]) for char in seq]

encoded_data = np.array([one_hot_encode(seq) for seq in sequences])

# Step 3: Train a simple AI model (example: K-Means clustering)
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3)  # Group into 3 clusters
clusters = kmeans.fit_predict(encoded_data.reshape(len(sequences), -1))

# Step 4: Build a tree (simplified example)
# (Replace this with a real tree-building method later!)
print("Clusters (fake 'branches' of the tree):", clusters)


---

### *Step 5: Test Your Code*
1. *Create a test file input.fasta* with DNA sequences. Example:  
   
   >Seq1
   ATGCGTA
   >Seq2
   ATGAGTA
   >Seq3
   CCGATAA
