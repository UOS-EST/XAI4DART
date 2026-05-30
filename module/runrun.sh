#!/bin/bash

# Conda 환경 활성화
source ~/opt/anaconda3/etc/profile.d/conda.sh
conda activate est_model

# 작업 디렉토리로 이동
cd '/Users/siyeol/UOS/EST LAB/1. Model/Code/Module_v.3'


# PYTHONPATH 설정
export PYTHONPATH=$(pwd)

# 모델 리스트 정의
models=('xgb' 'rf' 'gbt' 'logistic'  'dt')
fingerprints=("Morgan" "MACCS" "RDKit" "Layered")

# Python 스크립트에 결과를 저장할 파일 초기화
output_file="results.csv"

# 헤더 작성
echo "Model,Fingerprint,Validation F1,Validation Precision,Validation Recall,Validation Accuracy,Validation AUC,Test F1,Test Precision,Test Recall,Test Accuracy,Test AUC" > "$output_file"

# 작업 반복 실행
for model in "${models[@]}"; do
    for fingerprint in "${fingerprints[@]}"; do
        # Python 스크립트 실행
        python_output=$(python "run/${model}.py" --fingerprint_type "${fingerprint}" --file_path "data/AOP206_TR.xlsx" --model_save_path "data/AOP206")

        # Extract metrics from the Python script's output using awk
        validation_f1=$(echo "$python_output" | awk '/Validation F1 Score:/ {print $NF}')
        validation_precision=$(echo "$python_output" | awk '/Validation Precision:/ {print $NF}')
        validation_recall=$(echo "$python_output" | awk '/Validation Recall:/ {print $NF}')
        validation_accuracy=$(echo "$python_output" | awk '/Validation Accuracy:/ {print $NF}')
        validation_auc=$(echo "$python_output" | awk '/Validation AUC:/ {print $NF}')
        test_f1=$(echo "$python_output" | awk '/Test F1 Score:/ {print $NF}')
        test_precision=$(echo "$python_output" | awk '/Test Precision:/ {print $NF}')
        test_recall=$(echo "$python_output" | awk '/Test Recall:/ {print $NF}')
        test_accuracy=$(echo "$python_output" | awk '/Test Accuracy:/ {print $NF}')
        test_auc=$(echo "$python_output" | awk '/Test AUC:/ {print $NF}')

        # Append metrics to the output file
        echo "${model},${fingerprint},${validation_f1},${validation_precision},${validation_recall},${validation_accuracy},${validation_auc},${test_f1},${test_precision},${test_recall},${test_accuracy},${test_auc}" >> "$output_file"
    done
done