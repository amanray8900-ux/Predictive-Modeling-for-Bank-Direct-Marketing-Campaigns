# 📈 Predictive Modeling for Bank Direct Marketing Campaigns
*An End-to-End Machine Learning Pipeline to Optimize Telemarketing ROI*

## 📊 Executive Summary
In the retail banking sector, telemarketing is a highly resource-intensive operation. Calling every client in a database drives up operational costs and induces customer fatigue, while failing to contact genuinely interested clients results in direct revenue loss. 

This project develops a predictive framework to identify potential term-deposit subscribers from a dataset of 41,188 marketing records. The core business objective is twofold: **Maximize Recall for the 'Subscribed' class (y=1)** to ensure potential conversions are not missed, and **Maximize Precision for the 'Not Subscribed' class (y=0)** to confidently filter out uninterested clients, saving telemarketers' time.

## 🛠️ Data Architecture & Preprocessing
To build a robust, production-ready system, all data preprocessing was strictly contained within Scikit-Learn `Pipeline` and `ColumnTransformer` objects. This prevents data leakage during cross-validation and ensures the model can seamlessly ingest new, raw customer records.

### Feature Engineering (`ColumnTransformer`)
Customer demographics, previous campaign contacts, and macroeconomic indicators were handled systematically:
* **Numerical Scaling:** Applied `RobustScaler` to features like `age`, `duration`, and macroeconomic indicators (`euribor3m`, `cons.price.idx`) to handle outliers and normalize variance.
* **Categorical Encoding:** Applied `OneHotEncoder(handle_unknown='ignore')` to nominal features such as `job`, `marital`, `education`, and `contact` type.
* **Imbalance Handling:** Integrated SMOTE within the pipeline to synthesize minority class (y=1) records during the training phase without leaking into the validation sets.

## 🤖 Modeling Strategy
To deeply explore model behavior and ensure high interpretability for non-technical stakeholders, the modeling phase was intentionally restricted to **two classifiers**. 

Both models were seamlessly integrated into the end-to-end `Pipeline` and optimized using `RandomizedSearchCV`.

1. **Gaussian Naive Bayes (`GaussianNB`)**
   * *Why:* Serves as a strong probabilistic baseline, particularly effective given the continuous macroeconomic indicators present in the dataset.
   * *Evaluation:* Analyzed for its ability to handle the conditional independence assumption among customer financial metrics.

2. **Decision Tree Classifier (`DecisionTreeClassifier`)**
   * *Why:* Highly interpretable. It allows business stakeholders to trace the exact decision paths (e.g., how the `euribor3m` rate combined with `poutcome` influences the final prediction).
   * *Tuning:* Heavily constrained via hyperparameter tuning (e.g., `max_depth`, `min_samples_leaf`) to prevent overfitting on the imbalanced data.

## 📈 Results & Business Implementation

The optimized **Decision Tree Classifier** yielded the best performance for this specific imbalance problem, achieving:
* **73% Recall** for Subscriptions (`y=1`) — Capturing nearly three-quarters of all potential subscribers.
* **95% Precision** for Non-Subscriptions (`y=0`) — Ensuring 95% of the clients the model recommended *skipping* were indeed non-subscribers.

**Business Impact:** By deploying this pipeline, the bank can confidently reduce its total outbound call volume. Telemarketers can focus exclusively on the high-probability segments identified by the model, drastically reducing operational costs while preserving the vast majority of term-deposit revenue.

## 📁 Repository Structure
```text
├── bank_data_analysis.ipynb   # Full modeling pipeline, EDA, and Pipeline construction
├── bank-additional-full.csv   # Raw dataset (Portuguese banking institution)
├── requirements.txt           # Dependency list
└── README.md

