# 🎮 Randomized Tie-Breaking in Reflex Play – CS188 Core Task

This project is an enhancement of the `ReflexAgent` used in the CS188 Artificial Intelligence course (UC Berkeley), focusing on **randomized tie-breaking** to improve agent behavior in environments with move score ambiguity.

---

## 📝 Summary

This project enhances the ReflexAgent by introducing **randomized tie-breaking**. By adding a small random jitter (ε ≤ δ) to move scores, the agent avoids deterministic decisions that often lead to repetitive or suboptimal paths. The implementation supports command-line flags for reproducibility and evaluation over multiple trials, showcasing the effect of randomness in decision-making.

---

## 🧠 Overview

In the standard ReflexAgent, actions with equal scores are chosen deterministically. This can result in the agent making the same decisions repeatedly, even when alternative paths could be more efficient.

To address this, the project introduces **random perturbations** to move scores, encouraging more diverse decision-making behavior.

---

## 🔧 Modifications

- Injected a small random value `ε ~ uniform(0, δ)` to each move score.
- Controlled via CLI flags:
  - `--delta`: Maximum jitter value added to each move score.
  - `--seed`: Optional random seed to ensure reproducibility.

---

## 🛠️ Implementation Details

- Located and modified the score comparison logic within the `ReflexAgent` class.
- Added random jitter using Python’s `random.uniform(0, delta)` function.
- Added support for command-line flags `--delta` and `--seed` for customization and reproducibility.

Example usage:
```bash
python pacman.py -p ReflexAgent --delta 0.05 --seed 42
