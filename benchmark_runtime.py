import time
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# -----------------------------
# Utility: Fake protein sequence generator
# -----------------------------
def generate_sequences(n_sequences, seq_len=50):
    # 20 standard amino acids → numeric encoding
    return np.random.rand(n_sequences, seq_len)

# -----------------------------
# Simple ML model (proxy model)
# -----------------------------
def create_model(input_dim):
    model = Sequential([
        Dense(64, activation='relu', input_shape=(input_dim,)),
        Dense(32, activation='relu'),
        Dense(8, activation='softmax')
    ])
    model.compile(
        optimizer=Adam(learning_rate=0.001),
        loss='categorical_crossentropy'
    )
    return model

# -----------------------------
# Benchmark function
# -----------------------------
def run_benchmark(n_sequences):
    X = generate_sequences(n_sequences)
    y = np.zeros((n_sequences, 8))
    y[:, 0] = 1  # dummy labels

    model = create_model(X.shape[1])

    start_train = time.time()
    model.fit(X, y, epochs=2, batch_size=16, verbose=0)
    train_time = time.time() - start_train

    start_pred = time.time()
    model.predict(X, verbose=0)
    pred_time = time.time() - start_pred

    return train_time, pred_time

# -----------------------------
# Run benchmarks
# -----------------------------
if __name__ == "__main__":
    print("Running benchmark...\n")

    for n in [10, 100]:
        train_t, pred_t = run_benchmark(n)
        print(f"Sequences: {n}")
        print(f"Training time: {train_t:.4f} seconds")

        import time
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# -----------------------------
# Dummy protein sequence encoder
# -----------------------------
def encode_sequence(seq):
    """
    Encodes protein sequence into fixed-length numeric vector.
    This is a proxy encoding for benchmarking only.
    """
    aa_map = {aa: i+1 for i, aa in enumerate("ACDEFGHIKLMNPQRSTVWY")}
    vector = np.zeros(20)
    for aa in seq:
        if aa in aa_map:
            vector[aa_map[aa]-1] += 1
    return vector / max(len(seq), 1)

# -----------------------------
# Generate dummy protein sequences
# -----------------------------
def generate_sequences(n, length=100):
    amino_acids = "ACDEFGHIKLMNPQRSTVWY"
    return [
        "".join(np.random.choice(list(amino_acids), length))
        for _ in range(n)
    ]

# -----------------------------
# Simple ML model (proxy)
# -----------------------------
def create_model():
    model = Sequential([
        Dense(64, activation='relu', input_shape=(20,)),
        Dense(32, activation='relu'),
        Dense(8, activation='softmax')
    ])
    model.compile(
        optimizer=Adam(learning_rate=0.001),
        loss='categorical_crossentropy'
    )
    return model

# -----------------------------
# Benchmark function
# -----------------------------
def run_benchmark(num_sequences):
    sequences = generate_sequences(num_sequences)
    X = np.array([encode_sequence(seq) for seq in sequences])
    
    model = create_model()
    
    start = time.time()
    _ = model.predict(X, verbose=0)
    end = time.time()
    
    return end - start

# -----------------------------
# Main Benchmark Run
# -----------------------------
if __name__ == "__main__":
    for n in [10, 100]:
        runtime = run_benchmark(n)
        print(f"Sequences: {n} | Runtime: {runtime:.4f} seconds")

        print(f"Inference time: {pred_t:.4f} seconds")
        print("-" * 40)

import time
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# -----------------------------
# Dummy protein sequence encoder
# -----------------------------
def encode_sequence(seq_length=100):
    """
    Simulates numerical encoding of a protein sequence
    """
    return np.random.rand(20)

# -----------------------------
# Simple ML model (proxy)
# -----------------------------
def create_model():
    model = Sequential([
        Dense(64, activation="relu", input_shape=(20,)),
        Dense(32, activation="relu"),
        Dense(16, activation="softmax")
    ])
    model.compile(optimizer="adam", loss="categorical_crossentropy")
    return model

# -----------------------------
# Benchmark function
# -----------------------------
def benchmark(num_sequences):
    model = create_model()

    start_time = time.time()

    for _ in range(num_sequences):
        encoded_seq = encode_sequence()
        encoded_seq = np.expand_dims(encoded_seq, axis=0)
        _ = model.predict(encoded_seq, verbose=0)

    end_time = time.time()
    return end_time - start_time

# -----------------------------
# Run benchmarks
# -----------------------------
if __name__ == "__main__":
    sizes = [10, 100]

    print("Benchmarking Computational Protein Design Pipeline")
    print("-" * 50)

    for size in sizes:
        runtime = benchmark(size)
        print(f"Sequences: {size} | Runtime: {runtime:.4f} seconds")


