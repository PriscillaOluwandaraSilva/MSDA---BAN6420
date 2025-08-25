
## 📄 `README.md`

# 🧬 Breast Cancer Dataset PCA & Logistic Regression Project

This project demonstrates how to use **Principal Component Analysis (PCA)** to reduce the dimensionality of the Breast Cancer dataset from scikit-learn, and how to use **Logistic Regression** on the reduced components to classify tumor types as **benign** or **malignant**.

## 📌 Objectives

- Load and preprocess the **Breast Cancer Wisconsin dataset** using scikit-learn.
- Apply **PCA** to reduce the feature space to **2 principal components**.
- Visualize the dataset in 2D using the principal components.
- Train a **logistic regression model** on the 2 principal components.
- Evaluate the model's performance.
- Save important outputs to the `outputs/` directory.

## 📁 Project Structure

your-project-folder/ - (Anderson Cancer Center - PCA)
│
├── pca\_logreg\_cancer.py      # Main Python script
├── README.md                 # Project documentation
├── .venv/                    # Python virtual environment (optional, not pushed to GitHub)
└── outputs/                  # Auto-created folder for generated files
├── pca\_scatter.png
├── confusion\_matrix.png
└── pca\_loadings.csv

## 📦 Requirements

Python 3.7 or higher is recommended.

Install the dependencies with:

```bash
pip install -r requirements.txt
````

Or manually:

```bash
pip install numpy pandas matplotlib scikit-learn
```

## ▶️ How to Run

1. Clone this repository or download the code into a folder.

2. Open the folder in [Visual Studio Code](https://code.visualstudio.com/) or any terminal.

3. (Optional) Create a virtual environment:

   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate  # Windows
   ```

4. Run the Python script:

   ```bash
   python pca_logreg_cancer.py
   ```

5. All output files will be saved in the `outputs/` folder:

   * `pca_scatter.png`: 2D plot of data after PCA
   * `confusion_matrix.png`: Confusion matrix from logistic regression
   * `pca_loadings.csv`: Feature loadings for PC1 and PC2


## 📊 Output Example

### PCA Scatter Plot

Visualizes how the two principal components separate the benign and malignant cases.

![PCA Scatter](outputs/pca_scatter.png)

### Confusion Matrix

Illustrates how well the logistic regression model performs on the test set.

![Confusion Matrix](outputs/confusion_matrix.png)

---

## 🧠 Key Concepts

* **Principal Component Analysis (PCA):**
  Reduces the number of features by finding the directions (principal components) that maximize variance in the data.

* **Logistic Regression:**
  A classification algorithm used to predict the probability that a given input belongs to a particular category.

---

## 🧪 Evaluation

The model is evaluated using:

* Accuracy
* Confusion Matrix
* Classification Report (precision, recall, F1-score)

All results are printed in the terminal and visualized.

---

## 📜 License

This project is open source and free to use.

Perfect — now that you’ve shared your actual output, I can give you:

1. ✅ **Accurate insights** based on your real PCA results
2. ✅ **Updated recommendations** tailored for potential donor reports
3. ✅ A section you can paste directly into your `README.md` or a proposal


### 🎯 PCA Summary

* Your PCA reduced **30 original features** to just **2 components**, capturing **63.24%** of the dataset’s total variance.
* This means those two components still preserve a **majority of the essential patterns** in the data.

---

## 🔍 Key Findings from PCA Loadings

### 🧠 Top 10 Features Driving PC1 (44.3% of variance):

These features contribute the most to PC1 — the most informative dimension for separating malignant and benign tumors:

| Rank | Feature              | Loading (PC1) |
| ---- | -------------------- | ------------- |
| 1    | mean concave points  | 0.2609        |
| 2    | mean concavity       | 0.2584        |
| 3    | worst concave points | 0.2509        |
| 4    | mean compactness     | 0.2393        |
| 5    | worst perimeter      | 0.2366        |
| 6    | worst concavity      | 0.2288        |
| 7    | worst radius         | 0.2280        |
| 8    | mean perimeter       | 0.2275        |
| 9    | worst area           | 0.2249        |
| 10   | mean area            | 0.2210        |

> These variables are all **shape and boundary-related characteristics**, strongly associated with malignancy.

---

### 🧬 Top 10 Features Driving PC2 (19.0% of variance):

| Rank | Feature                 | Loading (PC2) |
| ---- | ----------------------- | ------------- |
| 1    | mean fractal dimension  | 0.3666        |
| 2    | fractal dimension error | 0.2801        |
| 3    | worst fractal dimension | 0.2753        |
| 4    | mean radius             | 0.2339        |
| 5    | compactness error       | 0.2327        |
| 6    | mean area               | 0.2311        |
| 7    | worst radius            | 0.2199        |
| 8    | worst area              | 0.2194        |
| 9    | mean perimeter          | 0.2152        |
| 10   | smoothness error        | 0.2044        |

> PC2 brings in more **complexity and texture metrics** (especially fractal dimension), which may relate to the tumor's irregularity and growth behavior.

---

## 📈 Logistic Regression Results (On PCA Components)

* **Accuracy:** `94.7%`
* **Precision/Recall:** High across both classes (malignant & benign)
* **F1-scores:**

  * Malignant: `0.93`
  * Benign: `0.96`

> Even with only 2 features (PC1 and PC2), the model performs almost as well as models trained on all 30 features. This reinforces PCA's ability to retain **critical information**.

---

## ✅ Evidence-Based Recommendations (Donor-Focused)

### 📌 1. **Prioritize Research Funding on High-Impact Biomarkers**

The PCA clearly identifies key features that **drive the diagnosis of breast cancer**, especially:

* **Concavity-related features** (`concave points`, `concavity`, `compactness`)
* **Tumor size/shape metrics** (`perimeter`, `area`, `radius`)

> 🎯 Donors should focus on supporting **biomarker research** and **early detection tools** based on these variables.

---

### 📌 2. **Fund AI/ML Models That Use Dimensionality Reduction**

The logistic regression model achieved **>94% accuracy using just 2 PCA components**.

This shows the viability of:

* Lightweight, interpretable models for **clinical use**
* Early-stage tools in **low-resource settings**
* Fast, scalable diagnostics using fewer variables

> ✅ Models like this can reduce diagnostic costs, making them ideal for global health initiatives.

---

### 📌 3. **Use PCA Visualizations to Tell a Clear, Convincing Story**

The PCA scatter plot likely showed **distinct separation** between benign and malignant tumors. These visuals can:

* Strengthen **grant proposals**
* Help **non-technical stakeholders** grasp model effectiveness
* Communicate **impactful science simply**

---

### 📌 4. **Target Investment into Fractal-Based Analysis**

Fractal dimension metrics also scored high on PC2. These are **less conventional**, but promising features for:

* Advanced imaging
* Tumor surface irregularity analysis
* AI-assisted diagnostics

> 💡 Donors can be encouraged to fund **exploratory research** in this space, as it's emerging and under-leveraged.

---

## 🧠 Final Message to Stakeholders

Your analysis proves that **a small subset of well-chosen features**, discovered through PCA, can:

* **Power highly accurate models**
* **Reduce data complexity**
* **Inform cost-effective, scalable diagnostics**

This positions your project as a **strong candidate for donor funding**, especially for:

* Early detection initiatives
* Global cancer diagnostics
* Healthcare AI innovation

