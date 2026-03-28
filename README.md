# Predictive Modeling for Bank Direct Marketing Campaigns

## 📌 Project Overview
Telemarketing campaigns are resource-intensive for financial institutions. Calling clients who have no interest in subscribing to a new product wastes valuable agent time and can negatively impact customer satisfaction. This project analyzes direct marketing campaign data from a Portuguese banking institution to predict whether a targeted client will subscribe to a term deposit.

**The primary business objective is two-fold:**
1. **Maximize Recall for the "Subscribed" class (y=1):** Ensure that the bank does not miss out on potential customers who are highly likely to subscribe.
2. **Maximize Precision for the "Not Subscribed" class (y=0):** Prevent unnecessary calls to customers who are highly unlikely to subscribe, saving operational costs and avoiding customer fatigue.

## 📊 The Dataset
The project utilizes the `bank-additional-full.csv` dataset, which contains comprehensive information on thousands of past telemarketing interactions. 

**Feature Categories include:**
- **Client Demographics:** Age, job, marital status, education, default status, housing loan, personal loan.
- **Campaign Information:** Contact communication type, month, day of week, duration.
- **Historical Contact Data:** Number of contacts performed during this campaign, in previous campaigns, and outcomes of previous campaigns (poutcome).
- **Macroeconomic Indicators:** Employment variation rate, consumer price index, consumer confidence index, euribor 3 month rate, number of employees.

## ⚙️ Data Preprocessing & Pipeline
Handling imbalanced data correctly is crucial for this project, as the vast majority of clients do *not* subscribe:
- **Exploratory Data Analysis (EDA):** Deep dive into continuous and categorical distributions using `pandas`, `seaborn`, and `matplotlib`.
- **Feature Engineering and Scaling:** Standardization and robust one-hot encoding utilized within scikit-learn `Pipeline` objects to ensure consistent transformations without data leakage.

## 🧠 Models & Hyperparameter Tuning
Two distinct modeling approaches were evaluated. Hyperparameter tuning was conducted using `RandomizedSearchCV`, targeting the `f1-score` metric to directly address the severe class imbalance in the dataset.

### 1. Decision Tree Classifier (The Winner)
* **Untuned:** The initial Decision Tree was highly susceptible to overfitting and struggled to correctly identify the minority class (subscribers).
* **Tuned:** By rigorously tuning tree depth, adjusting `min_samples_split`, and specifically utilizing **`class_weight='balanced'`** to drastically penalize missed subscriptions, the model transitioned into a highly effective targeting tool.
  * **Recall (Subscribed - Class 1): 73%** (Successfully captures nearly 3 out of 4 potential subscribers).
  * **Precision (Not Subscribed - Class 0): 95%** (Extremely confident when eliminating poor leads).

### 2. Gaussian Naive Bayes
* A secondary model evaluated for its inherent ability to work well with categorical relationships and provide probabilistic baseline boundaries. The Decision Tree ultimately outperformed it in the vital Recall metric.

## 🏆 Final Business Conclusion
The extensively tuned **Decision Tree Classifier** expertly balances the bank's dual objectives. Achieving a **73% Recall** for actual subscriptions guarantees that the marketing team is consistently reaching their most lucrative prospects. Concurrently, generating a **95% Precision** for non-subscriptions ensures telemarketing agents aren't wasting hours calling un-convertible leads. By deploying this model, the bank can optimize resource allocation and drastically increase campaign ROI.

## 🚀 How to Run Locally

1. Clone the repository.
2. Install the necessary dependencies (listed in `requirements.txt`):
   ```bash
   pip install -r requirements.txt
   ```
3. Run the primary analysis pipeline via the `bank_data_analysis.ipynb` Jupyter Notebook.
