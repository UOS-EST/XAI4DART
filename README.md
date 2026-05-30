# XAI4DART

Explainable AI (XAI) framework for DART (Developmental And Reproductive Toxicity) prediction.  
This project builds and evaluates machine learning models that predict toxicity endpoints using molecular fingerprints, with SHAP-based interpretability.

---

## Project Structure

```
XAI4DART/
├── data/                         # Input datasets (.xlsx)
├── module/
│   ├── main.py                   # Main training & evaluation pipeline
│   ├── requirements.txt          # Python dependencies
│   ├── runrun.sh                 # Shell script to run pipeline
│   ├── run/                      # Model scripts
│   │   ├── rf.py                 # Random Forest
│   │   ├── gbt.py                # Gradient Boosting
│   │   ├── xgb.py                # XGBoost
│   │   ├── dt.py                 # Decision Tree
│   │   └── logistic.py           # Logistic Regression
│   └── utils/                    # Utility modules
│       ├── read_data.py          # Data loading
│       ├── common.py             # Parameter grid, shared utils
│       ├── model_utils.py        # Model helpers
│       ├── smiles2fing.py        # SMILES → Fingerprint conversion
│       └── logging_utils.py      # Logging
├── val_results/                  # Validation results & best model lists
└── application_EPAA/             # Application to EPAA dataset
    ├── application.py
    ├── app_data.xlsx
    └── app_result/               # Prediction outputs
```

---

## Models

| Model | Description |
|-------|-------------|
| Random Forest (RF) | Ensemble of decision trees |
| Gradient Boosting (GBT) | Sequential boosting ensemble |
| XGBoost (XGB) | Optimized gradient boosting |
| Decision Tree (DT) | Single tree classifier |
| Logistic Regression | Linear baseline |

## Molecular Fingerprints

- Morgan
- MACCS
- RDKit
- Layered

---

## How to Run

```bash
cd module
python main.py
```

Or use the shell script:

```bash
bash runrun.sh
```

Results are saved as `.xlsx` in the `data/` and `val_results/` directories.

---

## Requirements

Install dependencies:

```bash
pip install -r module/requirements.txt
```

Key packages: `scikit-learn`, `xgboost`, `rdkit`, `shap`, `imbalanced-learn`, `pandas`, `openpyxl`
