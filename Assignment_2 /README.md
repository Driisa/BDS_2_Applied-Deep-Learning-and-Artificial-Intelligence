# Portfolio Assignment 2

**Deadline:** Monday, 17th February  
**Title:** Fine-Tuning Transformer Models for Classification  

## Introduction
This assignment focuses on fine-tuning transformer models for classification tasks using modern deep learning techniques. The objective is to develop models capable of effectively classifying text into different categories. We worked on two classification tasks:
- **Binary Classification**
- **Multi-Class Classification**

Using **Hugging Face Transformers**, we fine-tuned pre-trained models and evaluated their performance using relevant metrics.

---

## Task Overview

### 1. Dataset Selection and Preprocessing
- Selected datasets suitable for binary and multi-class classification from **Hugging Face Datasets**.
- Applied necessary preprocessing steps:
  - **Tokenization** using `AutoTokenizer` from Hugging Face.
  - **Handling class imbalance** through techniques such as **oversampling** and **class weighting**.
  - **Splitting data** into training, validation, and test sets.

### 2. Model Selection and Fine-Tuning
- **Transformer-based models used:**
  - **BERT** for Binary Classification
  - **FinBERT** for Multi-Class Classification
- Configured hyperparameters, including:
  - Learning rate, batch size, number of epochs, and early stopping.
- Trained models on **Google Colab** using **GPU acceleration**.

### 3. Evaluation
Model performance was assessed using the following metrics:
- **Binary Classification:** Accuracy, F1-score, Precision, Recall, ROC-AUC.
- **Multi-Class Classification:** Accuracy, Precision, Recall, Macro F1-score.

Analyzed test set results and provided a discussion on model performance.

### 4. Upload to Hugging Face Hub
- Fine-tuned models were uploaded to the **Hugging Face Model Hub**.
- Each model card includes:
  - **Dataset Used:**
    - Hugging Face dataset used for training.
    - Custom synthetic dataset from GitHub.
  - **Training Parameters:**

| Parameter             | Binary Classification | Multi-Class Classification |
|----------------------|----------------------|--------------------------|
| Model Architecture  | BERT                 | FinBERT                   |
| Batch Size         | 16                    | 16                         |
| Learning Rate      | 2e-5                   | 2e-5                       |
| Epochs            | 3                     | 3                          |
| Optimizer         | AdamW                 | AdamW                      |
| Evaluation Metric  | Accuracy, F1-score    | Accuracy, F1-score         |

  - **Evaluation Results:**

| Dataset  | Binary Classification Accuracy | Binary Classification F1 (Weighted) | Binary Classification Precision | Binary Classification Recall | Multi-Class Classification Accuracy | Multi-Class Classification F1 (Weighted) | Multi-Class Classification Precision | Multi-Class Classification Recall |
|---------|--------------------------------|------------------------------------|--------------------------------|-----------------------------|------------------------------------|------------------------------------|--------------------------------|-----------------------------|
| Train Set | 94.3% | 94.2% | 94.4% | 94.3% | 94.3% | 94.2% | 94.4% | 94.3% |
| Test Set | 85.7% | 85.6% | 85.8% | 85.7% | 85.7% | 85.6% | 85.8% | 85.7% |

  - **Intended Use:**
    - ✅ Sentiment analysis on text data.
    - ✅ Classification of financial, news, or medical documents.
    - ✅ NLP-based classification research.
  - **Limitations:**
    - ⚠️ Performance may vary on unseen datasets.
    - ⚠️ Further fine-tuning may be required for domain-specific applications.

---

## Data Sources
- **Hugging Face Datasets** (`datasets` library)
- **GitHub (Synthetic dataset)**

---

## How to Run the Code

### 1. Clone the Repository
```bash
git clone <repository-link>
cd <repository-folder>
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Jupyter Notebook
```bash
jupyter notebook
```
Open `Assignment_2_Binary.ipynb` or `Assignment_2_Multi-class.ipynb` to run training and evaluation.

---

## Group Members & Contributions
- **Daniel S. Riisager** - Binary Classification Model Development
- **Vittorio, Oliver, Daniel** - Multi-Class Classification Model Development
- **Daniel S. Riisager** - Deployment & Documentation
- **Daniel S. Riisager** - Technical Explainer Video

---
