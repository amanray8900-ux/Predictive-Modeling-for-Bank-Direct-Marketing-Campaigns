import shutil
import os
import sys

# Paths
notebook_src = r"c:\Users\amanr\AppData\Local\Packages\5319275A.WhatsAppDesktop_cv1g1gvanyjgm\LocalState\sessions\4990EA9A35464E9D7A65ED800A221C7812149418\transfers\2026-12\Bank_data_analysis - Copy.ipynb"
dataset_src = r"D:\Local Disk\Downloads\bank-additional-full.csv"

dest_dir = r"C:\Users\amanr\.gemini\antigravity\scratch\Predictive-Modeling-for-Bank-Direct-Marketing-Campaigns"

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir, exist_ok=True)

try:
    if os.path.exists(notebook_src):
        shutil.copy(notebook_src, os.path.join(dest_dir, "bank_data_analysis.ipynb"))
        print("Notebook copied successfully.")
    else:
        print(f"Notebook not found at: {notebook_src}")

    if os.path.exists(dataset_src):
        shutil.copy(dataset_src, os.path.join(dest_dir, "bank-additional-full.csv"))
        print("Dataset copied successfully.")
    else:
        print(f"Dataset not found at: {dataset_src}")
        
except Exception as e:
    print(f"Error: {e}")
