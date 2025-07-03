
---

## ✅ `loading_example.py` (RAR + Hugging Face Compatible)

```python
"""
Load and explore the ELNER-DZ dataset from a RAR archive.
Author: Bouguettoucha Hadjer Hanine & Djouablia Ilhem
Dataset: https://huggingface.co/datasets/HadjerHaninebgt7878/ELNER-DZ
Zenodo: https://doi.org/10.5281/zenodo.15798592
"""

import os
import rarfile
from datasets import load_dataset

# Paths
rar_path = "../data/data.rar"
json_path = "../data/data.json"

# Step 1: Extract data.json if not already extracted
if not os.path.exists(json_path):
    print("📦 Extracting data.json from data.rar...")
    try:
        rf = rarfile.RarFile(rar_path)
        rf.extractall("../data/")
        print("✅ Extraction complete.")
    except Exception as e:
        print("❌ Failed to extract:", e)
        exit()
else:
    print("✅ data.json already extracted.")

# Step 2: Load dataset using Hugging Face Datasets
print("📚 Loading dataset...")
dataset = load_dataset("json", data_files=json_path, split="train")

# Step 3: Print a sample
print("\n📄 Sample Text:")
print(dataset[0]["text"])

print("\n🔍 Entities:")
for entity in dataset[0]["entities"]:
    span = dataset[0]["text"][entity["start"]:entity["end"]]
    print(f"  - '{span}' | Label: {entity['label']} | Normalized: {entity.get('normalized')} | QID: {entity.get('wikidata_id')}")

print(f"\n📊 Total Samples: {len(dataset)}")
