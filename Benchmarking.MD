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

