#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
sys.path.append('../')
import json
import warnings
import joblib
import logging
import numpy as np
from tqdm import tqdm
from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score, roc_auc_score
from utils.read_data import load_data
from utils.common import ParameterGrid
from rdkit import RDLogger
from imblearn.over_sampling import SMOTE
import os
import subprocess
import pandas as pd


# In[ ]:


work_dir = "/Users/Desktop/XAI4DART" 
os.chdir(work_dir)

# PYTHONPATH 
os.environ["PYTHONPATH"] = os.getcwd()


# In[ ]:


# model list
models = ['rf','gbt', 'logistic', 'dt', 'xgb'] 
# molecular fingerprints
fingerprints =  ["Morgan", "MACCS", "RDKit","Layered"]



# performance metrics
columns = ["Model", "Fingerprint", "Validation F1", "Validation Precision", "Validation Recall",
           "Validation Accuracy", "Validation AUC", "Test F1", "Test Precision", "Test Recall",
           "Test Accuracy", "Test AUC"]

results = []


# In[ ]:


for model in models:
    for fingerprint in fingerprints:
        try:
            #script path
            script_path = f"run/{model}.py"
            command = [
                "python",
                script_path,
                "--fingerprint_type", fingerprint,
                "--file_path", "data/ATG_PPARa_TRANS.xlsx", 
                "--model_save_path", "data/ATG_PPARa_TRANS" 
            ]
            print(f"Running: {command}")
            process = subprocess.run(command, capture_output=True, text=True, check=True)
            output = process.stdout
            validation_f1 = next((line.split(":")[-1].strip() for line in output.splitlines() if "Validation F1 Score:" in line), None)
            validation_precision = next((line.split(":")[-1].strip() for line in output.splitlines() if "Validation Precision:" in line), None)
            validation_recall = next((line.split(":")[-1].strip() for line in output.splitlines() if "Validation Recall:" in line), None)
            validation_accuracy = next((line.split(":")[-1].strip() for line in output.splitlines() if "Validation Accuracy:" in line), None)
            validation_auc = next((line.split(":")[-1].strip() for line in output.splitlines() if "Validation AUC:" in line), None)
            test_f1 = next((line.split(":")[-1].strip() for line in output.splitlines() if "Test F1 Score:" in line), None)
            test_precision = next((line.split(":")[-1].strip() for line in output.splitlines() if "Test Precision:" in line), None)
            test_recall = next((line.split(":")[-1].strip() for line in output.splitlines() if "Test Recall:" in line), None)
            test_accuracy = next((line.split(":")[-1].strip() for line in output.splitlines() if "Test Accuracy:" in line), None)
            test_auc = next((line.split(":")[-1].strip() for line in output.splitlines() if "Test AUC:" in line), None)

            # results save
            results.append([model, fingerprint, validation_f1, validation_precision, validation_recall,
                            validation_accuracy, validation_auc, test_f1, test_precision, test_recall,
                            test_accuracy, test_auc])
        except subprocess.CalledProcessError as e:
            print(f"Error while running {model} with {fingerprint}: {e.stderr}")


# In[ ]:


results_df = pd.DataFrame(results, columns=columns)


output_file = "data/ATG_PPARa_TRANS/results.xlsx"
results_df.to_excel(output_file, index=False, engine='openpyxl')
print(f"Results saved to {output_file}")


# In[ ]:




