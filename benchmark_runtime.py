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
        print(f"Inference time: {pred_t:.4f} seconds")
        print("-" * 40)

