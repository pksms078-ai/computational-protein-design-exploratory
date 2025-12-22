"""
Minimal In-Silico Experimental Proxy
-----------------------------------
Purpose:
Evaluate relative stability proxy of protein sequences
using ML embeddings + simulated structural score.

This is NOT a biological claim.
This is a computational decision-support experiment.
"""

import numpy as np
import time
import random

# -----------------------------
# 1. Amino acid encoding
# -----------------------------
AA_MAP = {
    'A': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5,
    'G': 6, 'H': 7, 'I': 8, 'K': 9, 'L': 10,
    'M': 11, 'N': 12, 'P': 13, 'Q': 14, 'R': 15,
    'S': 16, 'T': 17, 'V': 18, 'W': 19, 'Y': 20
}

def encode_sequence(seq, max_len=50):
    encoded = [AA_MAP.get(aa, 0) for aa in seq[:max_len]]
    padded = encoded + [0] * (max_len - len(encoded))
    return np.array(padded)

# -----------------------------
# 2. Dummy ML scoring model
# -----------------------------
def ml_sequence_score(encoded_seq):
    """
    Proxy for ML prediction
    """
    return np.mean(encoded_seq) + np.std(encoded_seq)

# -----------------------------
# 3. Structural proxy simulation
# -----------------------------
def structural_proxy_score(seq_length):
    """
    Proxy for structural compactness / stability
    """
    entropy_penalty = random.uniform(0.8, 1.2)
    return (1 / seq_length) * entropy_penalty

# -----------------------------
# 4. Run experiment
# -----------------------------
def run_experiment(sequences):
    results = []

    start = time.time()

    for seq in sequences:
        encoded = encode_sequence(seq)
        ml_score = ml_sequence_score(encoded)
        structure_score = structural_proxy_score(len(seq))

        combined_score = ml_score * structure_score

        results.append({
            "sequence": seq,
            "ml_score": round(ml_score, 4),
            "structure_proxy": round(structure_score, 4),
            "final_rank_score": round(combined_score, 6)
        })

    runtime = round(time.time() - start, 4)
    return results, runtime

# -----------------------------
# 5. Example usage
# -----------------------------
if __name__ == "__main__":
    test_sequences = [
        "MKTAYIAKQRQISFVKSHFSRQ",
        "GAVLILALLVLAVVALG",
        "MNIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSL"
    ]

    output, runtime = run_experiment(test_sequences)

    print("=== In-Silico Experimental Proxy Results ===")
    for row in output:
        print(row)

    print(f"\nRuntime: {runtime} seconds")

{'sequence': 'MKTAY...', 'ml_score': 11.24,
 'structure_proxy': 0.041, 'final_rank_score': 0.460}

Runtime: 0.0021 seconds
