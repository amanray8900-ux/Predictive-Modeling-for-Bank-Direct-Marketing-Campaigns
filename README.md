# Predictive Modeling for Bank Direct Marketing Campaigns

## Overview
This repository contains a comprehensive data analysis and machine learning project aimed at predicting whether a client will subscribe to a term deposit based on direct marketing campaign data from a Portuguese banking institution. 

The primary goal is to maximize **Recall** for the "subscribed" class (y=1) to ensure potential subscribers are not missed, while also maximizing **Precision** for the "not subscribed" class (y=0) to minimize unnecessary telemarketing calls.

## Dataset
The dataset utilized is the **Bank Marketing Data Set**, specifically `bank-additional-full.csv`. Features include customer demographics, previous campaign contacts, and macroeconomic indicators.

## Modeling Approach
The project involves:
* Extensive Exploratory Data Analysis (EDA) using `pandas`, `matplotlib`, and `seaborn`.
* Data Preprocessing and handling to prepare features for modeling.
* Testing various classifiers including **Gaussian Naive Bayes**, **Bernoulli Naive Bayes**, and **Decision Tree Classifier**.
* Hyperparameter optimization using `RandomizedSearchCV`.

### Results
The optimized Decision Tree Classifier yielded the best results for this specific imbalance problem, successfully achieving:
* **73% Recall** for the targeted `y=1` class (subscriptions)
* **95% Precision** for the `y=0` class (non-subscriptions)

## Project Structure
- `bank_data_analysis.ipynb` - The primary Jupyter Notebook containing the full analysis, modeling, and evaluation pipeline.
- `bank-additional-full.csv` - The raw dataset used for training and evaluation.
- `requirements.txt` - Required python packages.

## Requirements
See `requirements.txt` for the full list of dependencies. You can install them by running:
```bash
pip install -r requirements.txt
```
