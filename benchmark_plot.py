import matplotlib.pyplot as plt

sequences = [10, 100]
runtime = [2.5, 24]

plt.figure()
plt.plot(sequences, runtime, marker='o')
plt.xlabel("Number of Protein Sequences")
plt.ylabel("Runtime (seconds)")
plt.title("Exploratory Framework Runtime Scaling")
plt.grid(True)
plt.savefig("benchmark_runtime.png")
plt.show()
