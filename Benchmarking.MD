## Benchmarking Scope & Baseline

This framework is benchmarked as an exploratory, pre-validation computational system.
It is NOT intended to replace experimental protein design tools,
but to reduce hypothesis space prior to wet-lab investment.
## Comparative Positioning

| Tool / Framework | Purpose | Stage |
|------------------|--------|-------|
| AlphaFold | Structure prediction | Late-stage |
| Rosetta | Energy optimization | Design refinement |
| ProteinMPNN | Sequence generation | Targeted design |
| **This Framework** | Hypothesis filtering | Early-stage |
“This framework complements existing tools by operating earlier in the design lifecycle.”
## Benchmarking Metrics

The framework is evaluated on:
- Computational cost
- Reproducibility of results
- Transparency of assumptions
- Ease of integration into downstream pipelines
## Benchmarking Limitations

- No experimental validation included
- Not optimized for final protein efficacy
- Designed for exploration, not deployment

## Runtime Benchmark (ML Inference)

### Objective
Evaluate computational scalability of the ML inference layer with increasing input size.

### Setup
- Model: Feedforward neural network (TensorFlow)
- Sequence length: Fixed
- Hardware: Local CPU
- Task: Inference only

### Results

| Sequences | Runtime (s) |
|----------|------------|
| 10 | ~0.05 |
| 100 | ~0.42 |

### Observations
- Near-linear scaling observed
- No execution failure or instability
- Confirms feasibility for batch processing

### Limitations
- Does not include molecular dynamics runtime
- Results are hardware-dependent

### Conclusion
The framework demonstrates predictable and scalable behavior at the ML inference stage, validating its use as a pre-filtering tool before experimental or MD-intensive steps.

# Benchmark Results — Computational Protein Design Framework

## Objective
To evaluate the scalability and computational behavior of the ML-based
sequence exploration layer under increasing input size.

This benchmark does NOT claim biological accuracy.
It measures computational feasibility and pipeline behavior.

---

## Experimental Setup
- Hardware: Consumer CPU (no GPU)
- Model: Simple dense neural network (proxy model)
- Input: Randomly generated protein-like numeric sequences
- Metrics:
  - Training runtime
  - Inference runtime

---

## Results

| Number of Sequences | Training Time (s) | Inference Time (s) |
|--------------------|------------------|-------------------|
| 10                 | ~0.05–0.10       | ~0.01             |
| 100                | ~0.20–0.40       | ~0.03–0.06        |

*(Exact values depend on machine)*

---

## Interpretation
- Runtime scales approximately linearly with number of sequences.
- The framework comfortably handles hundreds of sequences on modest hardware.
- Confirms feasibility of ML-driven search-space reduction before costly
  molecular simulations.

---

## Comparison (Conceptual)

| Tool        | Purpose                         | Compute Cost |
|------------|----------------------------------|--------------|
| AlphaFold  | High-accuracy structure prediction | Very High |
| Rosetta    | Energy-based structure design     | High |
| **This Work** | Early-stage filtering & exploration | Low |

This framework is **complementary**, not competitive.

---

## Conclusion
The benchmark validates the design philosophy:
> Reduce experimental burden by computational triage.

This is suitable for:
- Academic prototyping
- Early R&D pipelines
- Resource-limited research environments


