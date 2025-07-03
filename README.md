# ELNER-DZ: Algerian Arabic Dataset for Named Entity Recognition and Entity Linking

> 📌 **Official DOI**: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15798592.svg)](https://doi.org/10.5281/zenodo.15798592)  
> 🤗 Also available on [Hugging Face](https://huggingface.co/datasets/HadjerHaninebgt7878/ELNER-DZ)  
> 📥 [Download Dataset (.rar from Zenodo)](https://zenodo.org/record/15798592/files/data.rar)

---

This dataset, titled **ELNER-DZ**, was created by **Bouguettoucha Hadjer Hanine** and **Djouablia Ilhem** as part of our Master’s thesis. It is the **first large-scale dataset** designed for **Named Entity Recognition (NER)** and **Entity Linking (EL)** in **Algerian Arabic Dialect** (Darija), including both **Arabic script** and **Arabizi** (Latin-script).

This dataset contains over **2 million dialectal sentences** labeled with more than **1.9 million named entities** and linked to **Wikidata QIDs**.

---

## 🧾 Dataset Summary

- **Name**: ELNER-DZ  
- **Languages**: Arabic (`ar` for MSA, `arq` for dialectal), Arabizi (Latin), French (`fr`), English (`en`)  
- **Script**: Arabic and Latin (Arabizi)  
- **Format**: JSON (compressed in `data.rar`)  
- **Annotations**:
  - Named Entity spans (start, end)
  - NER labels (PER, LOC, ORG, etc.)
  - Normalized forms
  - Wikidata QIDs

---

## 📁 File Structure

- `data/data.rar` — Compressed archive containing `data.json`
- `examples/loading_example.py` — Script to extract and load the dataset
- `LICENSE` — CC-BY-4.0
- `dataset_card.md` — Hugging Face dataset summary

---

## ✨ Example Format

```json
{
  "id": 188,
  "text": "3reft wa7ed lperson khadem f Yassir",
  "entities": [
    {
      "start": 29,
      "end": 35,
      "label": "ORG",
      "wikidata_id": "Q117156470",
      "normalized": "Yassir"
    }
  ]
}
````

---

## 🏷️ Entity Types

* `PER`: Person
* `LOC`: Location
* `ORG`: Organization
* `PROD`: Product
* `LAW`: Legal texts or rules
* `LANG`: Language
* `EVENT`: Events
* `DATE`: Temporal expressions
* `NORP`: Nationality/Religious/Political groups
* `SPORT`: Sports & Competitions
* `SYMPTOM`, `DISEASE`: Medical categories
* `MISC`: Miscellaneous

---

## 🧪 Tasks Supported

* Named Entity Recognition (NER)
* Entity Linking (EL) with Wikidata
* Dialectal NLP in Algerian Arabic
* Code-switching and multiscript modeling
* Low-resource transfer learning

---

## 🧰 How to Use

### ▶️ Requirements

```bash
pip install datasets rarfile
sudo apt-get install unrar    # For Linux
```

### ▶️ Run the loading script

```bash
python examples/loading_example.py
```

Or manually extract and load:

```python
import rarfile
rf = rarfile.RarFile("data/data.rar")
rf.extractall("data/")

from datasets import load_dataset
dataset = load_dataset("json", data_files="data/data.json", split="train")
print(dataset[0])
```

---

## 🔍 Dataset Details

* **Source**: Social media, dialogues, e-commerce, Wikidata SPARQL
* **Annotation**:

  * Semi-automated and rule-based extraction
  * Manual normalization of entity surface forms
  * Wikidata QID linking via SPARQL and fallback search

---

## 👩‍💻 Authors

* **Bouguettoucha Hadjer Hanine**
* **Djouablia Ilhem**


---

## 📄 License

This dataset is licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.

🔗 [View Full License](https://creativecommons.org/licenses/by/4.0/)

---

## 📚 Citation

```bibtex
@dataset{bouguettoucha_djouablia_2025,
  author       = {Bouguettoucha, Hadjer Hanine and Djouablia, Ilhem},
  title        = {ELNER-DZ: A Dataset for Named Entity Recognition and Linking in Algerian Arabic},
  year         = 2025,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.15794817},
  url          = {https://doi.org/10.5281/zenodo.15794817}
}
```

