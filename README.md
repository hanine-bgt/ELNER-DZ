# ELNER-DZ
ELNER-DZ: A Dataset for Named Entity Recognition and Linking in Algerian Arabic Dialect (Darija)


This dataset, titled **ELNER-DZ**, was created by **Bouguettoucha Hadjer Hanine** and **Djouablia Ilhem** as part of our Master’s thesis . It is the **first large-scale dataset** designed for **Named Entity Recognition (NER)** and **Entity Linking (EL)** in **Algerian Arabic Dialect** (Darija), including both **Arabic script** and **Arabizi** (Latin-script).

This dataset contains over **2 million dialectal sentences** labeled with more than **1.9 million named entities** and linked to **Wikidata QIDs**.

---

## 🧾 Dataset Summary

- **Name**: ELNER-DZ
- **Languages**: Arabic (`ar`{For Modern Standard Arabic}, `arq`{For dialectal Arabic}), Arabizi (Latin), French (`fr`), English (`en`)
- **Script**: Arabic script and Latin script (Arabizi)
- **Format**: JSON (single file `data.json`)
- **Annotations**:
  - Named Entity spans (start, end)
  - Entity labels (PER, LOC, ORG, PROD, EVENT, LANG, LAW, MISC, DATE, NORP)
  - Wikidata IDs
  - Normalized canonical forms

---

## 📁 File Structure

The dataset is provided as a single JSON file:

- `data.json`: A list of annotated examples. Each entry includes:
  - `id`: Unique ID of the sentence
  - `text`: Sentence string (Darija in Arabic or Arabizi)
  - `entities`: List of dictionaries with:
    - `start`, `end`: Character offsets of the entity span
    - `label`: NER label (PER, LOC, ORG, etc.)
    - `normalized`: Canonical surface form
    - `wikidata_id`: Corresponding QID from Wikidata

---

## ✨ Example

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
```
## 🏷️ Entity Types

The dataset includes the following entity types (NER labels):

* `PER`: Person
* `LOC`: Location
* `ORG`: Organization
* `PROD`: Product
* `LAW`: Legal concepts or texts
* `LANG`: Language
* `EVENT`: Events
* `DATE`: Dates
* `NORP`: Nationality, Religious, or Political groups
* `MISC`: Miscellaneous
* `SPORT`: Sports and Competitions
* `SYMPTOM`, `DISEASE`: Medical categories

---

## 🧪 Tasks Supported

This dataset can be used for:

* Named Entity Recognition (NER)
* Entity Linking (EL) with Wikidata
* Dialectal NLP in Algerian Arabic
* Multilingual and multiscript NER modeling
* Pretraining or fine-tuning low-resource models

---

## 🧰 How to Use

Install 🤗 Datasets and load the JSON file:

```python
from datasets import load_dataset

dataset = load_dataset("HadjerHaninebgt7878/ELNER-DZ", data_files="data.json", split="train")
print(dataset[0])
```

---

## 🔍 Dataset Details

* **Source**: Social media, forums, dialogues, e-commerce, Wikidata SPARQL
* **Annotation**:

  * Manual and semi-automatic annotation
  * Entity normalization
  * Linking to Wikidata (QIDs)


---

## 👩‍💻 Authors

* **Bouguettoucha Hadjer Hanine**
* **Djouablia Ilhem**



---

## 📄 License

This dataset is licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.

You are free to share, copy, redistribute, adapt, and build upon the material for any purpose, even commercially, **as long as you give appropriate credit**.

🔗 [View full license](https://creativecommons.org/licenses/by/4.0/)

---

## 📚 Citation

Please cite this dataset as:

```bibtex
@dataset{bouguettoucha_djouablia_2025,
  author       = {Bouguettoucha, Hadjer Hanine and Djouablia, Ilhem},
  title        = {ELNER-DZ: A Dataset for Named Entity Recognition and Linking in Algerian Arabic},
  year         = 2025,
  howpublished = {\url{https://huggingface.co/datasets/HadjerHaninebgt7878/ELNER-DZ}},
  url          = {https://doi.org/10.5281/zenodo.xxxxxxx}
}

```



```

