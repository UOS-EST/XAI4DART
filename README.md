# XAI4DART

**Mechanistically interpretable developmental and reproductive toxicity prediction using AOP-based explainable AI models**

---

## Overview

Developmental and reproductive toxicity (DART) assessment traditionally relies on animal testing, which is resource-intensive and ethically constrained. This study proposes an **AOP (Adverse Outcome Pathway)-anchored explainable AI framework** for DART screening that integrates:

- **In vitro** ToxCast bioassay data (molecular initiating events & key events)
- **In vivo** OECD test guideline data (adverse outcomes)

Machine learning models were developed for individual AOP events and integrated via a rule-based strategy to classify chemicals by DART concern. The framework was validated using the **EPAA NAM Designathon** reference set, achieving an **F1 score of 0.54** — outperforming a conventional in vivo-only model (F1 = 0.46).

---

## Project Structure

```
XAI4DART/
├── data/                    # Input datasets (ToxCast, OECD, etc.)
├── module/
│   ├── main.py              # Main training & evaluation pipeline
│   ├── requirements.txt     # Dependencies
│   ├── runrun.sh            # Shell script runner
│   ├── run/                 # Per-model training scripts
│   │   ├── rf.py            # Random Forest
│   │   ├── gbt.py           # Gradient Boosting
│   │   ├── xgb.py           # XGBoost
│   │   ├── dt.py            # Decision Tree
│   │   └── logistic.py      # Logistic Regression
│   └── utils/               # Data loading, fingerprints, logging
├── val_results/             # Validation results & best model lists
└── application_EPAA/        # Application to EPAA NAM Designathon dataset
```

---

## Models & Molecular Fingerprints

| Models | Fingerprints |
|--------|-------------|
| Random Forest, Gradient Boosting, XGBoost, Decision Tree, Logistic Regression | Morgan, MACCS, RDKit, Layered |

---

## How to Run

```bash
cd module
python main.py
```

---

## Keywords
`DART` · `Adverse Outcome Pathway (AOP)` · `Explainable AI` · `New Approach Methodologies (NAMs)` · `Chemical Prioritization` · `ToxCast` · `OECD`
