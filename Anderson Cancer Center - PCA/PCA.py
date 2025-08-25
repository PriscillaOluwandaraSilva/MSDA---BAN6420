import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

# ----- Config -----
SAVE_DIR = "outputs"
os.makedirs(SAVE_DIR, exist_ok=True)
RANDOM_STATE = 42
DO_BONUS_LOGREG = True  # set False if you want to skip logistic regression

# ----- Load & prep data -----
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name="target")  # 0 = malignant, 1 = benign

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ----- PCA (2 components) -----
pca = PCA(n_components=2, random_state=RANDOM_STATE)
X_pca = pca.fit_transform(X_scaled)
pc_df = pd.DataFrame(X_pca, columns=["PC1", "PC2"])
pc_df["target"] = y

explained = pca.explained_variance_ratio_
print(f"Explained variance ratio per component: {explained}")
print(f"Total explained variance (PC1+PC2): {explained.sum():.4f}\n")

# Feature loadings
loadings = pd.DataFrame(
    pca.components_.T,
    index=X.columns,
    columns=["PC1", "PC2"]
)
loadings.to_csv(os.path.join(SAVE_DIR, "pca_loadings.csv"), index=True)

# Top contributing features
for comp in ["PC1", "PC2"]:
    print(f"Top 10 absolute loadings for {comp}:")
    print(loadings[comp].abs().sort_values(ascending=False).head(10))
    print()

# ----- Scatter plot -----
plt.figure(figsize=(8, 6))
for label, marker in [(0, "o"), (1, "s")]:
    subset = pc_df[pc_df["target"] == label]
    plt.scatter(subset["PC1"], subset["PC2"], label=f"{'malignant' if label==0 else 'benign'}", alpha=0.7, marker=marker)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA (2 Components) — Breast Cancer Dataset")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(SAVE_DIR, "pca_scatter.png"), dpi=150)
plt.show()

# Logistic Regression -----
if DO_BONUS_LOGREG:
    X_train, X_test, y_train, y_test = train_test_split(pc_df[["PC1", "PC2"]], y, test_size=0.2, random_state=RANDOM_STATE, stratify=y)
    clf = LogisticRegression(random_state=RANDOM_STATE)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print(f"\nLogistic Regression on 2 PCs — Accuracy: {acc:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=data.target_names))

    cm = confusion_matrix(y_test, y_pred)
    fig = plt.figure(figsize=(5, 4))
    plt.imshow(cm, interpolation="nearest")
    plt.title("Confusion Matrix (LogReg on PCs)")
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.xticks([0, 1], data.target_names)
    plt.yticks([0, 1], data.target_names)
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(j, i, cm[i, j], ha="center", va="center")
    plt.tight_layout()
    fig.savefig(os.path.join(SAVE_DIR, "confusion_matrix.png"), dpi=150)
    plt.show()
    plt. savefig