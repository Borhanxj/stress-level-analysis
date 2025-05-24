# **Stress Level Analysis Based on Socioeconomic and Environmental Factors**

A data science project analyzing the relationship between **stress levels** and **socioeconomic & environmental factors** such as temperature, unemployment rates, salary distribution, cost of living, and demographics. Using statistical analysis and machine learning to uncover patterns and predictive insights.

---

## **📌 Project Overview**
This project explores how external factors—including **economic indicators and climate conditions**—impact stress levels. By analyzing data from multiple sources, I aim to **identify key contributors to stress and develop predictive models**.

### **Key Research Questions**
- How do **unemployment rates and salary distribution** impact reported stress levels?
- Do **environmental conditions** (temperature, rainfall, pollution) correlate with higher stress levels?
- Do **physiological factors** like **respiration rate, body temperature, heart rate**, and **hours of sleep** influence stress?
- Are there **regional or demographic differences** in stress patterns?
- Does the **cost of living** influence mental health outcomes?

---

## **📌 Motivation**
Stress is something many of us experience, but it's also becoming a major public health issue worldwide.  
A recent survey ranked it just behind **cancer and mental health** as one of the biggest concerns, with countries like **South Korea and Turkey** reporting especially high levels.  
Younger people are often more affected, but even a significant number of older adults struggle with stress.  
This makes me wonder—**what’s driving this rise in stress?**  
Could factors like **economic instability, climate conditions, or health factors** play a role?  
**That’s what I want to explore in this project.**  
([Statista](https://www.statista.com/statistics/1057961/the-most-stressed-out-populations-worldwide/?utm_source=chatgpt.com))

---

## **📌 Datasets & Parameters**
This project integrates multiple datasets to analyze stress levels in relation to external factors.

### **1️⃣ Mental Health & Stress Dataset**
📂 **File:** `Stress_Data.csv`  
📌 **Source:** Kaggle Mental Health Dataset  
📌 **Includes:** Stress levels, mental health conditions, work-life balance.  
📌 **Covers:** Multiple countries (Country is a parameter).  

### **2️⃣ Gallup Stress Survey**
📂 **File:** `gallup_emotion_data_2023.csv`  
📌 **Source:** Gallup Global Emotions Report  
📌 **Includes:** Global stress trends based on survey data.  
📌 **Covers:** Multiple countries.  

### **3️⃣ Weather & Climate Dataset**
📂 **File:** `Weather_Data.csv`  
📌 **Source:** Kaggle Weather Dataset  
📌 **Includes:** Temperature, precipitation, pollution levels.  
📌 **Covers:** Multiple countries (Country is a parameter).  

### **4️⃣ Economic Indicators**

#### **a. Global Economic Data**
📂 **File:** `World_Economic_Data.csv`  
📌 **Source:** Kaggle - World Data 2023  
📌 **Includes:** GDP, income levels, unemployment rates.  
📌 **Covers:** Multiple countries (Country is a parameter).  

#### **b. Income Distribution (OECD)**
📂 **File:** `OECD_Income_Data.pdf`  
📌 **Source:** OECD Income Distribution Database  
📌 **Includes:** Salary distribution, income inequality.  
📌 **Covers:** Multiple countries (requires data extraction).  

### **5️⃣ Social Media Usage & Emotion
📂**File:** `social_media_stress.csv`  
📌**Source:** Survey-Based Dataset  
📌**Description:**  
  Individual-level data on platform usage and emotional response. **Note: Cleaning pending.** Intended fields:
  - Daily usage time
  - Posts, likes, comments, messages per day
  - Dominant emotion (e.g., Anxiety, Neutral, etc.)

---

## **📊 Data Collection & EDA**

### 🧼 Data Cleaning Summary

Before performing exploratory data analysis (EDA), we applied structured cleaning operations across all datasets to ensure consistency and reliability:

#### ✅ `Stress_Data.csv` – Cleaning Overview
**Goal:** Prepare individual-level mental health and stress data for analysis by ensuring consistency and removing invalid values.

### Cleaning Steps Performed:
1. **Convert `Age` column to numeric**:
   - Coerce invalid entries to `NaN`.
   - Drop rows with missing or unrealistic age values (e.g., less than 13 or more than 100).

2. **Drop rows with any missing values** in critical columns:
   - `Age`, `Gender`, `Mental_Health_Condition`, `Stress_Level`, `Sleep_Hours`, `Work_Hours`, `Physical_Activity_Hours`.

3. **Normalize categorical values**:
   - Standardize text fields like `Gender`, `Mental_Health_Condition`, and `Stress_Level` to consistent casing (title case).

### 🧾 Cleaning Code
📎 [`clean_stress_data.py`](./data/clean_stress_data.py)

> ✅ Result: A clean and ready-to-use dataset for correlation and predictive modeling.

---

#### ✅ `World_Economic_Data.csv`
**Goal:** Prepare country-level economic indicators for merging with stress survey data and other global indices.

### Cleaning Steps Performed

1. **Removed formatting artifacts**:
   - Stripped `%` signs and commas from the following columns:
     - `Unemployment rate`
     - `CPI`
     - `Life expectancy`
     - `Tax revenue (%)`
     - `Population: Labor force participation (%)`

2. **Converted columns to numeric types** for analysis

### 🧾 Cleaning Code
📎 [`clean_world_economic_data.py`](./data/clean_world_economic_data.py)

---

### 🔗 Merged Dataset Overview

We created a merged dataset combining **country-level stress proportions** from `Stress_Data.csv` with **economic indicators** from `World_Economic_Data.csv`.

📄 **File:** `merged_stress_economics.csv`  
🧩 **Purpose:** To analyze how **economic and healthcare metrics** (e.g., life expectancy, unemployment, physician density) correlate with the **proportion of people reporting high stress**.

This merged dataset was used for our **correlation heatmap** and multiple cross-variable analyses.

---

### 🧪 EDA: Likes, Comments & DMs vs Emotion

📂 **Dataset used:** `social_media_stress.csv`

We explored how different types of social media engagement (likes, comments, and messages) vary based on users' dominant emotional state using violin plots.

📄 **Code file**: [`eda_social_engagement.py`](eda/eda_social_engagement.py)

🧠 **Insights:**
- **Happiness** and **Anxiety** show broader spread in likes and message counts
- **Anger** and **Sadness** are associated with more DMs and comment activity
- Emotional state is reflected in the quantity and variability of online engagement

![Violin Plot - Engagement vs Emotion](eda/violin_engagement_emotion.png)

---

### 🔗 EDA: Correlation Between Stress and Economic Indicators

📂 **Datasets used:** `Stress_Data.csv` + `World_Economic_Data.csv`  
📄 **Merged file:** `merged_stress_economics.csv`

We analyzed how the proportion of people reporting **high stress** correlates with various economic and health indicators across countries.

📄 **Code file**: [`eda_stress_correlation.py`](eda/eda_stress_correlation.py)

🧠 **Insights:**
- High stress levels show **negative correlation** with **life expectancy** and **physician availability**
- Stress is **positively correlated** with **unemployment** and **CPI (inflation)**
- Strong economic and healthcare systems may contribute to reduced national stress

![Stress Correlation Heatmap](eda/stress_correlation_heatmap.png)

---

### 🧠 EDA: Emotional Metrics by Country (Gallup 2023)

📂 **Dataset used:** `Gallup_Stress_Report_2024.pdf` → structured as `gallup_emotion_data_2023.csv`

We visualized five key emotional indicators from Gallup’s global survey: **stress, worry, anger, sadness, and loneliness**.

📄 **Code file**: [`eda_emotion_heatmap.py`](eda/eda_emotion_heatmap.py)

🧠 **Insights:**
- **Israel** and **Guinea** show high levels across multiple emotions
- **Vietnam** and **Canada** report notably low emotional negativity
- The heatmap allows easy country-to-country emotional comparison

![Emotion Heatmap Table](eda/emotion_heatmap_table.png)

---

## 📌 Hypotheses Based on Visualizations

### 1️⃣ Social Media Activity Reflects Emotional State  
📂 **Dataset:** `social_media_stress.csv`  
📊 **Visualization:** Violin plots — Likes, Comments & DMs vs Emotion

> People who feel **anxious** or **sad** are more likely to send **DMs** or leave **comments** instead of just liking posts.  
> This might mean that people with negative emotions try to interact more with others online. It also shows that the **way people use social media** can tell us about their emotional state — not just how much time they spend on it.

---

### 2️⃣ Culture Might Help People Handle Economic Stress  
📂 **Dataset:** `gallup_emotion_data_2023.csv`, `oecd_income_sample.csv`  
📊 **Visualization:** Emotion Heatmap + OECD Income Overlay

> Some **low-income countries** (like **Vietnam**) still show high levels of **positive emotions**.  
> This suggests that **cultural or social support** in these countries might help people feel better, even if the economy isn’t strong.  
> So, **income alone doesn’t explain stress levels** — the environment people live in also matters a lot.

---
## 🧪 Hypothesis Testing

As part of the exploratory phase, we performed statistical hypothesis testing using **independent samples t-tests** to check whether observed differences in our data were statistically significant.

---

### 🧪 Hypothesis Test 1: Social Media Expression and Emotional State

📂 **Dataset used:** `social_media_stress.csv`  
📁 **Code file:** [`hypothesis1_social_media_test.py`](eda/hypothesis1_social_media_test.py)  
🧪 **Method:** Independent Samples t-Test

---

#### 📌 Hypothesis
- **H₀ (Null Hypothesis):** There is no difference in DMs or comments between users who report Anxiety or Sadness and those who don’t.
- **H₁ (Alternative Hypothesis):** Users who report Anxiety or Sadness send significantly more DMs or comments than others.

---

#### 📈 Test Results

- **Messages Sent Per Day:**  
  t = `1.2319`, p = `0.2209`

- **Comments Received Per Day:**  
  t = `0.0805`, p = `0.9360`

---

#### ✅ Conclusion
Since both p-values are greater than 0.05, we **fail to reject the null hypothesis**.  
Although visuals suggested that anxious or sad users might engage more via DMs or comments, the t-test shows that the difference is **not statistically significant** in this dataset.

---

### 🧪 Hypothesis Test 2: Culture May Buffer Against Economic Stress

📂 **Datasets used:** `cleaned_gallup_emotion_data.csv`, `cleaned_oecd_income_data.csv`  
📁 **Code file:** [`hypothesis2_income_vs_emotion_test.py`](eda/hypothesis2_income_vs_emotion_test.py)  
🧪 **Method:** Independent Samples t-Test

---

#### 📌 Hypothesis
- **H₀ (Null Hypothesis):** There is no difference in Positive Experience Index between high-income and low-income countries.
- **H₁ (Alternative Hypothesis):** Low-income countries report significantly different levels of positive emotion compared to high-income countries.

---

#### 📊 Test Results

- **Positive Experience Index (Low vs High Income):**  
  t = `-0.8188`, p = `0.4442`

---

#### ✅ Conclusion
Since the p-value is greater than 0.05, we **fail to reject the null hypothesis**.  
This means that in this dataset, there is **no statistically significant difference** in positive emotions between high-income and low-income countries — even though the original hypothesis suggested there might be.

---

Unfortunately, our alternative hypotheses about external factors contributing to stress levels were not supported, and we failed to reject the null hypotheses. Therefore, in the machine learning model, I will only use physiological features to predict stress levels.

## 📌 Phase 3: Machine Learning Model Design

**Goal:** Transform cleaned mental health data into a format suitable for supervised machine learning.

---

### ✅ Final Cleaning Steps Performed

1. **Dropped irrelevant columns**:
   - `User_ID` (not useful for prediction)
   - `Severity` (omitted for simplification)

2. **Removed incomplete/demographic noise**:
   - Filtered out rows where `Gender` was "Prefer not to say"

3. **Converted `Stress_Level` to binary label**:
   - `High` → `1` (Positive class)
   - All other levels (`Medium`, `Low`) → `0` (Negative class)

Full code is saved here:  
📎 [`prepare_stress_data_for_ml.py`](./data/prepare_stress_data_for_ml.py)

> ✅ Output file: `ml_ready_Stress_Data.csv` – ready to be used for training models in Phase 3.

---

## 📊 Train/Test Data Splitting

Before building machine learning models, we divide the dataset into **features** and **target**, then split them for training and evaluation.

---

### 🧩 Why Split?

- **Features (`X`)**: All columns used as input to predict stress level (e.g., Age, Sleep Hours).
- **Target (`y`)**: The column we want to predict → `Stress_Level` (binary: 1 = High, 0 = Not High).

We perform an **80/20 split**:
- 80% for training the model (`X_train`, `y_train`)
- 20% for evaluating performance on unseen data (`X_test`, `y_test`)

---

### 🧾 Code Used

The full Python script is saved here:  
📎 [`split_data_for_modeling.py`](./models/split_data_for_modeling.py)

This script:
- Loads the final dataset
- Splits into features and target
- Divides the data into training and testing sets
- Saves all parts as separate CSV files for modeling

> ✅ Output: 4 files (`X_train`, `X_test`, `y_train`, `y_test`) are now ready for model training.

---

## Model 1 : Logistic Regression Model

We begin by training a **Logistic Regression** model on our dataset. This serves as a simple and interpretable baseline.

---

### 🧩 Steps Performed

1. **One-hot encoded** all categorical features
2. **Aligned** test and training sets to ensure matching columns
3. **Trained** a logistic regression model with:
   - `max_iter=1000` to ensure convergence
4. **Predicted probabilities** for the test set
5. **Evaluated** performance using:
   - ROC Curve
   - AUC (Area Under the Curve)

---

### 📊 Performance

- **AUC Score:** `0.44` (Weak performance, suggests model is not predictive yet)

---

### Codes:

📎 [`train_logistic_regression.py`](./models/train_logistic_regression.py)
📎 [`train_logistic_regression_with_roc.py`](./models/train_logistic_regression_with_roc.py)

This script handles data preprocessing, training, and ROC plotting.  
> Output image: `roc_logistic_regression.png`

---

## **📌 Project Timeline**
| Date | Task |
|------|------|
| **March 10** | Submit project proposal (GitHub README) |
| **April 18** | Collect and clean data, perform EDA |
| **May 23** | Implement machine learning models |
| **May 30** | Final submission (GitHub repository) |

---

📌 _**This README was structured with guidance from ChatGPT to ensure clarity and completeness.**_
