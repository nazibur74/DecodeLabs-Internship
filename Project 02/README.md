# AI Project 2: Data Classification Using AI

A beginner-friendly supervised machine learning project that classifies Iris flowers into three species using the **K-Nearest Neighbors (KNN)** algorithm.

## Project Overview

The goal of this project is to build a basic classification model using a small dataset and understand the fundamental supervised learning workflow:

- Load and explore a dataset
- Perform basic data analysis and visualization
- Separate features and target labels
- Split data into training and testing sets
- Scale numerical features
- Train a classification model
- Evaluate model performance

## Dataset

This project uses the built-in **Iris dataset** from Scikit-learn.

- **Total samples:** 150
- **Features:** 4 numerical measurements
- **Classes:** 3 Iris species
- **Samples per class:** 50

### Features

| Feature | Description |
|---|---|
| Sepal Length | Length of the sepal |
| Sepal Width | Width of the sepal |
| Petal Length | Length of the petal |
| Petal Width | Width of the petal |

### Target Classes

- Setosa
- Versicolor
- Virginica

## Technologies & Libraries

- Python
- Google Colab / Jupyter Notebook
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

## Project Workflow

1. Load the Iris dataset.
2. Inspect the dataset using `head()`, `info()`, `describe()`, and null/duplicate checks.
3. Explore the data using count plots, histograms, boxplots, pairplots, and a correlation heatmap.
4. Separate input features (`X`) and target labels (`y`).
5. Split the data into training and testing sets using an 80:20 ratio.
6. Apply `StandardScaler` to standardize the features.
7. Train a KNN classifier.
8. Predict the test-set labels.
9. Evaluate the model using accuracy, confusion matrix, and classification report.
10. Compare different K values and use cross-validation to assess model stability.

## Model

**Algorithm:** K-Nearest Neighbors (KNN)

KNN classifies a new sample based on the labels of its nearest neighbors in the feature space.

- Initial K value: `5`
- Training samples: `120`
- Testing samples: `30`
- Train/test split: `80% / 20%`
- Random state: `42`
- Stratified splitting: Enabled

## Results

### Initial KNN Model (K = 5)

| Metric | Result |
|---|---:|
| Training Accuracy | 97.50% |
| Test Accuracy | 93.33% |
| Correct Test Predictions | 28 / 30 |
| 5-Fold Cross-Validation Mean | 95.83% |

### K Value Comparison

| K | Test Accuracy |
|---:|---:|
| 3 | 93.33% |
| 5 | 93.33% |
| 7 | 96.67% |
| 10 | 96.67% |
| 15 | 96.67% |

The K values 7, 10, and 15 achieved the highest observed test accuracy in this experiment. Cross-validation can be used to select a K value more reliably before evaluating the final model on the held-out test set.

## Evaluation Methods

- **Accuracy:** Percentage of correctly classified test samples.
- **Confusion Matrix:** Shows correct and incorrect predictions for each class.
- **Classification Report:** Includes precision, recall, F1-score, and support.
- **Cross-Validation:** Evaluates model performance across multiple training/validation folds.

## How to Run

1. Open the notebook in Google Colab or Jupyter Notebook.
2. Run the cells in order.
3. The Iris dataset is built into Scikit-learn, so no separate dataset download is required.

## Project Structure

```text
AI-Project-2/
├── Data Classification.ipynb
└── README.md
```

## Learning Outcomes

By completing this project, I practiced:

- Data handling and exploratory data analysis
- Understanding features and target labels
- Train/test splitting
- Feature scaling
- Supervised learning with KNN
- Model evaluation and performance interpretation
- Cross-validation and K value comparison

## Conclusion

This project demonstrates a complete basic classification workflow using the Iris dataset and KNN. The initial K=5 model achieved **93.33% test accuracy**, while experimenting with different K values produced up to **96.67% test accuracy** on the same test split.

---

⭐ If you find this project interesting, feel free to explore the code and experiment with additional chatbot responses.