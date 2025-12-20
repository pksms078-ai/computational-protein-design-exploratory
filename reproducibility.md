# Reproducibility Statement

This repository is designed as a reproducible exploratory computational research framework.

## Environment
- Python: >= 3.9
- TensorFlow / Keras
- NumPy, Pandas
- MDTraj
- PyMOL (for visualization)
- GROMACS / OpenMM (optional, external)

Exact package versions are documented in `requirements.txt`.

## Determinism & Randomness
- Random seeds can be fixed for ML experiments to ensure reproducibility.
- Molecular dynamics simulations are stochastic by nature; therefore, reproducibility is defined statistically, not identically.

## Data
- No proprietary or experimental wet-lab data is included.
- Users may plug in publicly available protein sequence datasets (e.g., UniProt).

## Reproducible Workflow
1. Encode protein sequences numerically
2. Train ML model for exploratory pattern learning
3. Select candidate sequences
4. Run molecular simulations for structural behavior analysis
5. Document assumptions and results

## Reproducibility Scope
This framework is intended for:
- Hypothesis generation
- Search-space reduction
- Early-stage validation

It does not claim experimental or clinical validation.

## Citation
If used, adapted, or extended, please cite:
DOI: 10.5281/zenodo.17984122
